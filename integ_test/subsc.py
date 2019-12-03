#!/usr/bin/env python
import rospy

from control_msgs.msg import JointControllerState

def check_joint1(msg):
  if abs(msg.set_point-msg.process_value) < 0.01:
    print('joint 1 passed test')
  else:
    print("failed")


def check_joint2(msg):
  if abs(msg.set_point-msg.process_value) < 0.01:
    print('joint 2 passed test')
  else:
    print("failed")

def check_joint3(msg):
  if abs(msg.set_point-msg.process_value) < 0.01:
    print('joint 3 passed test')
  else:
    print("failed")

def check_joint4(msg):
  if abs(msg.set_point-msg.process_value) < 0.01:
    print('joint 4 passed test')
  else:
    print("failed")

def test():
  counter = 0
  rospy.init_node('image_listener')

  #topics for each leg

  joint1_topic = '/MYROBOT/joint1_position_controller/state'
  joint2_topic = '/MYROBOT/joint2_position_controller/state'
  joint3_topic = '/MYROBOT/joint3_position_controller/state'
  joint4_topic = '/MYROBOT/joint4_position_controller/state'

  #2 subscribers for 2 legs

  rospy.Subscriber(joint1_topic,JointControllerState,check_joint1)
  rospy.Subscriber(joint2_topic,JointControllerState,check_joint2)
  rospy.Subscriber(joint3_topic,JointControllerState,check_joint3)
  rospy.Subscriber(joint4_topic,JointControllerState,check_joint4)


  rospy.spin()


if __name__ == '__main__':
  test()



