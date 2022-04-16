from os import access
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    webpage=Webpage.objects.all()
    webpages=Webpage.objects.filter(Topic_name='Foot Ball')
    #webpages=Webpage.objects.exclude(Topic_name='Foot Ball')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]
    webpages=Webpage.objects.all().order_by('Name')
    webpages=Webpage.objects.all().order_by('-Name')
    webpages=Webpage.objects.all().order_by(Length('Name'))
    webpages=Webpage.objects.all().order_by(Length('Name').desc())
    d={'WS':webpages}

    return render(request,'display_webpage.html',d)

def display_Access(request):
    access=Access_Records.objects.all()
    d={'AS':access}
    return render(request,'display_Access.html',d)

