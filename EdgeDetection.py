import os
import cv2
import numpy as np
from skimage import img_as_ubyte

def Canny(imgName):
     # Read the original image
    img = cv2.imread(imgName)
    gaussianBlur = 7
    thr1 = 100
    thr2 = 150

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    # 3*3, 5*5
    img_blur = cv2.GaussianBlur(img_gray, (gaussianBlur,gaussianBlur), 0) 

    # 100, 150
    # 100, 200
    # 100, 300
    # 50, 200
    edges = cv2.Canny(image=img_blur, threshold1=thr1, threshold2=thr2) # Canny Edge Detection
    # Display Canny Edge Detection Image
    print(edges)

    
    # groupX = 10
    # groupY = 8
    # edgeCount=[]
    # for i in range(int(len(edges)/groupY)):
    #     edgeCount.append([])
    #     for j in range(int(len(edges[i])/groupX)):
    #         count=0
    #         zeroCount = 0
    #         nonZeroCount = 0
    #         for ii in range(groupY):
    #             for jj in range(groupX):
    #                 if(edges[(i*groupY)+ii][(j*groupX)+jj] > 0):
    #                     count += edges[(i*groupY)+ii][(j*groupX)+jj]
    #                     nonZeroCount = nonZeroCount+1
    #                 else:
    #                     zeroCount = zeroCount+1
                    
    #         # if(count>0):
    #         #     count=255
    #         if(zeroCount > 3*nonZeroCount):
    #             count = 0
    #         else:
    #             count = 255
    #         # edgeCount[i].append(int(count/(groupX*groupY)))
    #         edgeCount[i].append(int(count))
    #         # if(edges[i][j]+e > 0):
    #         #     count = count + 1

    # cv2.imwrite('myImage.jpg', np.array(edgeCount))
    # print(edgeCount)

    print('Original: ', img.shape)
    print('Original: ', edges.shape)
    # print('Collapsed:', edgeCount.shape)

    final = cv2.merge([edges, edges, edges])    

    combined = cv2.hconcat([img, final])

    fileName = os.path.basename(imgName).split('/')[-1]

    path = "Canny\{}_{}_{}".format(gaussianBlur, thr1, thr2)
    if not os.path.exists(path):
        os.mkdir(path)

    p1 = os.path.join(path, 'Combined.' + fileName)
    p2 = os.path.join(path, fileName)

    cv2.imwrite(p1, combined)
    cv2.imwrite(p2, final)
    print('Saved: ', p1)

    return

def Sobel(imgName):
    # Read the original image
    img = cv2.imread(imgName)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    #Sobel Edge Detection
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
 
    cv2.imwrite('Sobel.' + imgName, sobelxy)

    return
 
# Canny Edge Detection 
images = [
    'SimpleImages\House.jpg',
    'FamousPaintings\Starry_Night.jpg',
    'SimpleImages\Parrot.jpg',
    'SimpleImages\House2.jpg',
    'SimpleImages\StarryNight_simplified.jpg',
]
for img in images:
    Canny(img)
# Canny('SimpleImages\House.jpg')
# Canny('FamousPaintings\The_Scream.jpg')
 
cv2.destroyAllWindows()