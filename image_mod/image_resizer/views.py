from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
import cv2
import numpy as np
from .form import ImageForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.

def resizer(request):
    # Generate the URL for the imgprocess view
    process_link = reverse('imgprocess')
    
    # Render the template with the form and the processlink
    template = loader.get_template('resizer_page.html')
    context = {
        'form': ImageForm(),
        'processlink': process_link,
    }
    return HttpResponse(template.render(context, request))

def imgprocess(request):
    if request.method == 'POST':
        # Get the uploaded image from the request
        uploaded_img = request.FILES['img']
        if uploaded_img.content_type.startswith('image'):
            # Save the uploaded image to a temporary location
            saved_path = default_storage.save('temp_image.jpg', ContentFile(uploaded_img.read()))
            
            # Get the absolute path of the saved file
            absolute_path = os.path.join(default_storage.location, saved_path)
            
            # Create an instance of the Image class with the absolute path
            img = Image(absolute_path)
            if img.load_image():
                # If image loaded successfully, show it
                img.show_image()
                return HttpResponse("image uploaded!")
            else:
                return HttpResponse("Image loading failed") 
        else:
            return HttpResponse("Not a valid image!")
    else:
        return HttpResponse("Method is not POST!")

class Image:
    def __init__(self, path) -> None:
        # Initialize the Image object with the path to the image file
        self.img_path = path
    
    def load_image(self) -> bool:
        # Load the image from the specified path
        self.image = cv2.imread(self.img_path)
        # Check if the image was loaded successfully
        return self.image is not None

    def resize(self, height, width):
        # Resize the image to the specified height and width
        self.image = cv2.resize(self.image, (width, height))   

    def show_image(self) -> None:
        # Display the image in a window
        cv2.imshow('Resized Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def save_image(self, new_image_name):
        # Save the image with a new name
        cv2.imwrite(new_image_name, self.image)
