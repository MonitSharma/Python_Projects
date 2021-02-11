## Histogram Equalization
Histogram Equalization is a basic image processing technique that adjust the global contrast of an image by updating the image histogram's pixel intensity distribution .

#### How does the Equalization works?
<li> Computing a histogram of image pixel intensities</li>
<li> Evenly spreading out and distributing the most frequent pixel values</li>
<li> Giving a linear trend to the cumulative distribution function</li>

The result will let the image with higher global contrast.

##### We can improve this by using Contrast Limited Adaptive Histogram Equalization (CLAHE)


Other than photographers using histogram equalization to correct under/over-exposed images, the most widely used histogram equalization application can be found in the medical field.

### OpenCV Histogram Equalization and Adaptive Histogram Equalization (CLAHE)
We’ll then implement two Python scripts:

<li>simple_equalization.py: Performs basic histogram equalization using OpenCV’s cv2.equalizeHist function.
<li>adaptive_equalization.py: Uses OpenCV’s cv2.createCLAHE method to perform adaptive histogram equalization.



### Histogram matching with OpenCV, scikit-image, and Python
<li> Load an input image (i.e., “source” image)
<li>Load a reference image
<li>Compute histograms for both images
<li>Take the input image and match it to the reference image, thereby transferring the color/intensity distribution from the reference image into the source image</li>