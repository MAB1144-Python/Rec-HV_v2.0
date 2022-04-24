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
6. OpenCV
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
