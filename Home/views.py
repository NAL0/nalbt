from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'Home/home.html')

def index2(request):
	return render(request, "Home/SDG's.html")

def index3(request):
    return render(request, 'Home/1.html')

def index4(request):
    return render(request, 'Home/2.html')
