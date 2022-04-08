# Road-Lane-Detection
A Computer Vision Project in Python

# Overview
Lane Line detection is a critical component for self driving cars and also for computer vision in general. This concept is used to describe the path for self-driving cars and to avoid the risk of getting in another lane.

In this project, we will build a machine learning project to detect lane lines in real-time. We will do this using the concepts of computer vision using OpenCV library. To detect the lane we have to detect the white markings on both sides on the lane.

# Block Diagram
![block diagram](https://user-images.githubusercontent.com/85211871/162394516-e296d4ae-441e-49f2-9612-01cd514e6024.png)

# Methodology
1.	Image Processing: To enhance the quality of image, we need to preprocess it. The processes like graying, noise reduction, edge detection, and contrast and color management are applied.
  ![image](https://user-images.githubusercontent.com/85211871/162394927-9298ac65-6b5f-4535-ab8c-4754a271e9ee.png)

2.  Region of Interest:
  ROI plays a significant role in detecting the computational complexity of lane identification and LDI systems. Only the selected regions are detected and forwarded to the next processing level. These ROI images are then employed in a suggested method for lane detection. The use of ROI shortens the time it takes for the frames to be processed.
  ![image](https://user-images.githubusercontent.com/85211871/162395034-2f4ec704-c34a-4d4c-b0d1-2245ea7af67c.png)

3.  Canny edge detection:
      Canny edge detection is a technique for extracting relevant structural information from various visual objects while reducing the amount of data to be processed considerably. It's been used in a variety of computer vision systems.
  ![image](https://user-images.githubusercontent.com/85211871/162395255-cc1843ad-2d87-4c89-8226-68f5f9242d41.png)

4.  Hough Transform:
A technique known as Hough Transform can be used to separate the features of various shapes within a picture. This method is commonly used to identify arbitrary forms such as straight lines, circles, ellipses, and so on. After the canny edges detection, the Hough Transform is applied to images in order to retrieve the image pixels that are wanted. The Hough Transform is utilized in this system to detect the coordinates of lane line from the image data.
