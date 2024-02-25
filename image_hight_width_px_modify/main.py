import cv2
import numpy as np

random_image = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)

cv2.imwrite('random_color_image.png', random_image)

cv2.imshow('Random Color Image', random_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Value of first pixel: ",random_image[0, 0])