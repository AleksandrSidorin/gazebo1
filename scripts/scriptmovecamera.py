#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math

def talker():
    
    rospy.init_node('talker', anonymous=True)

    pub1 = rospy.Publisher('/MYROBOT/joint2_position_controller/command', Float64, queue_size=10)
  
    rate = rospy.Rate(40) # 20hz
    i=0
    while not rospy.is_shutdown():
     
        position1 = math.sin(i/20.)*2.5
       
        #rospy.loginfo(position1)
        
        pub1.publish(position1)

        i=i+1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass










