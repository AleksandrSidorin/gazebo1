#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    
    rospy.init_node('talker', anonymous=True)

    pub2 = rospy.Publisher('/MYROBOT/joint2_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(40) # 20hz

    while not rospy.is_shutdown():
     
        position2 = 1
       
        #rospy.loginfo(position1)
        
        pub2.publish(position2)
 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass














