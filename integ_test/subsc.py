#!/usr/bin/env python
import rospy

from control_msgs.msg import JointControllerState


def check_joint2(msg):
  if abs(msg.set_point-msg.process_value) < 0.01:
    print('joint is located right')
  else:
    print("wrong position")


def test():
  counter = 0
  rospy.init_node('image_listener')

  #topics for joints

  joint2_topic = '/MYROBOT/joint2_position_controller/state'

  #2 subscribers 

  rospy.Subscriber(joint2_topic,JointControllerState,check_joint2)


  rospy.spin()


if __name__ == '__main__':
  test()



