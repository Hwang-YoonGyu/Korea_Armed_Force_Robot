
import cv2  # opencv 사용
import numpy as np
import time
import paho.mqtt.client as mqtt
import math

# 원본 영상 읽기
# 흰색, 노란색 범위 필터링하여 후보로 저장
# 영상을 graySclae로 변환
# Canny Edge Detection알고리즘 edge추출
# gaussian_blur filter
# ROI
# Hough 변환

trap_height = 0.4
global topic
global image

def grayscale(img):  # Grayscale
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
def filter_colors(img):  # 색깔 필터링

    # Filter white pixels
    lower_white = np.array([200, 200, 200])
    upper_white = np.array([255, 255, 255])
    white_mask = cv2.inRange(image, lower_white, upper_white)

    white_image = cv2.bitwise_and(image, image, mask=white_mask)

    # Filter yellow pixels
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([10, 100, 100])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    yellow_image = cv2.bitwise_and(image, image, mask=yellow_mask)

    # Combine the two above images
    image2 = cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)

    return image2
def canny(img, low_threshold, high_threshold):  # Canny 알고리즘
    return cv2.Canny(img, low_threshold, high_threshold)
def gaussian_blur(img, kernel_size):  # 가우시안 필터
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
def region_of_interest(img, vertices, vertices_stopLine, color3=(255, 255, 255), color1=255):  # ROI 셋팅

    mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지
    mask_stopLine = np.zeros_like(img)

    if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
        color = color3
    else:  # 흑백 이미지(1채널)라면 :
        color = color1

    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
    cv2.fillPoly(mask, vertices, color)
    cv2.fillPoly(mask_stopLine, vertices_stopLine, color)

    # 이미지와 color로 채워진 ROI를 합침
    ROI_image_line = cv2.bitwise_and(img, mask)
    ROI_image_stopLine = cv2.bitwise_and(ROI_image_line, mask_stopLine)
    ROI_image = cv2.bitwise_or(ROI_image_stopLine, ROI_image_line)

    cv2.imshow("mask", mask)
    cv2.imshow("mask_Stop", mask_stopLine)
    cv2.imshow("ROI_imgae", ROI_image)
    return ROI_image
# def region_of_interest_stopLine(img, vertices_stopLine, color3=(255, 255, 255), color1=255):  # ROI 셋팅
#
#     mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지
#
#     if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
#         color = color3
#     else:  # 흑백 이미지(1채널)라면 :
#         color = color1
#
#     # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
#     cv2.fillPoly(mask, vertices_stopLine, color)
#
#     # 이미지와 color로 채워진 ROI를 합침
#     ROI_image_stopLine = cv2.bitwise_and(img, mask)
#
#     cv2.imshow("mask_stopLine", mask)
#
#     return ROI_image_stopLine
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # 허프 변환
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #print("img.shape[0]:", img.shape[0]) #height
    #print("line_img:", line_img)

    draw_lines(line_img, lines)

    return line_img
