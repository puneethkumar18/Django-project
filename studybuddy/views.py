from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World! 🌍</h1>")

def home(request):
    return render(request=request,template_name='home.html')

def login(request):
    return render(request,template_name='login.html')

def register(request,method=["POST"]):
    if request.method == 'POST':
        return HttpResponse("<h1>You have reached the correct URL, Congraulations!🌱</h1>")
    return render(request,template_name='register.html')