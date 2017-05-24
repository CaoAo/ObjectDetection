from django.core.files.storage import FileSystemStorage
from PIL import Image,ImageFilter
import os
from ObjectDetection.settings import MEDIA_ROOT

def detectImg(path):
    Img=Image.open(path)
    resultImg =Img.filter(ImageFilter.BLUR)
    resultImg.save(path)


