# import the necessary packages
import argparse
import cv2

# constructing the argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type = str, required=True, help= "path to input image")
args = vars(ap.parse_args())

# loads the image and now the work
print("[INFO] loading input image....")
image = cv2.imread(args["image"])

# now gray scale it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
print("[INFO] performing the Histogram equalization ... ")
equalized = cv2.equalizeHist(gray)

# now show the output
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)