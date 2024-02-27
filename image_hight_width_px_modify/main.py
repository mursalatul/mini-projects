import cv2
import numpy as np

class Image:
    def __init__(self, path) -> None:
        self.img_path = path
    
    def load_image(self) -> bool:
        # loading the image
        image = cv2.imread(self.img_path)
        # return status
        if image is not None:
            self.image = image
            return True
        else:
            return False

    def resize(self, hight, width):
        self.image = cv2.resize(self.image, (width, hight))   

    def show_image(self) -> None:
        cv2.imshow('Resized Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def save_image(self, new_image_name):
        cv2.imwrite(new_image_name, self.image)

img = Image("random_color_image.png")
if not img.load_image():
    print("Image load failed")
else:
    # image loaded
    width, hight = [int(x) for x in input("Width, hight: ").split()]
    img.show_image()
    img.resize(width, hight)
    img.show_image()
    sv = input("Save(0/1): ")
    if sv == "1":
        img.save_image("new.jpg")
        print("saved")
    else:
        pass