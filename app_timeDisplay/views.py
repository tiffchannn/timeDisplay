from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.utils import timezone
from time import strftime, gmtime

# Create your views here.

def index(request):
    print("In the index function")
    return HttpResponse("This is coming from views.py!")

def displayTime(request):
  print('*'*60)
  print('In the displayTime function')
  nowDateTime = datetime.datetime.now()
  nowTimeZone = timezone.now()

  context = {
    "date": strftime("%b %d, %Y", gmtime()),
    "time": strftime("%I:%M %p", gmtime()),
  }
  return render(request, "index.html", context)