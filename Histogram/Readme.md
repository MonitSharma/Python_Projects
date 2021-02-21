## Histogram Equalization
Histogram Equalization is the basic Image processing techniques that adjusts the global contrast of an Image by updating the Image histogram's pixel intensity distribution.

#### How does it work?
<li> Computing a histogram of Image pixel intensities</li>
<li> Evenly Spreading out the most frequent pixel values(the one with the largest counts in Histogram)</li>
<li> Give a Linear trend to the cumulative distribution function(CDF)</li>

After applying all this, what we'll get is an Image with higher global contrast, and
then we can further improve it by Contrast Limited Adaptive Histogram Equalization (CLAHE), results in even higher quality output images.


#### We'll then use two Python Scripts
<li> simple_equalization.py : Performs basic histogram equalization using the OpenCV library</li>
<li> adaptive_equalization.py : Using createCLAHE function</li>


We do have some limitations for the basic histogram equalization, a more computationally expensive , the adaptive equalization can yield better result.

#### adaptive_equalization.py
We take three arguments
<li> --image: The path to the input image, from your device</li>
<li> --clip: The threshold for contrast limiting, mostly leave in the range of 2-5, if the value is too big, then it'll maximise the local contrast </li>
<li> --tile: The tile grid size for CLAHE, here we are dividing the input image into tilt x tile cells, and then apply histogram equalization</li>



















