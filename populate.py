#set up django environments
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project22.settings')
#adding features of django
import django
django.setup()
import random
from faker import Faker
f=Faker()
from app.models import *
topics=['cricket','Foot Ball','Volley Ball','Kabaddi','Basket Ball']

def add_topic():
    t=Topic.objects.get_or_create(Topic_name=random.choice(topics))[0]
    t.save()
    return t

def add_webpage(WN,WU):
    t=add_topic()
    w=Webpage.objects.get_or_create(Topic_name=t,Name=WN,Url=WU)[0]
    w.save()
    return w

def add_access(WN,WU,WD):
    w=add_webpage(WN,WU)
    a=Access_Records.objects.get_or_create(Name=w,date=WD)[0]
    a.save()

def add_data(n):

    for i in range(1,n+1):
        WN=f.first_name()
        WU=f.url()
        WD=f.date()
        add_access(WN,WU,WD)
if __name__=='__main__':
    n=int(input('enter how many rows u wants to insert'))
    print('population is started')
    add_data(n)
    print('population is ended')