# import the necessary packages
import argparse
import imutils
import cv2

# construct an argument

# helps to run our program from the terminal

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# load the input image
image = cv2.imread(args["image"])
cv2.imshow("Image", image)

cv2.waitKey(0)

# convert the image to grayscale

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Edge Detection
# applying the Edge Detection we cab find the outlines of objects in image

edged = cv2.Canny(gray, 30, 150)
# using the popular Canny algorithm

cv2.imshow("Edged", edged)
cv2.waitKey(0)

# thresholding
# it helps us to remove lighter and darker regions and contour of images
# threshold the image by setting all pixel values less than 225

thresh = cv2.threshold(gray, 225, 225, cv2.THRESH_BINARY_INV)[1]
# Grabbing all pixels in the gray  image
# greater than 225 and setting them to 0 (black)
# which corresponds to the background of the image
cv2.imshow("Thresh", thresh)
# Setting pixel vales less than 225 to 255 (white)
# which corresponds to the foreground of the image
# (i.e., the Tetris blocks themselves).
cv2.waitKey(0)

# detecting and drawing contours

# it finds all foreground white pixels in the thresh.copy() image

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours = imutils.grab_contours(contours)
output = image.copy()

# loop over the contours
for c in contours:
    # draw each contour on the output image with a 3px thick purple
    # outline, then display the output contours one at a time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

# draw the total number of contours found in purple
# this builds a text string containing the number of steps
text = "I found {} objects!".format(len(contours))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)


# Erosion and Dilation
# used to reduce the noise in binary images

mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

# similarly, dilation can increase the size of the ground objects
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)


# masking and bitwise operations

# a typical operation we may want to apply is to take our mask
# and apply a bitwise AND to our input image , keeping the masked regions

mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Output", output)
cv2.waitKey(0)
