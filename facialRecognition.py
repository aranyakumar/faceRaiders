import cv2
import sys
import math

# Get user supplied values
imagePath = "mother.jpg"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))
cv2.imshow("Faces found", image)

cv2.waitKey(0)

# Draw a rectangle around the faces
(x, y, w, h) = faces[0]
p = .5
x = math.floor((1-p)*x)
y = math.floor((1-p)*y)
w = math.floor((1+2*p)*w)
h = math.floor((1+2*p)*h)
image = image[y:y+h, x:x+w]
cv2.imshow("Faces found", image)

cv2.waitKey(0)

#blur gaussian
gaus = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("blur", gaus)
cv2.waitKey(0)

#blur bilateral
bilat = cv2.bilateralFilter(image,9,75,75)
cv2.imshow("bilat", bilat) 
cv2.waitKey(0)