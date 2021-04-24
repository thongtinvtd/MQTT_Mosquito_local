import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"  # 192.168.189.130
PORT = 1883
MQTT_USER = "thongtinvtd"
MQTT_PASS = "trung789"

TOPIC_0 = "dev/test0"
TOPIC_1 = "dev/test1"
TOPIC_2 = "dev/test2"
TOPIC_3 = "dev/test3"
TOPIC_4 = "dev/test4"
TOPIC_5 = "dev/test5"
TOPIC_6 = "dev/test6"
TOPIC_7 = "dev/test7"
TOPIC_8 = "dev/test8"
TOPIC_9 = "dev/test9"

Client = mqtt.Client('client1')
Client.username_pw_set(MQTT_USER,MQTT_PASS)

Client.connect(HOST,PORT)
Client.loop_start()

while(1):
    mess_1 = "test publish"
    str1 = TOPIC_1[:-1]

    for i in range(10):
        topic = ''.join([str1,str(i)])
        mess = ' '.join([mess_1,str(i)])
        Client.publish(topic,mess)
        print(topic+mess)
    time.sleep(1)
