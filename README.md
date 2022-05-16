# Image-Compression-using-K-Means
Use K-means algorithm to reduce the color information (image compression) of an image.

Solution:
1.	Generate K random means
2.	Create a matrix, M, with rows = noOfSamples and cols = K. Fill all entries with zero.
3.	For each sample, find the mean that the sample is closest to. 
4.	M [sampleNo][mean] = 1  (which mean the sample is closest to)
5.	For each mean, add all the samples which are closest to that mean. Divide this sum with the count of those samples. We get a new mean.
6.	Do step 5 for all means to get K updated means
7.	Repeat steps 2-6 till all the means stop updating or till the noOfIterations reach a specific value.
8.	Change the value of each sample to the value of the mean it was closest to. The matrix M will be used for this. 
9.	The new image generated from this will be the compressed image.

Results:
The original image was the following:

![image](https://user-images.githubusercontent.com/54996440/168550869-aa62decd-0f22-408d-a200-7bc98dd8c206.png)

The compressed images, their respective number of clusters (k) and the number of iterations are shown in the table on the next page.

![image](https://user-images.githubusercontent.com/54996440/168550739-49728f13-9919-4977-9d63-fdfda0d8511a.png)




