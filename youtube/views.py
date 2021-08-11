
from django.shortcuts import render, redirect
from.models import *
from datetime import date, timedelta


def video(request):
    error=''
    if request.method == 'POST':
        v = request.FILES['videoo']
        c = request.POST['caption']
        t = request.FILES['image']
        ty = request.POST['type']
        try:
            Video.objects.create(video=v, caption=c, thumbnail=t,type=ty,creationdate=date.today())
            error = "no"
        except:
            error = "yes"

    video=Video.objects.all()
    d={'video': video,'error': error,}
    return render(request,'video.html',d)

def videosearch(request):

    if request.method == 'GET':
        search= request.GET['search']
        captionfilter   = Video.objects.filter(caption__icontains=search)
        typefilter      = Video.objects.filter(type__icontains=search)
        caption = captionfilter.union(typefilter)
    d = {'caption': caption,'search': search,}
    return render(request, 'videosearch.html', d)