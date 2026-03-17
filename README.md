# IoT-Based Remote Health Outpost Monitor for Outpatient Queue Management

![WhatsApp Image 2026-03-14 at 12 10 49 PM](https://github.com/user-attachments/assets/523cb539-17b1-4525-b31d-81b984beed00)


## Abstract
Healthcare centers in rural and remote areas often face challenges in managing outpatient queues efficiently due to limited staff and infrastructure.  

This project proposes an **IoT-based Remote Health Outpost Monitor** that helps track patient queue status and estimate waiting time in real time.  

The system uses an ultrasonic sensor to detect patient arrivals and a touch sensor to simulate the doctor calling the next patient. A Raspberry Pi processes sensor data and hosts a web-based dashboard that displays the number of patients waiting, estimated waiting time, waiting area status, and queue trends.  

Additionally, the system uploads real-time operational data to **Google Sheets** for cloud logging and analytics.  

This solution demonstrates how low-cost IoT systems can improve patient flow monitoring and healthcare facility management.

---

## Problem Statement
Outpatient healthcare facilities, especially in rural areas, often lack digital systems to monitor patient queues and waiting times. Staff manually track patients, which can lead to confusion, long waiting times, and inefficient service management.  

There is a need for a low-cost automated system that can monitor patient flow and provide real-time updates to healthcare staff.

---

## Objectives
- To design a low-cost IoT system to monitor outpatient waiting queues.
- To detect patient arrivals using sensors.
- To estimate waiting time dynamically based on queue length.
- To create a real-time web dashboard displaying patient flow information.
- To store operational data in the cloud for analysis using Google Sheets.
- To demonstrate the use of IoT technology in healthcare monitoring.

---

## Architecture
The system architecture consists of:

- **Ultrasonic Sensor (HC-SR04)** → Detects patient arrivals  
- **Touch Sensor** → Simulates doctor calling the next patient  
- **Raspberry Pi** → Central processing unit that reads sensors, calculates waiting time, and updates the dashboard  
- **Flask Web Dashboard** → Real-time display (hosted on Raspberry Pi)  
- **Google Sheets** → Cloud logging and analytics  

*(Add your Architecture Diagram image here – `architecture.png`)*

---

## Technologies Used

### Hardware
- Raspberry Pi
- Ultrasonic Sensor (HC-SR04)
- Touch Sensor
- Jumper Wires

### Software
- Python
- Flask (Web Dashboard)
- Chart.js (Graph Visualization)
- Google Sheets API
- gspread Python Library

### Tools
- Raspberry Pi OS
- Google Cloud Console
- GitHub (Version Control)

---

## Repository Structure
HEALTH-OUTPATIENT-MONITORING/
├── documentation/
│   └── Remote_Health_Outpost.pdf
├── raspberry_pi_code/
│   └── patient.py
├── architecture.jpeg
└── README.md


---

## Results / Output
The system successfully demonstrates:
- Real-time monitoring of outpatient queues
- Automatic waiting time estimation
- Live dashboard showing patient queue status
- Graph visualization of queue trends
- Cloud data logging using Google Sheets
![WhatsApp Image 2026-03-17 at 8 30 33 PM](https://github.com/user-attachments/assets/3061edc5-f866-4ac7-a9f8-067f487fb261)



---

## Challenges Faced
- Handling unstable ultrasonic sensor readings
- Preventing duplicate patient detection
- Integrating Google Sheets API with Raspberry Pi
- Designing a responsive real-time web dashboard
- Managing sensor timing and synchronization

---

## Future Improvements
- Camera-based patient detection using computer vision
- SMS or mobile alerts when queues become long
- Integration with hospital appointment systems
- Mobile application for remote monitoring
- AI-based prediction of patient waiting time
- Multi-room monitoring for larger healthcare facilities

---

## Setup & Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/health-monitor-project.git
   cd health-monitor-project

2.Install dependencies:
  bash:  pip install -r requirements.txt
 
3.Setup Google Sheets API:
Create a Service Account in Google Cloud Console
Download credentials.json and place it in the project root
Share your Google Sheet with the service account email

4.Run the system:
python patient.py

5.Open the dashboard: http://<raspberry-pi-ip>:5000











