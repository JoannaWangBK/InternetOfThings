import numpy as np
import cv2
import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "mosquitto"
MQTT_TOPIC = "faces"

cap = cv2.VideoCapture(0)
print("Is cap opened:", cap.isOpened())

# create mqtt client for publishing
mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER, port=1883)


#create face detector
facealg = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#connect to camera
#cap = cv.VideoCapture(1)
num = 0
while(True):

    #read image in gray scale
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #cv2.imshow('frame', gray)
    
    #detect a face
    faces = facealg.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        print("New img")
        #cut the face from the frame
        roi_gray = gray[y:y+h, x:x+w]
    
        #encode and public message
        rc,png = cv2.imencode('.png', roi_gray)
        #cv2.imwrite('test_file'+str(num) + '.png', roi_gray)
        msg = png.tobytes()
        ret = mqttc.publish(MQTT_TOPIC, msg, qos=0, retain=False)
        print(ret)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
