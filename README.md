AS 1 FRP
Modeling the robot Manipulator

Description:
In this project I model the Manipulator, which I invented by myself. Modeling robot is a useful project for me because I am interested in how different manipulators work and how to control them.

Aims:
- Figuring out how to work in Ros, Rviz, Gazebo
- Figuring out how to write Urdf file
- Learning how to model robots

In order to launch my robot Manipulator:
- Open the terminal
- Print "cd"your workspace"/src/
- Print "git clone https://github.com/AleksandrSidorin/Gazedo1"
- Print "catkin_make"
- Print "roslaunch gazebo1 gazebo.launch"

![Robot](https://user-images.githubusercontent.com/55827366/66889063-ab305280-efe9-11e9-8aff-1f2af79dfd3a.png)

AS 2 FRP
Creating robot movements

Description:
In this task I continue to work with my Manipulator. 

Aims:
- Make all appropriate joints to move
- Create a Python script that moves joints
- Make video how they are moving

In order to launch and move my robot Manipulator:
- Open the terminal
- Print "cd"your workspace"/src/
- Print "git clone https://github.com/AleksandrSidorin/Gazedo1"
- Print "catkin_make"
- Print "roslaunch gazebo1 gazebo.launch"
You should see the Robot in Gazebo, next steps:
- Open the new terminal
- Print "cd"your workspace"/src/
- Print "source devel/setup.bash"
- Print "rosrun gazebo1 scriptmove.py"

Now you see how Rpbot moves

Link to the video on YouTube:
https://youtu.be/Ck_fy_Z6fno

AS 3 FRP
Sensors

Description:
In this task I continue to work with my Manipulator. 

Aims:
- Add a camera sensor to one movable link
- Create a Python script that moves link with a camera
- Create a Python script that takes pictures
- Make video 

In order to launch my robot Manipulator and get pictures:
- Open the terminal
- Print "cd"your workspace"/src/
- Print "git clone https://github.com/AleksandrSidorin/Gazedo1"
- Print "catkin_make"
- Print "roslaunch gazebo1 gazebo.launch"
You should see the Robot in Gazebo, next steps:
- Open the new terminal
- Print "cd"your workspace"/src/
- Print "source devel/setup.bash"
- Print "rosrun gazebo1 scriptmovecamera.py"
Now link with the camera are movung, next steps:
- Open the new terminal
- Print "cd"your workspace"/src/
- Print "source devel/setup.bash"
- Print "rosrun gazebo1 scriptakepic.py"

Now we have pictures in folder "Pictures"

Link to the video on YouTube:
https://youtu.be/ghjpqJtXvy0

AS 4 FRP
Testing

Description:
In this task I continue to work with my Manipulator. 

Aims:
- Implement a function that makes useful calculations (FK)
- Implement unit - tests that validate FK
- Implement intagtation test
- Make video

In order to launch Unit test:
- Open the terminal
- Print "cd"your workspace"/src/
- Print "git clone https://github.com/AleksandrSidorin/Gazedo1"
- Print "catkin_make"
- Print "cd gazebo1/unit_test/"
- Print "python utest.py"
Now there is written OK (Test Done)
In order to launch Integ test:
- Open the new terminal
- Print "cd"your workspace"/src/
- Print "catkin make"
- Print "source devel/setup.bash"
- Print "roslaunch gazebo1 testik.launch "
Now there is written which links done test and which not

Link to the video on YouTube:
https://youtu.be/ghjpqJtXvy0


