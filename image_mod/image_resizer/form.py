from django import forms

class ImageForm(forms.Form):
    # Define form fields
    name = forms.CharField()  # A text field for user to input a name
    img = forms.ImageField()  # An image field for user to upload an image file
