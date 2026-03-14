# IoT Health Outpatient Monitoring System

## Overview
This project is an IoT-based health outpatient monitoring system. It monitors patient activity in real-time using multiple sensors connected to a Raspberry Pi. The system sends data to the cloud (Google Sheets) and displays it on a mobile dashboard with alerts.

## Features
- Real-time monitoring of patients
- Touch, motion, distance, and sound sensors
- Cloud data logging via Google Sheets
- Alerts for abnormal patient behavior
- Mobile monitoring app built with MIT App Inventor

## Technologies Used
- Hardware: Raspberry Pi, Touch Sensor, Motion Sensor, Ultrasonic Sensor, Sound Sensor
- Software: Python, Google Sheets API, MIT App Inventor
- Cloud: Google Sheets (acts as lightweight database)

## Folder Structure
This is our iot project : health outpatient monitoring system


## Setup Instructions (Simulation)
1. Install Python 3 and `requests` library
2. Run `simulation/sensor_simulation.py` to simulate sensor data
3. Open Google Sheet to see live data
4. Open mobile app via MIT App Inventor companion to see dashboard

## Future Work
- Replace simulation with Raspberry Pi sensor input
- Add AI-based anomaly detection
- Create fully functional mobile app with notifications