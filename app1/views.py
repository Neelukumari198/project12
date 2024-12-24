from django.shortcuts import render

# Create your views here.
def sheryians(request):
    return render(request,'sheryians.html')
def home(request):
    return render(request,'home.html')
def Courses(request):
    return render(request,'Courses.html')
def Bootcamp(request):
    return render(request,'Bootcamp.html')
def RequestCallback(request):
    return render(request,'RequestCallback.html')
def frontend(request):
    return render(request,'frontend.html')
def backend(request):
    return render(request,'backend.html')

def java(request):
    return render(request,'java.html')

def Aptitude(request):
    return render(request,'Aptitude.html')

