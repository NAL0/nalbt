from django.shortcuts import render
import calendar
import os
# Create your views here.

def index(request):
            return render(request, 'Calendar/Calendar.html')