def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    # 기울기 찾고 계산
    # 선의 분류 (left , right)
    # 선들의 교차점을 통해 운전진행 방향 예측

    # 에러 일경우 선을 긋지 않는다.
    if lines is None:
        return
    if len(lines) == 0:
        return
    draw_right = True
    draw_left = True

    # 모든 기울기 찾기
    # abs(slope) > slope_threshold : 기울기가 너무 수평인 선은 제외한다.
    slope_threshold = 0.5 # 기울기 값 선택 , 확률 50%
    slopes = []
    new_lines = []

    for line in lines:
        x1, y1, x2, y2 = line[0]  # line = [[x1, y1, x2, y2]]

        # 기울기 계산
        if x2 - x1 == 0.:  # 코너링에서 0으로 나뉘는 것을 배제
            slope = 999.  # practically infinite slope
        else:
            slope = (y2 - y1) / (x2 - x1)

        # 기울기가 수평인 선을 제외
        if abs(slope) > slope_threshold:
            slopes.append(slope)
            new_lines.append(line)

    lines = new_lines

    # 선들 좌우 선으로 분류
    # Right/left lane lines must have positive/negative slope, and be on the right/left half of the image
    right_lines = []
    left_lines = []

    for i, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        img_x_center = img.shape[1] / 2  # center
        if slopes[i] > 0 and x1 > img_x_center and x2 > img_x_center:
            right_lines.append(line)
            right_detect = True
        elif slopes[i] < 0 and x1 < img_x_center and x2 < img_x_center:
            left_lines.append(line)
            left_detect = True

    # 선형 회귀를 통해 좌우 차선 각각의 가장 적합한 선을 찾기
    # 오른쪽 라인 코스
    right_lines_x = []
    right_lines_y = []

    for line in right_lines:
        x1, y1, x2, y2 = line[0]

        right_lines_x.append(x1)
        right_lines_x.append(x2)

        right_lines_y.append(y1)
        right_lines_y.append(y2)

    if len(right_lines_x) > 0:
        right_m, right_b = np.polyfit(right_lines_x, right_lines_y, 1)  # y = m*x + b
    else:
        right_m, right_b = 1, 1
        draw_right = False

    # 왼쪽 라인 코스
    left_lines_x = []
    left_lines_y = []

    for line in left_lines:
        x1, y1, x2, y2 = line[0]

        left_lines_x.append(x1)
        left_lines_x.append(x2)

        left_lines_y.append(y1)
        left_lines_y.append(y2)

    if len(left_lines_x) > 0:
        left_m, left_b = np.polyfit(left_lines_x, left_lines_y, 1)  # y = m*x + b
    else:
        left_m, left_b = 1, 1
        draw_left = False

    # Find 2 end points for right and left lines, used for drawing the line
    # y = m*x + b --> x = (y - b)/m -> 2개의 기울기 구하기
    y1 = img.shape[0]
    y2 = img.shape[0] * (1 - trap_height)

    right_x1 = (y1 - right_b) / right_m
    right_x2 = (y2 - right_b) / right_m

    left_x1 = (y1 - left_b) / left_m
    left_x2 = (y2 - left_b) / left_m

    # float -> int 변환
    y1 = int(y1)
    y2 = int(y2)
    right_x1 = int(right_x1)
    right_x2 = int(right_x2)
    left_x1 = int(left_x1)
    left_x2 = int(left_x2)

    # 예측
    thres_vp = 15

    # 교차점
    vx = (left_b - right_b) / (right_m - left_m)

    if (vx < img_x_center - thres_vp):
        client.publish("drive", 'l', qos=0)
        #print("left")
    elif (vx > img_x_center + thres_vp):
        client.publish("drive", 'r', qos=0)
        #print("right")
    elif (vx >= (img_x_center - thres_vp) and vx <= (img_x_center + thres_vp)):
        client.publish("drive", 's', qos=0)
        #print("straight")



    # 오른쪽 왼쪽 선그리기
    if draw_right:
        cv2.line(img, (right_x1, y1), (right_x2, y2), color, thickness)
    if draw_left:
        cv2.line(img, (left_x1, y1), (left_x2, y2), color, thickness)
def weighted_img(img, initial_img, α=1, β=1., λ=0.):  # 두 이미지 operlap 하기
    return cv2.addWeighted(initial_img, α, img, β, λ)
def LineTrace(img):
    global image
    image = img

    height, width = image.shape[:2]  # 이미지 높이, 너비q
    #("height:", height, "width:", width)
    #print("height/2:", height/2, "width/2:", width/2)
    filter_img = filter_colors(image)
    gray_img = grayscale(filter_img)  # 흑백이미지로 변환
    blur_img = gaussian_blur(gray_img, 3)  # Blur 효과
    canny_img = canny(blur_img, 50, 170)  # Canny edge 알고리즘

    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)
    #print("width, height", vertices)
    # vertices_stopLine ROI 설정
    # filter_img_stopLine = filter_colors(image)
    # gray_img_stopLine = grayscale(filter_img_stopLine)  # 흑백이미지로 변환
    # blur_img_stopLine = gaussian_blur(gray_img_stopLine, 3)  # Blur 효과
    # canny_img_stopLine = canny(blur_img_stopLine, 50, 170)  # Canny edge 알고리즘

    vertices_stopLine = np.array(
        [[(100, 400), (100, 300), (860, 300), (860, 400)]],
        dtype=np.int32)
    # ROI_img_stopLine = region_of_interest_stopLine(canny_img, vertices_stopLine)
    # hough_img_stopLine = hough_lines(ROI_img_stopLine, 1, 1 * np.pi / 180, 30, 10, 20)
    # result_stopLine = weighted_img(hough_img_stopLine, image)
    # cv2.imshow("result_stopLine", result_stopLine)

    ROI_img = region_of_interest(canny_img, vertices, vertices_stopLine)  # ROI 설정
    #hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # 허프 변환
    hough_img = hough_lines(ROI_img, 1, 1 * np.pi / 180, 30, 10, 20)  # 허프 변환
    result = weighted_img(hough_img, image)  # 원본 이미지에 검출된 선 overlap
    #result_ori_stop = weighted_img(result, result_stopLine)
    # cv2.imshow("result_ori_stop", result_ori_stop)
    cv2.imshow('result', result)  # 결과 이미지 출력
    cv2.imshow("roi", ROI_img)
    cv2.waitKey()


    # Release
    #cap.release()
    cv2.destroyAllWindows()
