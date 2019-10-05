import cv2
import numpy as np 
from PIL import ImageGrab
import time

cc = cv2.VideoWriter_fourcc(*'mp4v')
name = "recordedVideo.mp4"
output = cv2.VideoWriter(name,cc,14,(1920,1080))
#time.sleep(5)

while True:
	image = ImageGrab.grab()
	image_numpy = np.array(image)
	reverted_image = cv2.cvtColor(image_numpy,cv2.COLOR_BGR2RGB)
	output.write(reverted_image)

	if(cv2.waitKey(1) != -1):
		break

output.release()
cv2.destroyAllWindows()

