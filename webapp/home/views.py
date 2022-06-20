from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import pyqrcode
from  .sendimage import *
import cv2
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        qr = pyqrcode.create(username+"/"+password)
        qr.png('home/static/home/uploads/qrcode.png', scale=5)

        send(email,'home/static/home/uploads/qrcode.png')

        return render(request, 'signup.html', {'png':'Signup Success QRCode has been sent to ur Mail. Please check ur Spam as well'})
    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        img = request.FILES['img']
        f = open('img.png', 'wb')
        f.write(img.read())
        f.close()
        image = cv2.imread('img.png')
        qrCodeDetector = cv2.QRCodeDetector()
        decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
        print(decodedText)
        arr = decodedText.split('/')
        username = arr[0]
        password = arr[1]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("logged")
            login(request, user)
            return redirect('https://www.localhost:8000')
    return render(request, 'signin.html')