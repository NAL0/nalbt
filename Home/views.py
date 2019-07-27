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

def index7(request):
    return render(request, 'Home/g1.html')

def index8(request):
    return render(request, 'Home/g2.html')

def index9(request):
    return render(request, 'Home/g3.html')

def index10(request):
    return render(request, 'Home/g4.html')

def index11(request):
    return render(request, 'Home/g5.html')

def index12(request):
    return render(request, 'Home/g6.html')

def index13(request):
    return render(request, 'Home/g7.html')

def index14(request):
    return render(request, 'Home/g8.html')

def index15(request):
    return render(request, 'Home/g9.html')

def index16(request):
    return render(request, 'Home/g10.html')

def index17(request):
    return render(request, 'Home/g11.html')

def index18(request):
    return render(request, 'Home/g12.html')

def index19(request):
    return render(request, 'Home/g13.html')

def index20(request):
    return render(request, 'Home/g14.html')

def index21(request):
    return render(request, 'Home/g15.html')

def index22(request):
    return render(request, 'Home/g16.html')

def index23(request):
    return render(request, 'Home/g17.html')

def index24(request):
    return render(request, 'Home/g18.html')


