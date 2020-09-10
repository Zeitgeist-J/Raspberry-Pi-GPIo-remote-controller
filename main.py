from flask import Flask, render_template, redirect, url_for
import time
import RPi.GPIO as g

g.setwarnings(0)
g.setmode(g.BCM)
g.setup(5, g.OUT)   #MotorA enable/disable (left)
g.setup(6, g.OUT)   #MotorB enable/disable (right)
g.setup(13, g.OUT)   #MotorA direction1   (left)
g.setup(19, g.OUT)   #MotorA direction2   (left)
g.setup(22, g.OUT)   #MotorB direction1   (right)
g.setup(27, g.OUT)   #MotorB direction2   (right)

g.setup(17, g.OUT)  #VCC
g.output(17, 1) #VCC ******************MUST BE REPLACED


app = Flask(__name__)

@app.route('/')
def index():
    g.output(5, 1) #enables motors, however no movement
    g.output(6, 1) #enables motors, however no movement
    g.output(13, 0) #(left)
    g.output(19, 0) #(left)
    g.output(22, 0) #(right)
    g.output(27, 0) #(right)
    return render_template('index.html')

@app.route('/stop', methods=['GET','POST'])
def stop():
    print('stop works!')
    g.output(5, 0) #disables motors
    g.output(6, 0) #disables motors
    time.sleep(1)
    return render_template('index.html')

@app.route('/forward', methods=['GET','POST'])
def forward():
    print('forward works!')
    g.output(5, 1)  #MotorA (left)
    g.output(6, 1)  #motorB (Right)
    g.output(13, 1) # (left)
    g.output(19, 0) # (left)
    g.output(22, 0) # (right)
    g.output(27, 1) # (right)
    time.sleep(1)
    return render_template('index.html')

@app.route('/backward', methods=['GET','POST'])
def backward():
    print('backward works!')
    g.output(5, 1)  #MotorA (left)
    g.output(6, 1)  #motorB (Right)
    g.output(13, 0) # (left)
    g.output(19, 1) # (left)
    g.output(22, 1) # (right)
    g.output(27, 0) # (right)
    time.sleep(1)
    return render_template('index.html')

@app.route('/left', methods=['GET','POST'])
def left():
    print('left works!')
    g.output(5, 1) #MotorA (left)
    g.output(6, 1) #motorB (Right)
    g.output(13, 1)
    g.output(19, 0)
    g.output(22, 1)
    g.output(27, 0)
    time.sleep(1)
    return render_template('index.html')

@app.route('/right', methods=['GET','POST'])
def right():
    print('right works!')
    g.output(5, 1) #MotorA (left)
    g.output(6, 1) #motorB (Right)
    g.output(17, 0)
    g.output(18, 1)
    g.output(6, 0)
    g.output(12, 1)
    time.sleep(1)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8013, host='0.0.0.0')