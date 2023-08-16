import cv2 as cv
import numpy as np
 

imageName = 'Starry_Night.jpg'

# read the image
image = cv.imread(imageName)

imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

final = np.zeros(image.shape, dtype = "uint8")

cv.drawContours(final, contours, -1, (128,128,128), 3)

print(image.shape)
print(final.shape)

c = cv.hconcat([final])

cv.imshow('im', c)

cv.imwrite('Contour.' + imageName, c)

# Waits for a keystroke
cv.waitKey(0)  
 
# Destroys all the windows created
cv.destroyAllWindows() 