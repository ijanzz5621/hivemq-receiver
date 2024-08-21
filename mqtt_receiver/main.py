import paho.mqtt.client as paho

def on_subscribe(self, client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client: paho.Client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print("Received message: " + str(msg.payload))
    
    print("Send file bytes to OSDU.")
    
    print("File successfully sent to OSDU.")
    # client.

def start() -> None:
    print("Start HiveMQ receiver. Receiving messages...")
    
    client = paho.Client(client_id="sharizan_redzuan_receiver", userdata=None, protocol=paho.MQTTv5)
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    
    client.will_set("encyclopedia/temperature", payload=None, qos=2, retain=False)
    
    client.connect("localhost", port=1883, keepalive=60, clean_start=0)
    client.subscribe("encyclopedia/temperature", qos=2)


    
    client.loop_forever()
    