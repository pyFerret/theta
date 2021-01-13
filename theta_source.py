import vex
import sys

# stuff so my text editor doesn't want to kill me; ignore this
#class Loader():
#    def run(h):
#        pass
#    pass
#loader = Loader()

#region config
testb       = vex.LimitSwitch(1)
loader      = vex.Motor(2)
motor_right = vex.Motor(3)
motor_left  = vex.Motor(4)
tube_servo  = vex.Servo(5)
joystick    = vex.Joystick()
#endregion config

def move_motors():
  if joystick.
  loader.run(100)
  sys.wait_for(lambda: not testb.is_on())
  loader.off()

def drop_ball():
  tube_servo.position(50)
  sys.sleep(0.1)
  tube_servo.position(15)

def theta_move():
  if joystick.axis3() > 5:
    motor_left.run((joystick.axis3()))
    motor_right.run((joystick.axis3()))
    sys.wait_for(lambda: joystick.axis3() < 5)
    motor_right.off()
    motor_left.off()
  elif joystick.axis3() < -5:
    motor_left.run(-((joystick.axis3())))
    motor_right.run(-((joystick.axis3())))
    sys.wait_for(lambda: joystick.axis3() > -5)
    motor_right.off()
    motor_left.off()

def forward():
  motor_left.run(100)
  motor_right.run(100)
  sys.wait_for(lambda: not testb.is_on())
  motor_right.off()
  motor_left.off()

def turn_right():
  motor_left.run(100)
  motor_right.run(-(100))
  sys.wait_for(lambda: not testb.is_on())
  motor_right.off()
  motor_left.off()

def turn_left():
  motor_left.run(-(100))
  motor_right.run(100)
  sys.wait_for(lambda: not testb.is_on())
  motor_right.off()
  motor_left.off()

def backward():
  motor_left.run(-(100))
  motor_right.run(-(100))
  sys.wait_for(lambda: not testb.is_on())
  motor_right.off()
  motor_left.off()


# main thread
while True:
  theta_move()
