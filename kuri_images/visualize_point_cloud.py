#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Point cloud library
import pcl
import pcl.pcl_visualization
import cv2
import sys


def main():
    # These are track bar initial settings adjusted to the given pointcloud to make it completely visible.
    # Need to be adjusted depending on the pointcloud and its xyz limits if used with new pointclouds.
    # int a = 22;
    # int b = 12;
    # int c=  10;

    a = 22
    b = 12
    c = 10

    # PCL Visualizer to view the pointcloud
    # pcl::visualization::PCLVisualizer viewer ("Simple visualizing window");
    viewer = pcl.pcl_visualization.PCLVisualizering()
    cloud = pcl.load("depth_cloud/"+"image_"+sys.argv[1]+".pcd")
    cloud_filtered = cloud
    last_c = 0

    while last_c != 27:

        # pcl::copyPointCloud(*cloud_filtered, *cloud);
        # // i,j,k Need to be adjusted depending on the pointcloud and its xyz limits if used with new pointclouds.
        i = 0.1 * a
        j = 0.1 * b
        k = 0.1 * c

        print("i = " + str(i) + " j = " + str(j) + " k = " + str(k))
        pass_th = cloud.make_passthrough_filter()
        pass_th.set_filter_field_name("y")
        pass_th.set_filter_limits(-k, k)
        cloud = pass_th.filter()

        pass_th.set_filter_field_name("x")
        pass_th.set_filter_limits(-j, j)
        cloud = pass_th.filter()
        pass_th.set_filter_field_name("z")
        pass_th.set_filter_limits(-10, 10)
        cloud = pass_th.filter()

        viewer.AddPointCloud(cloud, b'scene_cloud', 0)
        viewer.SpinOnce()
        viewer.RemovePointCloud(b'scene_cloud', 0)
        viewer.AddCoordinateSystem()

if __name__ == "__main__":
    main()

