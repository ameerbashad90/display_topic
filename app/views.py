from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render (request,'display_topics.html',d)