from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import AllAppUrl

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    url_data = {
        'url_data' : AllAppUrl.objects.all().values(),
    }
    return HttpResponse(template.render(url_data, request))

# redirect / to /index url
def index_redirect(request):
    return redirect('index/')