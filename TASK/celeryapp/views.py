from django.shortcuts import render
from django.shortcuts import HttpResponse

from .task import *


# Create your views here.
def index(request):
    send_mail_task.delay()

    return render(request,'index.html')

def send(request):
    return HttpResponse('send email successfully')



