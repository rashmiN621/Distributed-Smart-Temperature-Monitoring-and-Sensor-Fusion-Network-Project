import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime

BROKER = "localhost"
PORT = 1883
TOPIC = "ee2120/groupproject/node1"
CSV_FILE = "sensor_data_log.csv"

def on_connect(client, userdata, flags, rc):
    print(f"[CONNECTED] Connected to MQTT Broker with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        node_id = data.get("node_id", "N/A")
        lm35 = data.get("lm35_temp", 0.0)
        ds18b20 = data.get("ds18b20_temp", 0.0)
        
        print(f"[{timestamp}] Recv -> Node: {node_id} | LM35: {lm35}°C | DS18B20: {ds18b20}°C")
        
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, node_id, lm35, ds18b20])
            
    except Exception as e:
        print("Error parsing payload:", e)

# Header එක එක පාරක් ලියන්න
try:
    with open(CSV_FILE, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Node_ID", "LM35_Temp", "DS18B20_Temp"])
except FileExistsError:
    pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
