import numpy as np
import cv2
import time


bgr_image = cv2.imread('lemons1.jpg')
image = bgr_image.copy()

no_of_lemons = 0  
if lemons is not None:
    lemons = np.round(lemons[0, :]).astype("int")
    no_of_lemons = len(lemons)

    for (x, y, r) in lemons:
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
end = time.time()
print ('no of lemons : {}'.format(no_of_lemons))
print ("Seconds: {}".format(end - start))
