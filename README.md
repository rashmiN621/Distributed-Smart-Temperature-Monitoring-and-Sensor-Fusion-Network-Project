# EE2120: IoT-Based Distributed Spatial Temperature Monitoring System

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Course](https://img.shields.io/badge/Course-EE2120_IoT-blue)
![University](https://img.shields.io/badge/University-Peradeniya-orange)

## 📌 Project Overview
This repository contains the full implementation of an end-to-end IoT system designed for real-time temperature data acquisition, multi-sensor fusion, GPS positioning, and spatial interpolation using Inverse Distance Weighting (IDW).

The system integrates ESP32 microcontrollers, MQTT protocol (Mosquitto), Node-RED dashboards, Python analytics scripts, and Git for version control.

---

## 🛠️ System Architecture & Workflow

[ ESP32 Nodes ] ---> (MQTT Broker: Mosquitto) ---> [ Node-RED Dashboard ]
(LM35 + DS18B20)         Topic: ee2120/groupproject/node1       |
                                                                v
[ Spatial Heatmap ] <--- [ IDW Spatial Script ] <--- [ Python CSV Logger ]

---

## 🚀 Key Features & Task Breakdown

### Day 1: System Setup & MQTT Broker
- Configured local Mosquitto MQTT Broker running on port 1883.
- Set up initial payload structure for publishing sensor data.
- Verified system communication via Node-RED MQTT nodes (day1_proof.png).

### Day 2: Sensor Characterization & Calibration
- Analyzed noise, drift, and response characteristics of LM35 (Analog) and DS18B20 (Digital) sensors.
- Calculated calibration offsets using linear regression analysis (day2_analysis.py).
- Generated noise and drift comparative plots (sensor_comparison_graphs.png).

### Day 3: Node-RED Dashboard & Automated Data Logging
- Designed an interactive Node-RED UI dashboard for real-time visualization (day3_dashboard.png).
- Developed day3_logger.py to automatically capture MQTT payloads and log timestamps, node IDs, and temperatures into sensor_data_log.csv.

### Day 4: Sensor Fusion & Spatial Interpolation
- Sensor Fusion: Implemented weighted average sensor fusion model (T_f = 0.3 * T_LM35 + 0.7 * T_DS18B20) to yield high-accuracy temperature estimates.
- GPS Data Integration: Embedded node geolocation coordinates (UoP EEE Dept: 7.2543, 80.5917) into the telemetry payload.
- Spatial Estimation: Developed day4_spatial_estimation.py using Inverse Distance Weighting (IDW) to estimate temperature across unmeasured coordinates and generate a spatial heat map (spatial_temperature_heatmap.png).

---

## 📂 Repository Structure

.
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore rules for OS/temp files
├── calibration_data.csv               # Raw calibration dataset (Day 2)
├── day1_proof.png                     # MQTT connection proof
├── day2_analysis.py                   # Sensor calibration & analysis script
├── day3_dashboard.png                 # Node-RED dashboard screenshot
├── day3_logger.py                     # Python MQTT subscriber & CSV logger
├── day4_spatial_estimation.py         # IDW spatial interpolation & heatmap generator
├── sensor_comparison_graphs.png       # Sensor noise/drift comparative plots
├── sensor_data_log.csv                # Real-time logged telemetry data with GPS & Fused Temp
└── spatial_temperature_heatmap.png    # Output spatial temperature heat map

---

## 🔧 How to Run the Project

### 1. Prerequisites
Ensure you have the following installed:
- Python 3.x
- Mosquitto MQTT Broker
- Node-RED

Install required Python dependencies:
pip install paho-mqtt matplotlib numpy seaborn

### 2. Running Data Logger (Sensor Fusion & Logging)
python day3_logger.py

### 3. Generating Spatial Heat Map
python day4_spatial_estimation.py

---

## 🎓 Course Details
* Course Code: EE2120 - Internet of Things (IoT)
* Institution: Department of Electrical & Electronic Engineering, University of Peradeniya