import numpy as np
import cv2
import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "broker"
MQTT_TOPIC = "faces"

# 1 should correspond to /dev/video1, the USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
print("Is cap opened:", cap.isOpened())

# create mqtt client for publishing
mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER, port=1883)


#create face detector
facealg = cv.CascadeClassifier("/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml")

#connect to camera
cap = cv.VideoCapture(1)

while(True):

    #read image in gray scale
    ret, frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)

    #detect a face
    faces = facealg.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        
        #cut the face from the frame
        roi_gray = gray[y:y+h, x:x+w]
    
        #encode and public message
        rc,png = cv.imencode('.png', roi_gray)
        msg = pickle.dumps(png)
        mqtt_client.publish(LOCAL_MQTT_TOPIC, msg, qos=0, retain=False)
    
    #quit capturing
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()