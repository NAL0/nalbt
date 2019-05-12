from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Yakisizwe/initiative.html')

def index2(request):
    return render(request, 'Yakisizwe/dash.html')
