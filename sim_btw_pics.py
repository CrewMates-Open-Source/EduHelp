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
imageA=cv2.imread("class.png")
imageB=cv2.imread("black.png")

#calling the function to display the similarities
image_comparison(imageA,imageA)
image_comparison(imageA,imageB)
