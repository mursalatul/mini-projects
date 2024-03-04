from django.db import models

# Create your models here.

class AllAppUrl(models.Model):
    # store row url(example: 'imgresizer/')
    url = models.CharField(max_length=30)
    #  store name of the url
    url_name = models.CharField(max_length=100, null=True)