def on_connect(client, userdata, flag, rc):
    print("Connected")
    client.subscribe("image", qos=0)
    global image
    image = cv2.imread('Capture.JPG')
    LineTrace(image)
def on_message(client, userdata, msg):
    image = msg.payload
    imageArray = np.frombuffer(image, dtype=np.uint8)
    img =cv2.imdecode(imageArray, cv2.IMREAD_COLOR)
    LineTrace(img)
    """cv2.imshow("img",img)
    cv2.waitKey()
    cv2.destroyWindow()"""

#ip = input("ip >> ")
#ip = "localhost "



client = mqtt.Client()
#client.connect('broker.hivemq.com', 8000)
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883)
client.loop_forever()


#cap = cv2.VideoCapture('qwe.jpg')
#cap = cv2.VideoCapture('123.mp4')
#cap = cv2.VideoCapture('solidWhiteRight.mp4')  # 동영상 불러오기
#cap = cv2.VideoCapture('solidYellowLeft.mp4')  # 동영상 불러오기
#cap = cv2.VideoCapture('비디오.mov')





"""while (cap.isOpened()):
    ret, image = cap.read()

    height, width = image.shape[:2]  # 이미지 높이, 너비q
    #("height:", height, "width:", width)
    #print("height/2:", height/2, "width/2:", width/2)

    filter_img = filter_colors(image)
    gray_img = grayscale(filter_img)  # 흑백이미지로 변환
    blur_img = gaussian_blur(gray_img, 3)  # Blur 효과
    canny_img = canny(blur_img, 50, 170)  # Canny edge 알고리즘

    vertices = np.array(
        [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
        dtype=np.int32)

    #print("width, height", vertices)

    ## vertices_stopLine ROI 설정

    # filter_img_stopLine = filter_colors(image)
    #
    # gray_img_stopLine = grayscale(filter_img_stopLine)  # 흑백이미지로 변환
    #
    # blur_img_stopLine = gaussian_blur(gray_img_stopLine, 3)  # Blur 효과
    #
    # canny_img_stopLine = canny(blur_img_stopLine, 50, 170)  # Canny edge 알고리즘

    vertices_stopLine = np.array(
        [[(100, 400), (100, 300), (860, 300), (860, 400)]],
        dtype=np.int32)

    # ROI_img_stopLine = region_of_interest_stopLine(canny_img, vertices_stopLine)
    # hough_img_stopLine = hough_lines(ROI_img_stopLine, 1, 1 * np.pi / 180, 30, 10, 20)
    # result_stopLine = weighted_img(hough_img_stopLine, image)
    #
    # cv2.imshow("result_stopLine", result_stopLine)
    ##########

    ROI_img = region_of_interest(canny_img, vertices, vertices_stopLine)  # ROI 설정

    ## 여기부터 생각 다시 수정필요
    # hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):  # 허프 변환
    hough_img = hough_lines(ROI_img, 1, 1 * np.pi / 180, 30, 10, 20)  # 허프 변환
    result = weighted_img(hough_img, image)  # 원본 이미지에 검출된 선 overlap

    # result_ori_stop = weighted_img(result, result_stopLine)

    # cv2.imshow("result_ori_stop", result_ori_stop)
    cv2.imshow('result', result)  # 결과 이미지 출력
    cv2.imshow("roi", ROI_img) 
    #integer = input(">>")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #1time.sleep(0.1)

"""


LineTrace()
client.loop_stop()
client.disconnect()