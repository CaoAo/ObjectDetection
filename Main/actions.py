from django.core.files.storage import FileSystemStorage
from PIL import Image
import os

def detectImg(Imgurl):
    fs = FileSystemStorage()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    Img=Image.open(os.path.join(BASE_DIR,Imgurl))
    resultImg=Img.convert('L')
    resultImgname = fs.save(resultImg.name, resultImg)
    result = fs.url(resultImgname)
    return result

