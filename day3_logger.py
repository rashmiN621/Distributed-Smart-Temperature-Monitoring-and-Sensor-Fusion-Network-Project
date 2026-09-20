import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime

BROKER = "localhost"
PORT = 1883
TOPIC = "ee2120/groupproject/node1"
CSV_FILE = "sensor_data_log.csv"

# Sensor Fusion Weights
W_LM35 = 0.3
W_DS18B20 = 0.7

# Simulated GPS Coordinates (UoP EEE Dept Location)
SIMULATED_LAT = 7.2543
SIMULATED_LON = 80.5917

def calculate_sensor_fusion(lm35, ds18b20):
    fused_temp = (W_LM35 * lm35) + (W_DS18B20 * ds18b20)
    return round(fused_temp, 2)

def on_connect(client, userdata, flags, rc):
    print(f"[CONNECTED] Connected to MQTT Broker with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        node_id = data.get("node_id", "node1")
        lm35 = float(data.get("lm35_temp", 0.0))
        ds18b20 = float(data.get("ds18b20_temp", 0.0))
        
        # GPS readings (if not provided in payload)
        lat = float(data.get("lat", SIMULATED_LAT))
        lon = float(data.get("lon", SIMULATED_LON))
        
        # Calculate Sensor Fusion
        fused_temp = calculate_sensor_fusion(lm35, ds18b20)
        
        print(f"[{timestamp}] Node: {node_id} | GPS: ({lat}, {lon}) | LM35: {lm35}°C | DS18B20: {ds18b20}°C | Fused: {fused_temp}°C")
        
        # Save to CSV including GPS Coordinates
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, node_id, lat, lon, lm35, ds18b20, fused_temp])
            
    except Exception as e:
        print("Error parsing payload:", e)

# Setup CSV Header with GPS fields
try:
    with open(CSV_FILE, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Node_ID", "Latitude", "Longitude", "LM35_Temp", "DS18B20_Temp", "Fused_Temp"])
except FileExistsError:
    pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
