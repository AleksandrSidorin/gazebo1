#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

def talker():
    
    rospy.init_node('talker', anonymous=True)

    pub1 = rospy.Publisher('/MYROBOT/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/MYROBOT/joint2_position_controller/command', Float64, queue_size=10)
    
    pub3 = rospy.Publisher('/MYROBOT/joint3_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('/MYROBOT/joint4_position_controller/command', Float64, queue_size=10)

    rate = rospy.Rate(40) # 20hz

    while not rospy.is_shutdown():
     
        position1 = 0.4
        position2 = 0.5
        position3 = -0.5
        position4 = 0.3

        #rospy.loginfo(position1)
        
        pub1.publish(position1)
        pub2.publish(position2)
        pub3.publish(position3)
        pub4.publish(position4)
 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass














