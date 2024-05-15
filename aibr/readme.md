# AI Based Robotics
## Init
Install ROS Melodic or a docker image with ROS Melodic.

## Install Warthog for simulation
### Installation
[Link](http://www.clearpathrobotics.com/assets/guides/melodic/ros/Drive%20a%20Warthog.html)
```
sudo apt-get update
sudo apt-get install ros-melodic-warthog-simulator
sudo apt-get install ros-melodic-warthog-desktop
sudo apt-get install ros-melodic-warthog-navigation
```
### Launch
```
roslaunch warthog_gazebo empty_world.launch
```

## Create Project

Make a workspace, 
```
mkdir -p aibr/src
```

Our workspace is now `aibr`

### Create Package 
If you're cloning the package, skip the steps below to the next section

cd `src`

and run
```
catkin_create_pkg -D "A package for AI based robotics research" -l "BSD" --author "Felix Sihitshuwam" --maintainer "Felix Sihitshuwam" aibr rospy roscpp std_msgs  geometry_msgs
```

Edit and set maintainer emails in package.xml

### Clone Package
cd into `src` and run

```
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```

```
cd .. && catkin_make --pkg aibr
```
or prefarably
```
cd .. && catkin build aibr
```
cd should be into the workspace, assuming that you were initially in `workspace/src`

## Creating Nodes
### Python
1. Create a scripts dir
2. Create a python file
3. Set it to executable `chmod +x [script.py]`
4. Build package.

### C++