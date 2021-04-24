import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"  # 192.168.189.130
PORT = 1883
TOPIC = "dev/test2"
MQTT_USER = "thongtinvtd"
MQTT_PASS = "trung789"

def on_connect(client,userdata,flags,rc):
    print("Connected!",str(rc))
    client.subscribe(TOPIC)

def on_message(client,userdata,message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic+' : ',message)


Client = mqtt.Client('client2')
Client.username_pw_set(MQTT_USER,MQTT_PASS)

Client.on_connect = on_connect
Client.on_message = on_message

Client.connect(HOST,PORT)

Client.loop_forever()
Client.disconnect()


# while(1):
#     print("\n")
#     time.sleep(1)