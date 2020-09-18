# Installing OpenCV
Run `pip install opencv-python` in your terminal.

# Using OpenCV in a Python Script
To use OpenCV, you will have to import it using `import cv2 as cv`. Then to use a function from OpenCV you use `cv.function()` The `as cv` part in the import statement is used to assign a different name to the module. Instead of having to write `cv2` every time we want to use OpenCV, we can just use `cv`.

# Useful Functions for Testing
## Reading an image from a file
Use `cv.imread("filename.png")` to load an image from a file. This will return an image object that OpenCV can manipulate.

## Writing an image to a file
Use `cv.imwrite("filename.png", image)` to write the `image` object to a file.

## Displaying an image
This opens a popup window to display `image`:
`cv.imshow(window_name, image)`
`window_name` is a string for the title of the window that will pop up.

Whenever you use `imshow`, you must also call `cv.waitKey(0)` after it. This will halt the execution of your python script until you press a key so that you can view the image. Otherwise, once it reaches the end of your script, it will exit and close all the windows.

## Example of reading an image file and displaying it
```python
import cv2 as cv

image = cv.imread("file.png")
cv.imshow("Image", image)
cv.waitKey(0)
```
# Face Detection
[This website](https://realpython.com/face-recognition-with-python/) has a good tutorial for face detection with OpenCV. There is a link to a Github with an example script. There is a file in the Github called `haarcascade_frontalface_default.xml` which contains the model for face detections that we can use.

This will return a list of rectangle coordinates where there are faces in an image. Notice in the examples that the rectangles do not fully encompass a person's head, so you may want to modify these coordinates so the whole head is inside.

# Background Removal
For the sake of simplicity, we will only focus on removing a solid color background.
## Color Spaces
When you load an image with OpenCV, it will be in the BGR color space. This means each pixel is defined by 3 numbers called channels, the first one for blue, then green, then red. This is backwards from RGB.

When trying to extract a certain color from an image, it may be better to use a different color space, such as HLS (Hue, Light, Saturation) or HSV (Hue, Saturation, Value).

To convert between color spaces use the `cvtColor` method.
`image = cv.cvtColor(src, cv.COLOR_BGR2HSV)`
`src` is the original image
`image` is the converted image
`cv.COLOR_BGR2HSV` tells which color spaces you are converting between. You can replace `HSV` with `HLS`.

## Masking
A mask is used to define which areas of an image you want to keep and which areas to throw away. We can create a mask based on color using the `inRange` method.

`mask = cv.inRange(src, lower, upper)`
`src` is the original image
`lower` and `upper` are the lower and upper bounds for the pixel values. They are a tuple of integers corresponding to each of the channels in the color space. For example, `(100, 100, 100)`.

You can use `imshow` on the mask for testing purposes.  Note that `inRange` includes only the pixels within the range. Since we want to exclude a color, we will want to invert the mask. This can be accomplished with `cv.bitwise_not(mask)` which will return the inverse of the mask.

## Getting the Mask Range
Since we do not know what color the background will be we have to find it somehow. One way you could do this is get user input by clicking on the area of the picture that is background. [This](https://docs.opencv.org/3.1.0/db/d5b/tutorial_py_mouse_handling.html) demonstrates how you can handle a mouse click on a picture. Another approach you could try is blob detection. [Here](https://www.learnopencv.com/blob-detection-using-opencv-python-c/) is a tutorial on blob detection in OpenCV.
