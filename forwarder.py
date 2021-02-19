import paho.mqtt.client as mqtt

#remote info
REMOTE_MQTT_HOST = "52.117.207.78"
REMOTE_MQTT_PORT = 1883
REMOTE_MQTT_TOPIC = "facedetector_topic_remote"

#remote callback function
def on_publish_remote(client,userdata,result):
    print("data published to remote server \n")
    pass

#create remote mqtt client
remote_mqtt_client = mqtt.Client()
remote_mqtt_client.on_publish = on_publish_remote
#Wait for AWS broker
#remote_mqtt_client.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT)
#remote_mqtt_client.publish(REMOTE_MQTT_TOPIC, "test remote connection")

#local info
LOCAL_MQTT_HOST = "mosquitto"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "facedetector_topic"

#local callback function
def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)


def on_message(client,userdata, msg):
 # try:
 #   remote_mqtt_client.publish(REMOTE_MQTT_TOPIC, payload=msg.payload, qos=0, retain=False)
 # except:
 #   print("Unexpected error:", sys.exc_info()[0])
    print("Got msg")
    
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
