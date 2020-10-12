from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def time(request):
    t=datetime.datetime.now()
    msg1='<h1>This is second project</h1><hr>'
    msg2=msg1+'<h1>The current time is:'+str(t)+'</h1>'

    return HttpResponse(msg2)
