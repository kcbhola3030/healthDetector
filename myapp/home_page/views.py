from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):

    print("request arrived!")
    return render(request,'index.html')

def handlefile(request):
    print(len(request.FILES))
    if len(request.FILES)!= 0:
        os.remove('./static/FILES/result.jpg')
        os.remove('./static/RESULT/result.jpg')
        folder='./static/FILES/'
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
        filename = fs.save("result.jpg", myfile)
        os.system('python ../yolov5/detect.py --weights ../yolov5/runs/train/exp/weights/best_fruit_quality.pt --img 640 --conf 0.25 --source ./static/FILES/result.jpg')
        print(filename)
    return render(request,'index.html')