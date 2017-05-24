from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .actions import detectImg

def index(request):
    if request.method == 'POST' and request.FILES['Image']:
        fs = FileSystemStorage()
        Img = request.FILES['Image']
        Imgname = fs.save(Img.name, Img)
        Imgurl = fs.url(Imgname)
        result = detectImg(Imgurl)
        return render(request, 'index.html', {'result': result})
    return render(request, 'index.html')


