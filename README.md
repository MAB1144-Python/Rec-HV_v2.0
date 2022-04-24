# installing-software
instalador 

## Publications
#### If you use this work in an academic context, please cite the following publication(s):
## Pre-requesites
1. ROS melodic or higher.
2. Python 3.6 or higher.
3. OpenNi2.
4. Virtualenv.
5. RPLIDAR.
## python libraries
1. OpenCV
2.  roslib
3.  rospy
4.  ros_numpy
5.  math
6.  numpy 
7.  time
8.  os
9.  statistics
10. open3d
11. struct
12. pandas
13. seaborn
14. sensor_msgs
15. datetime
16. Header

## Compile
1. Assuming you already have ROS related tools installed
```linux
$ sudo apt-get update
$ sudo apt-get install -y libqt4-dev qt4-dev-tools \ 
       libglew-dev glew-utils libgstreamer1.0-dev \ 
       libgstreamer-plugins-base1.0-dev libglib2.0-dev \
       libgstreamer-plugins-good
$ sudo apt-get install -y libopencv-calib3d-dev libopencv-dev 
```
2. Navigate to your catkin workspace and clone the repository:
```linux
$ cd ~/catkin_ws/src
$ git clone https://github.com/MAB1144-Python/rechv2.git
$ cd ..
$ catkin_make
```
3. Build the node:
#### Navigate to catkin workspace folder.
```linux
cd src
cd rechv2
cd launch
chmod +x Rec_HV.launch
chmod +x reconstruction.launch
chmod +x segmentation.launch
cd ..
cd src
chmod +x evaluation.py
chmod +x evaluation.pyc
chmod +x regression.py
chmod +x nodo_detection
chmod +x nodo_reconstruction
chmod +x nodo_segmentation
cd ..
cd ..
cd ..
```
## Run
```linux
cd ~/python36_ws
source py36env/bin/activate
cd
cd catkin_ws/src/rdslam/src
sudo chmod 666 /dev/ttyUSB0
____password____
roslaunch rechv2 Rec_HV.launch
```
