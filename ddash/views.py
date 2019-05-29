from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'ddash/dashboard.html')


def index2(request):
	return render(request, 'ddash/y_dash.html')

def index3(request):
	return render(request, 'ddash/constitution.html')
