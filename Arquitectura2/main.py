from flask import Flask, render_template, redirect, url_for
import time
# import RPi.GPIO as GPIO

# GPIO.setwarnings(0)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(5, GPIO.OUT)   #MotorA enable/disable (left)
# GPIO.setup(6, GPIO.OUT)   #MotorB enable/disable (right)
# GPIO.setup(13, GPIO.OUT)   #MotorA direction1   (left)
# GPIO.setup(19, GPIO.OUT)   #MotorA direction2   (left)
# GPIO.setup(22, GPIO.OUT)   #MotorB direction1   (right)
# GPIO.setup(27, GPIO.OUT)   #MotorB direction2   (right)

# GPIO.setup(4, GPIO.OUT)  #GROUND
# GPIO.setup(17, GPIO.OUT)  #VCC
# GPIO.output(4, 0) #GROUND
# GPIO.output(17, 1) #VCC ******************MUST BE REPLACED

app = Flask(__name__)

@app.route('/')
def index():
    print('GPIO.output(5, 1) enables motors, however no movement')
    print('GPIO.output(6, 1) enables motors, however no movement')
    print('GPIO.output(13, 0) (left)')
    print('GPIO.output(19, 0) (left)')
    print('GPIO.output(22, 0) (right)')
    print('GPIO.output(27, 0) (right)')
    return render_template('index.html')

@app.route('/stop', methods=['GET','POST'])
def stop():
    print('stop works!')
    print('GPIO.output(5, 0) disables motors')
    print('GPIO.output(6, 0) disables motors')
    time.sleep(1)
    return render_template('index.html')

@app.route('/forward', methods=['GET','POST'])
def forward():
    print('forward works!')
    print('GPIO.output(5, 1) MotorA (left)')
    print('GPIO.output(6, 1) motorB (Right)')
    print('GPIO.output(13, 1) (left)')
    print('GPIO.output(19, 0) (left)')
    print('GPIO.output(22, 0) (right)')
    print('GPIO.output(27, 1) (right)')
    time.sleep(1)
    return render_template('index.html')

@app.route('/backward', methods=['GET','POST'])
def backward():
    print('backward works!')
    print('GPIO.output(5, 1) MotorA (left)')
    print('GPIO.output(6, 1) motorB (Right)')
    print('GPIO.output(13, 0) (left)')
    print('GPIO.output(19, 1) (left)')
    print('GPIO.output(22, 1) (right)')
    print('GPIO.output(27, 0) (right)')
    time.sleep(1)
    return render_template('index.html')

@app.route('/left', methods=['GET','POST'])
def left():
    print('left works!')
    print('GPIO.output(5, 1) MotorA (left)')
    print('GPIO.output(6, 1) motorB (Right)')
    print('GPIO.output(13, 1)')
    print('GPIO.output(19, 0)')
    print('GPIO.output(22, 1)')
    print('GPIO.output(27, 0)')
    time.sleep(1)
    return render_template('index.html')

@app.route('/right', methods=['GET','POST'])
def right():
    print('right works!')
    print('GPIO.output(5, 1) MotorA (left)')
    print('GPIO.output(6, 1) motorB (Right)')
    print('GPIO.output(17, 0)')
    print('GPIO.output(18, 1)')
    print('GPIO.output(6, 0)')
    print('GPIO.output(12, 1)')
    time.sleep(1)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8013, host='0.0.0.0')