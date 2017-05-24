from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .actions import detectImg
from ObjectDetection.settings import MEDIA_ROOT
import os

def index(request):
    if request.method == 'POST' and request.FILES['Image']:
        fs = FileSystemStorage()
        Img = request.FILES['Image']
        Imgname = fs.save(Img.name, Img)
        Imgurl = fs.url(Imgname)
        path=os.path.join(MEDIA_ROOT,Imgname)
        detectImg(path)
        result=Imgurl
        return render(request, 'index.html', {'result': result})
    return render(request, 'index.html')


