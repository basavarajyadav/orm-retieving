from os import access
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topic(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    webpage=Webpage.objects.all()
    #webpages=Webpage.objects.filter(Topic_name='Foot Ball')
    #webpages=Webpage.objects.exclude(Topic_name='Foot Ball')
    #webpages=Webpage.objects.all()[0:2:]
    #webpages=Webpage.objects.all()[-3]#its throw error
    #webpages=Webpage.objects.all().order_by('Name')
    #webpages=Webpage.objects.all().order_by('-Name')
    #webpages=Webpage.objects.all().order_by(Length('Name'))
    #webpages=Webpage.objects.all().order_by(Length('Name').desc())
    #webpages=Webpage.objects.filter(Name__startswith='sam')
    #webpages=Webpage.objects.filter(Name__endswith='e')
    #webpages=Webpage.objects.filter(Name__contains='t')
    #webpages=Webpage.objects.filter(Name__in=('Samantha','Kathleen'))
    #webpages=Webpage.objects.filter(Name__regex=r'^[a-zA-Z]{2}m')
    #webpages=Webpage.objects.filter(Q(Topic_name='Kabaddi') & Q(Name='Kathleen'))
    #webpages=Webpage.objects.filter(Q(Topic_name='Foot Ball') & Q(Url__startswith='https') & Q(Name__endswith='e'))
    d={'WS':webpage}

    return render(request,'display_webpage.html',d)

def display_Access(request):
    access=Access_Records.objects.all()
    access=Access_Records.objects.filter(date='2007-08-07')
    #access=Access_Records.objects.filter(date__gte='2007-08-07')
    #access=Access_Records.objects.filter(date__lt='2007-08-07')
    #access=Access_Records.objects.filter(date__year='2020')
    #access=Access_Records.objects.filter(date__year__gt='2020')
    #access=Access_Records.objects.filter(date__month='08')
    #access=Access_Records.objects.filter(date__day='7')
    d={'AS':access}
    return render(request,'display_Access.html',d)

def update_webpage(request):
    #Webpage.objects.filter(Topic_name='Foot Ball').update(Name='Ronaldo')
    #Webpage.objects.filter(Name='YADAV').update(Url='http://YADAV.com/')
    #Webpage.objects.update_or_create(Name='Samantha',defaults={'Url':'http://Samantha.com/'})
    t=Topic.objects.get_or_create(Topic_name='Rugbi')[0]
    t.save()
    Webpage.objects.update_or_create(Topic_name='Rugbi',defaults={'Topic_name':t,'Name':'Rugbi Star','Url':'http://Ronaldo.com/'})
    webapge=Webpage.objects.all()
    d={'WS':webapge}
    return render(request,'display_webpage.html',d)

def delete_webpage(request):
    Webpage.objects.filter(Name='Ronaldo').delete()
    #Webpage.objects.all().delete()
    webapges=Webpage.objects.all()
    d={'WS':webapges}
    return render(request,'display_webpage.html',d)


