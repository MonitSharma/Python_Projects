## Measuring the Size of Objects with OpenCV

Measuring is similar to compute the distance from camera to an object.
We need to define the ratio that measures the number of pixels per given metric.

## The "Pixels per Metric" ratio
We need to perform calibration using reference object, there must be some properties that it must follow.

<li> Property #1: We should know the dimensions of the object in measurable unit </li> 
<li> Property #2 :We should be able to easily find the reference object in the image. Our reference should be uniquely identifiable</li>

In this example, we'll use the US quarter as the reference objet and will be placed in the left most object in the image

By guaranteeing the quarter is the left-most object, we can sort our object contours from left-to-right, grab the quarter (which will always be the first contour in the sorted list), and use it to define our pixels_per_metric, which we define as:

pixels_per_metric = object_width / know_width

A US quarter has a known_width of 0.955 inches. Now, suppose that our object_width (measured in pixels) is computed be 150 pixels wide (based on its associated bounding box).

The pixels_per_metric is therefore:

pixels_per_metric = 150px / 0.955in = 157px

Thus implying there are approximately 157 pixels per every 0.955 inches in our image. Using this ratio, we can compute the size of objects in an image.