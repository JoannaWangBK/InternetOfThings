import numpy as np
import cv2
import paho.mqtt.client as mqtt
import math
LOCAL_MQTT_HOST="mosquitto"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"
image_number = 0

def on_connect(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
def on_message(client, userdata, msg):
    global image_number
    msg = np.frombuffer(msg.payload, dtype='uint8')
    img = cv2.imdecode(msg, flags=1)
    print(img.shape)
    img_name = "face-" + str(image_number) + ".png"
    print(f"{img_name}")
    image_number += 1
    cv2.imwrite('/mnt/mountpoint/'+img_name, img)
    print("got msg")

mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
mqttclient.loop_forever()
