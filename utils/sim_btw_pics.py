#here, we use structural similarity for comparing between two images
from skimage.metrics import structural_similarity as ssim
#importing cv2
import cv2

#function for calculating and displaying the percentage similarity between two images
def image_comparison(imageA,imageB):
	value_of_similarity=ssim(imageA,imageB,multichannel=True)
			#multichannel is kept as true as the images are colored
	print(value_of_similarity*100)

#reading the two different images
imageA=cv2.imread("")
imageB=cv2.imread("")

#checking for the picture of comparatively small diamensions
(h1,w1,c1)=imageA.shape[0],imageA.shape[1],imageA.shape[2]
(h2,w2,c2)=imageB.shape[0],imageA.shape[1],imageB.shape[2]
print(h1,w1,c1)
print(h2,w2,c2)
if (h1,w1)<(h2,w2):
	imageB=cv2.resize(imageB,(w1,h1))
else:
	imageA=cv2.resize(imageA,(w2,h2))  
print(imageA.shape[0],imageA.shape[1])
	

#calling the function to display the similarities
image_comparison(imageA,imageA)
image_comparison(imageA,imageB)
