from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
	return render(request, 'Home/home.html')

def index2(request):
	return render(request, "Home/SDG's.html")

@login_required
def index3(request):
    return render(request, 'Home/constitutive_act.html')

def index4(request):
    return render(request, 'Home/2.html')

def index5(request):
    return render(request, 'Home/SADC_national_anthem.html')

def index6(request):
    return render(request, 'Home/plan.html')

##def index8(request):
##    return render(request, 'Home/sign_in.html')
