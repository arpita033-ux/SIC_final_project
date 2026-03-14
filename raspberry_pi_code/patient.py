import gspread
from oauth2client.service_account import ServiceAccountCredentials
import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify
import threading
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
'credentials.json', scope)

client = gspread.authorize(creds)

sheet = client.open("RemoteHealthMonitor").sheet1

TRIG = 23
ECHO = 24
TOUCH = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TOUCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

patients_waiting = 0
wait_time = 0
motion_status = "Empty"

queue_history = []

person_detected = False
last_touch_state = 0

app = Flask(__name__)


def get_distance():

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    distance = (stop - start) * 34300 / 2
    return distance
@app.route('/')
def dashboard():

    return """
<html>

<head>

<title>Remote Health Outpost Monitor</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>

body{
font-family:Arial;
background:linear-gradient(135deg,#141E30,#243B55);
color:white;
text-align:center;
}

h1{
margin-top:20px;
font-size:36px;
}

.container{
display:flex;
justify-content:center;
flex-wrap:wrap;
margin-top:20px;
}

.card{
background:white;
color:black;
padding:25px;
margin:15px;
border-radius:15px;
width:240px;
box-shadow:0 10px 25px rgba(0,0,0,0.4);
}

.value{
font-size:36px;
font-weight:bold;
margin-top:10px;
}

.status-low{
color:green;
font-weight:bold;
}

.status-medium{
color:orange;
font-weight:bold;
}

.status-high{
color:red;
font-weight:bold;
}

.graph-container{
width:90%;
max-width:950px;
margin:40px auto;
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 10px 30px rgba(0,0,0,0.4);
}

canvas{
width:100% !important;
height:420px !important;
}

</style>

</head>

<body>

<h1>🏥 Remote Health Outpost Monitor</h1>

<div class="container">

<div class="card">
<h3>👥 Patients Waiting</h3>
<p id="patients" class="value">0</p>
</div>

<div class="card">
<h3>⏱ Estimated Wait Time</h3>
<p id="wait" class="value">0</p>
</div>

<div class="card">
<h3>🪑 Waiting Area</h3>
<p id="status" class="value">Empty</p>
</div>

<div class="card">
<h3>🚦 Queue Load</h3>
<p id="queue_status" class="value">Low</p>
</div>

</div>

<div class="graph-container">

<h2>📈 Queue Trend</h2>

<canvas id="chart"></canvas>

</div>

<script>

let ctx=document.getElementById('chart').getContext('2d');

let chart=new Chart(ctx,{
type:'line',
data:{
labels:[],
datasets:[{
label:'Patients Waiting',
data:[],
borderColor:'#00FFFF',
backgroundColor:'rgba(0,255,255,0.2)',
fill:true,
tension:0.4,
borderWidth:3
}]
},
options:{
responsive:true,
scales:{
y:{
beginAtZero:true,
ticks:{stepSize:1,color:'black'}
},
x:{
ticks:{color:'black'}
}
}
}
});

function animateValue(id,value){

let element=document.getElementById(id);
let start=Number(element.innerText)||0;
let range=value-start;
let stepTime=20;

let current=start;

let timer=setInterval(function(){

current+=Math.sign(range);

element.innerText=current;

if(current==value){
clearInterval(timer);
}

},stepTime);

}

function updateData(){

fetch('/data')
.then(response=>response.json())
.then(data=>{

animateValue("patients",data.patients);
animateValue("wait",data.wait_time);

document.getElementById("status").innerText=data.status;

let queueStatus="Low";
let colorClass="status-low";

if(data.patients>=3 && data.patients<=5){
queueStatus="Moderate";
colorClass="status-medium";
}

if(data.patients>=6){
queueStatus="Crowded";
colorClass="status-high";
}

let q=document.getElementById("queue_status");
q.innerText=queueStatus;
q.className="value "+colorClass;

chart.data.labels.push("");
chart.data.datasets[0].data.push(data.patients);

if(chart.data.labels.length>25){
chart.data.labels.shift();
chart.data.datasets[0].data.shift();
}

chart.update();

});

}

setInterval(updateData,2000);

</script>

</body>

</html>
"""

@app.route('/data')
def data():
    return jsonify({
        "patients": patients_waiting,
        "wait_time": wait_time,
        "status": motion_status
    })


def sensor_loop():

    global patients_waiting
    global wait_time
    global motion_status
    global person_detected
    global last_touch_state

    ignore_ultrasonic_until = 0

    while True:

        distance = get_distance()
        touch = GPIO.input(TOUCH)

        current_time = time.time()

        if current_time > ignore_ultrasonic_until:

            if distance < 60 and not person_detected:
                patients_waiting += 1
                person_detected = True

            if distance > 120:
                person_detected = False


        if touch == 1 and last_touch_state == 0:

            if patients_waiting > 0:
                patients_waiting -= 1

            ignore_ultrasonic_until = time.time()+2


        last_touch_state = touch


        if patients_waiting>0:
            motion_status="Occupied"
        else:
            motion_status="Empty"


        wait_time=patients_waiting*3
        sheet.append_row([
        patients_waiting,
        wait_time,
        motion_status
        ])

        time.sleep(5)


threading.Thread(target=sensor_loop).start()

app.run(host="0.0.0.0",port=5000)
