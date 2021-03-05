import paho.mqtt.client as mqtt
import sys

#remote info
REMOTE_MQTT_HOST = "ec2-3-142-12-11.us-east-2.compute.amazonaws.com"
REMOTE_MQTT_PORT = 1883
REMOTE_MQTT_TOPIC = "faces"

#local info
LOCAL_MQTT_HOST = "mosquitto"
LOCAL_MQTT_PORT = 1883
LOCAL_MQTT_TOPIC = "faces"

r_conn = 0

#remote callback function
def on_publish_remote(client,userdata,result):
    print("data published to remote server \n")
    pass

#local callback function
def on_connect_local(client, userdata, flags, rc):
	print("connected to local broker with rc: " + str(rc))
	client.subscribe(LOCAL_MQTT_TOPIC)

def on_connect_remote(client, userdata, flags, rc):
    global r_conn
    print("connected to remote broker with rc: " +str(rc))
    r_conn = 1
def on_disconnect_remote(client, userdata, rc):
    global r_conn
    r_conn = 0
def on_message(client,userdata, msg):
  global r_conn
  try:
    print("message received!")
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    if r_conn == 0:
        remote_mqtt_client.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
        r_conn = 1
    remote_mqtt_client.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

    
#create local mqtt client
print("Local")
local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.on_message = on_message
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


#create remote mqtt client
print("Remote")
remote_mqtt_client = mqtt.Client()
remote_mqtt_client.on_connect = on_connect_remote
remote_mqtt_client.on_publish = on_publish_remote
remote_mqtt_client.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT)
remote_mqtt_client.publish(REMOTE_MQTT_TOPIC, "test remote connection")

# go into a loop
local_mqttclient.loop_forever()
