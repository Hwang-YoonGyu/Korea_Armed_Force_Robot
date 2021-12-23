import io

import cv2 # opencv 사용
import numpy as np
import time
import paho.mqtt.client as mqtt
import math
import camera
from PIL import Image
import arduinoHeader



order = ""
global mode
mode = "mode3"

def on_message(client, userdata, msg):
    global order
    global mode
    command = msg.payload.decode("utf-8")

    print("receive " + command)
    if (msg.topic == "drive"):
        time.sleep(1)

        if command == "go1":
            if ( order != command):
                order = command
                arduinoHeader.MGo1()
            if (mode == "mode1"):
                cameraPub()
        if command == "go2":
            if ( order != command):
                order = command
                arduinoHeader.MGo2()
        if command == "go3":
            if ( order != command):
                order = command
                arduinoHeader.MGo3()
        if command == "go4":
            if ( order != command):
                order = command
                arduinoHeader.MGo4()
        if command == "go5":
            if ( order != command):
                order = command
                arduinoHeader.MGo5()
        if command == "go6":
            if ( order != command):
                order = command
                arduinoHeader.MGo6()
        if command == "go7":
            if ( order != command):
                order = command
                arduinoHeader.MGo7()
        if command == "go8":
            if ( order != command):
                order = command
                arduinoHeader.MGo8()
        if command == "go9":
            if ( order != command):
                order = command
                arduinoHeader.MGo9()
        if command == "fgo1":
            if (order != command):
                order = command
                arduinoHeader.FGo1()
                if (mode == "mode1"):
                    cameraPub()
        if command == "fgo2":
            if (order != command):
                order = command
                arduinoHeader.FGo2()
        if command == "fgo3":
            if (order != command):
                order = command
                arduinoHeader.FGo3()
        if command == "fgo4":
            if ( order != command):
                order = command
                arduinoHeader.FGo4()
        if command == "fgo5":
            if ( order != command):
                order = command
                arduinoHeader.FGo5()
        if command == "fgo6":
            if ( order != command):
                order = command
                arduinoHeader.FGo6()
        if command == "fgo7":
            if ( order != command):
                order = command
                arduinoHeader.FGo7()
        if command == "fgo8":
            if ( order != command):
                order = command
                arduinoHeader.FGo8()
        if command == "fgo9":
            if ( order != command):
                order = command
                arduinoHeader.FGo9()
        if command == "back1":
            if (order != command):
                order = command
                arduinoHeader.MBack1()
                if (mode == "mode1"):
                    cameraPub()
        if command == "back2":
            if (order != command):
                order = command
                arduinoHeader.MBack2()
        if command == "back3":
            if (order != command):
                order = command
                arduinoHeader.MBack3()
        if command == "back4":
            if (order != command):
                order = command
                arduinoHeader.MBack4()
        if command == "back5":
            if (order != command):
                order = command
                arduinoHeader.MBack5()
        if command == "back6":
            if (order != command):
                order = command
                arduinoHeader.MBack6()
        if command == "back7":
            if (order != command):
                order = command
                arduinoHeader.MBack7()
        if command == "back8":
            if (order != command):
                order = command
                arduinoHeader.MBack8()
        if command == "back9":
            if (order != command):
                order = command
                arduinoHeader.MBack9()
        if command == "fback1":
            if (order != command):
                order = command
                arduinoHeader.FBack1()
                if (mode == "mode1"):
                    cameraPub()
        if command == "fback2":
            if (order != command):
                order = command
                arduinoHeader.FBack2()
        if command == "fback3":
            if (order != command):
                order = command
                arduinoHeader.FBack3()
        if command == "fback4":
            if (order != command):
                order = command
                arduinoHeader.FBack4()
                if (mode == "mode1"):
                    cameraPub()
        if command == "fback5":
            if (order != command):
                order = command
                arduinoHeader.FBack5()
        if command == "fback6":
            if (order != command):
                order = command
                arduinoHeader.FBack6()
        if command == "fback7":
            if (order != command):
                order = command
                arduinoHeader.FBack7()
                if (mode == "mode1"):
                    cameraPub()
        if command == "fback8":
            if (order != command):
                order = command
                arduinoHeader.FBack8()
        if command == "fback9":
            if (order != command):
                order = command
                arduinoHeader.FBack9()
        if command == "left1":
            if (order != command):
                order = command
                arduinoHeader.MLeft1()
            if (mode == "mode1"):
                cameraPub()
        if command == "left2":
            if (order != command):
                order = command
                arduinoHeader.MLeft2()
        if command == "left3":
            if (order != command):
                order = command
                arduinoHeader.MLeft3()
        if command == "left4":
            if (order != command):
                order = command
                arduinoHeader.MLeft4()
        if command == "left5":
            if (order != command):
                order = command
                arduinoHeader.MLeft5()
        if command == "left6":
            if (order != command):
                order = command
                arduinoHeader.MLeft6()
        if command == "left7":
            if (order != command):
                order = command
                arduinoHeader.MLeft7()
        if command == "left8":
            if (order != command):
                order = command
                arduinoHeader.MLeft8()
        if command == "left9":
            if (order != command):
                order = command
                arduinoHeader.MLeft9()
        if command == "right1":
            if (order != command):
                order = command
                arduinoHeader.MRight1()
            if (mode == "mode1"):
                cameraPub()
        if command == "right2":
            if (order != command):
                order = command
                arduinoHeader.MRight2()
        if command == "right3":
            if (order != command):
                order = command
                arduinoHeader.MRight3()
        if command == "right4":
            if (order != command):
                order = command
                arduinoHeader.MRight4()
        if command == "right5":
            if (order != command):
                order = command
                arduinoHeader.MRight5()
        if command == "right6":
            if (order != command):
                order = command
                arduinoHeader.MRight6()
                if (mode == "mode1"):
                    cameraPub()
        if command == "right7":
            if (order != command):
                order = command
                arduinoHeader.MRight7()
        if command == "right8":
            if (order != command):
                order = command
                arduinoHeader.MRight8()
        if command == "right9":
            if (order != command):
                order = command
                arduinoHeader.MRight9()
        if command == "stop1":
            if (order != command):
                order = command
                arduinoHeader.MStop()
        if command == "fstop":
            if (order != command):
                order = command
                arduinoHeader.FStop()

        if command == "rightspin1":
            if (order != command):
                order = command
                arduinoHeader.MRightSpin1()
                if (mode == "mode1"):
                    cameraPub()
        if command == "rightspin2":
            if (order != command):
                order = command
                arduinoHeader.MRightSpin2()
                if (mode == "mode1"):
                    cameraPub()
        if command == "rightspin3":
            if (order != command):
                order = command
                arduinoHeader.MRightSpin3()
                if (mode == "mode1"):
                    cameraPub()
        if command == "leftspin1":
            if (order != command):
                order = command
                arduinoHeader.MLeftSpin1()
                if (mode == "mode1"):
                    cameraPub()
        if command == "leftspin2":
            if (order != command):
                order = command
                arduinoHeader.MLeftSpin2()
                if (mode == "mode1"):
                    cameraPub()
        if command == "leftspin3":
            if (order != command):
                order = command
                arduinoHeader.MLeftSpin3()
                if (mode == "mode1"):
                    cameraPub()
    elif (msg.topic == "mode"):
        mode = msg.payload.decode("utf-8")
        if mode == "mode2": # All Stop
            arduinoHeader.MStop()
            arduinoHeader.FStop()



def on_connect(client, userdata, msg, rc):
    client.subscribe("drive", qos=0)
    client.subscribe("mode", qos=0)
    cameraPub()
    print("Connect Success")
    pass

def cameraPub():
    imgData = camera.takePicture()
    """imgBytes = io.BytesIO(imgData)
    img = Image.open(imgBytes)
    fname = './data/1.jpg'
    img.save(fname)
    print(fname)"""
    imgData = bytes(imgData)
    client.publish("image", imgData, qos=0)
    print("Camera Published")
    pass


client = mqtt.Client()
#ip = input("broker ip >> ")
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883)
client.loop_forever()
