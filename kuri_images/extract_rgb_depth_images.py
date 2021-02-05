#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import os,sys  
from cv_bridge import CvBridge, CvBridgeError
import cv2
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2
import pcl
#visualization
import pcl.pcl_visualization
import numpy as np


bridge = CvBridge()
current_cloud = None
counter = 0
def image_callback(msg):
	global counter, cloud
	print("Image Received")
	try:
		cv2_img=bridge.imgmsg_to_cv2(msg,"bgr8")
	except CvBridgeError as e:
		print(e)
	else:
		cv2.imwrite("sub_images/"+'image_'+str(counter)+'.jpeg', cv2_img)
		gen = pc2.read_points(current_cloud, field_names="x,y,z")
		pc_list=list(gen)
		pcl_object=pcl.PointCloud()
		pcl_object.from_list(pc_list)
		cloud=pcl_object
		cloud.to_file("depth_cloud/image_"+str(counter)+".pcd")
		counter+=1	





def read_callback(msg):
	global current_cloud
	current_cloud = msg
	

if __name__ == '__main__':
	rospy.init_node('depth_image_listener')
	cloud_topic="/cloud"
	image_topic="/camera_image"
	rospy.Subscriber(image_topic,Image, image_callback)
	rospy.Subscriber(cloud_topic, PointCloud2, read_callback)
	rospy.spin()
