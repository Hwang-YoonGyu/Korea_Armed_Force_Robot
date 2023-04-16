# YOLO 동영상 처리
# -*- coding: utf-8 -*- # 한글 주석쓰려면 이거 해야함
import math
import cv2
import numpy as np
import time
import serial
import serial.tools.list_ports

z = 30 # 높이

#### 아두이노 로봇팔 연결 안했을 때 주석 처리해야하는 부분 시작 #####
# Find USB Port
# def find_port():  #Finds which port the arduino is plugged into
#     ports = list(serial.tools.list_ports.comports())
#     for p in ports:
#         if '0403' in p[2]: #unique to Osepp Uno (arduino clone)
#             return p[0]
#     print(p[0])
# find_port()

# 포트 번호는 현재 본인의 컴퓨터에 따라 다르니 알아서 수정
# ArduinoSerial = serial.Serial('/dev/cu.usbmodem14401', 9600, timeout=0.1) # 아두이노 시리얼 포트 연결
#### 아두이노 로봇팔 연결 안했을 때 주석 처리해야하는 부분 끝 #####

# 파일 가져오기 -> 이걸 파이카메라로 가져와야함 -> 아래의 cap 변수 변형
file_name = 'chairtest.mp4' # 파일이 위치한 절대주소를 입력
min_confidence = 0.5

# 물체 찾기
def detectAndDisplay(frame):
    start_time = time.time() # 프레임 단위 타이머 시작
    img = cv2.resize(frame, None, fx=0.4, fy=0.4) # 이미지 크기 변환
    height, width, channels = img.shape # img.shape[] 변수에 저장 행=[1], 열=[0]

    cv2.imshow("Original Image", img)

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob) # net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        # Detected된 Object별 iteration
        for detection in out:
            # class score는 detetection배열에서 5번째 이후 위치에 있는 값. 즉 6번쨰~85번째 까지의 값
            scores = detection[5:]
            # scores배열에서 가장 높은 값을 가지는 값이 class confidence, 그리고 그때의 위치 인덱스가 class id
            class_id = np.argmax(scores)
            # 5번쨰 값은 objectness score이다. 객체인지 아닌지의 확률이다. 6번쨰~85번째 까지의 값이 그 객체일 확률 값이다.
            confidence = scores[class_id]
            if confidence > min_confidence:
                # Object detected
                # detection은 scale된 좌상단, 우하단 좌표를 반환하는 것이 아니라, detection object의 중심좌표와 너비/높이를 반환
                # 원본 이미지에 맞게 scale 적용 및 좌상단, 우하단 좌표 계산
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

                # 사각형의 좌표값 알고 싶으면 이거 주석 해제
                # print("class name:",class_id, "point car:", )
                # print("Center x좌표:", center_x, "y좌표:", center_y)
                # print("박스 x좌표:", x, "y좌표:", y)

    # 인덱스들을 모아서 가장 확률이 높은걸로 박스 하나로 통일 여러 박스를 하나로 만드는 작업
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, min_confidence, 0.4)

    print("len(indexes): ", len(indexes))

    font = cv2.FONT_HERSHEY_PLAIN # 그냥 폰트 설정

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i] # 좌상단, 우하단, 사물의 w, h

            object_index = classes.index(classes[class_ids[i]])

            #### 아두이노 로봇팔 연결 안했을 때 주석 처리해야하는 부분 시작 #####
            ### 수정
            # sending coordinates to Arduino
            if (object_index == 56): # z == 56 은 chair(의자)를 의미함, 따라서 다른걸 찾고싶다면 56을 바꿔주면 되는데 # 찾고싶은 물체를 z로 칭한다면, 물체의 인덱스는 coco.names 파일에 있는 물체 이름 줄 번호 -1 을 하면됨
                if (x < 320):
                    x1 = 320 - x;
                    d1 = np.arctan(x1 / y) * 180 / np.pi
                else:
                    x1 = x - 320
                    d1 = np.arctan(x1 / y) * 180 / np.pi + 90

                # print("type(d1): ", type(d1))
                d1 = int(d1)
                print("d1 : ", d1)

                send_d1 = 'd{}'.format(d1) # format을 사용하게되면 str형으로 바뀜
                # ArduinoSerial.write(send_d1.encode('utf-8'))
                # ArduinoSerial.write([d1]) # 정수 전달 방법?
                # print("type(send_d1): ", type(send_d1))

                x_mid = 'X{}'.format((x + w // 2))
                print(x_mid)
                # ArduinoSerial.write(x_mid.encode('utf-8'))

                y_mid = 'Y{}'.format((y + h // 2))
                print(y_mid)
                # ArduinoSerial.write(y_mid.encode('utf-8'))

                object_index = 'z{}'.format(object_index)
                print(object_index)
                # ArduinoSerial.write(cla.encode('utf-8'))

                x_mid2 = (x + w) // 2
                y_mid2 = (y + h) // 2

                a = (x_mid2*x_mid2+y_mid2*y_mid2+z*z-240*240-350*350)/(2*240*350)
                b = np.sqrt(1 - a * a)
                xn = np.sqrt(x_mid2 * x_mid2 + y_mid2 * y_mid2)
                zn = z
                k1 = 240 + 350 * a
                k2 = 350 * b

                st1 = (np.arctan(y_mid2/x_mid2))*180/np.pi
                st2 = (np.arctan2(k1*zn-k2*xn, k1*xn-k2*zn))*180/np.pi
                st3 = (np.arctan2(b, a))*180/np.pi
                st4 = ((-st2)-(st3))*180/np.pi

                print("st1 : ", st1)
                print("st2 : ", st2)
                print("st3 : ", st3)
                print("st4 : ", st4)

                st1 = 'a{}'.format(st1)
                print(st1)

                st2 = 'b{}'.format(st2)
                print(st2)

                st3 = 'c{}'.format(st3)
                print(st3)

                st4 = 'd{}'.format(st4)
                print(st4)

                # ArduinoSerial.write(st1.encode('utf-8'))
                # ArduinoSerial.write(st2.encode('utf-8'))
                # ArduinoSerial.write(st3.encode('utf-8'))
                # ArduinoSerial.write(st4.encode('utf-8'))


            ###################
            #### 아두이노 로봇팔 연결 안했을 때 주석 처리해야하는 부분 끝 #####

            # label = "{}: {:.2f}%".format(classes[class_id[i]], confidences[i] * 100)
            label = "index: {}: {:.2f}%".format(classes.index(classes[class_ids[i]]), confidences[i] * 100)
            print(label)

            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 1, color, 1)

    end_time = time.time() # 시간 계산 종료
    process_time = end_time - start_time # 시간계산 출력용
    print("=== A frame took {:.3f} seconds".format(process_time))
    cv2.imshow("YOLO Video", img)


# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg") # 파일이 위치한 절대주소 입력, weights, cfg 파일 순서 중요

classes = []

with open("coco.names", "r") as f: # 파일이 위치한 절대주소 입력
    classes = [line.strip()
               for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# -- 2. Read the video stream
cap = cv2.VideoCapture(file_name)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame) # 프레임 단위로 전송
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xff == ord('q'): # waitkey(1)을 waitkey(0)으로 바꾸면 첫번째프레임만 전송 후 정지상태
        break

cv2.destroyAllWindows()
