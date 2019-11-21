#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()


def image_callback(msg):
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError, e:
        print(e)
    else:
      global k
      if k < 7:
	filename = '/home/aleksandr/simulation_ws/src/gazebo1/Pictures/' + str(k) + '.png'
          # Save your OpenCV2 image as a jpeg 
        cv2.imwrite(filename, cv2_img)
        k = k + 1
        print("saved")
      else: 
        k = 1

def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/TAKEPIC/camera1/image_raw"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()
    # Spin until ctrl + c
    #rospy.spin()

#Main section of code that will continuously run unless rospy receives interuption (ie CTRL+C)
if __name__ == '__main__':
  k = 1
  main()





