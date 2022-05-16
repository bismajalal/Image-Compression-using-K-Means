import random
import numpy as np
import cv2
import copy
import math

noOfClusters= 3           #number of clusters
mean = []                    #store k random means in it

image = cv2.imread('face2.bmp', -1)        # Load an image as it is
cv2.imshow('photo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
dimensions = image.shape  # get dimensions of image
height = image.shape[0]  # height, width, number of channels in image
width = image.shape[1]

print(image.shape)
TARGET=[]
TARGET=copy.deepcopy(np.asarray(image))    #convert the image to array for further processing

for i in range(noOfClusters):
    #initialize k means with random rgb values
    point = []
    point.append(random.randint(0, 255))
    point.append(random.randint(0, 255))
    point.append(random.randint(0, 255))
    mean.append(point)

print('mean 1',mean[0])
print('mean 2',mean[1])
print('mean 3',mean[2])

noOfIterations=0
stop=False

distance = 10000
meanX = 0
meanY = 0
meanZ = 0

while stop is False and noOfIterations < 50:

    PArray=[]
    for i in range(height):
        for j in range(width):

            distance = 10000
            for m in range(noOfClusters):
                d = np.linalg.norm(TARGET[i][j] - mean[m])
                if d < distance:                                                     #save the mean with the smallest distance from pixel
                    distance = d
                    index = m

            value = [[0] * noOfClusters]
            value[0][index] = 1  # 1 on the index of least distance mean
            print (value)
            PArray.append(value[0])

    newMean = []
    for m in range(noOfClusters):
        noOf1s=0
        sumX=0
        sumY=0
        sumZ=0

        for i in range(height):
             for j in range(width):                                                        #calculate the avg of all pixel RGB values which are closest to mth mean
                 sumX = sumX + TARGET[i][j][0] * PArray[(i * width) + j][m]
                 sumY = sumY + TARGET[i][j][1] * PArray[(i * width) + j][m]
                 sumZ = sumZ + TARGET[i][j][2] * PArray[(i * width) + j][m]

                 if PArray[( i * width) + j][m] == 1:
                     noOf1s=noOf1s+1

        if noOf1s > 0:
            meanX = int(sumX / noOf1s)                                    #store the avg of  all pixel RGB values which are closest to mth mean
            meanY = int(sumY / noOf1s)
            meanZ = int(sumZ / noOf1s)

        newMean.append([meanX,meanY,meanZ])

    print('\n\n', noOfIterations,' Iteration:')
    print('New Mean: ', newMean)
    print('Old Mean:',mean)

    diff=0
    flag = 0
    for i in range(noOfClusters):  # calculate the difference between old mean and new means
        diff = sum([(a - b) for a, b in zip(newMean[i], mean[i])])

        if (diff == 0):
            flag = flag + 1

        if (flag == noOfClusters):
            print("MATCHED")
            stop = True

    mean=newMean
    noOfIterations=noOfIterations+1

minDis = 0
meanIndex = 0
for i in range(height):
    for j in range(width):
        minDis = 10000

        for m in range(noOfClusters):
            d = np.linalg.norm(TARGET[i][j] - mean[m])

            if d < minDis:                                                     #save the mean with the smallest distance from pixel
                minDis = d
                meanIndex = m

        TARGET[i][j] = copy.deepcopy(mean[meanIndex])

cv2.imshow('photo', TARGET)
cv2.waitKey(0)



