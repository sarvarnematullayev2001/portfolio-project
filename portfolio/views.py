import os
from django.conf import settings
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import FilesAdmin

# Create your views here.
def home(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request, '../templates/home.html', context)

def download(request, path):
    file_path = os.path(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)                
            return response
            
        raise Http404