import io
import numpy as np
import time
import paho.mqtt.client as mqtt
import math
import arduinoHeader2

def on_message(client, userdata, msg):
    command = msg.payload.decode("utf-8")
    print("receive " + command)
    
    if(msg.topic == "arm"):
        if command == "btn11": #왼쪽
            arduinoHeader2.arm_left()
        elif command == "btn12": #오른쪽
            arduinoHeader2.arm_right()
        elif command == "btn21":
            arduinoHeader2.arm1_up()
        elif command == "btn22":
            arduinoHeader2.arm1_down()
        elif command == "btn31":
            arduinoHeader2.arm2_up()
        elif command == "btn32":
            arduinoHeader2.arm2_down()
        elif command == "btn41":
            arduinoHeader2.gripper_up()
        elif command == "btn42":
            arduinoHeader2.gripper_down()
   
def on_connect(client, userdata, msg, rc):
    client.subscribe("arm", qos=0)
    client.subscribe("arm_mode", qos=0)
    print("Connect Success")
    pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883)
client.loop_forever()
