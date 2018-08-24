from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
import math
# Create your views here.
from django.template import loader

from Board.forms import ImageForm
from Board.models import Image

imagesOnOneSite = 10

def annoucments(request):
    return render(request, 'annoucments.html')

def main(request):
    return redirect('/kwejk/1')

@login_required(login_url='/login/')
def kwejk(request, siteNumber):
    siteNumber = siteNumber - 1
    if siteNumber < 1:
        images = Image.objects.all().order_by('-date')[0:imagesOnOneSite]
    else:
        startIndex = imagesOnOneSite*siteNumber
        images = Image.objects.all().order_by('-date')[startIndex:startIndex+10]
    numberOfSites = math.ceil(Image.objects.all().count()/10)
    indexTemplate = loader.get_template('kwejk.html')
    context = {
        'siteNumber' : siteNumber+1,
        'images': images,
        'numberOfSites' : numberOfSites,
    }
    return HttpResponse(indexTemplate.render(context, request))

def gif_monitor(request):
    try:
        image = Image.objects.filter(isOnGifMonitor=True).get()
    except ObjectDoesNotExist:
        print("Gif monitor is currently empty")
        image = Image.objects.none()
    indexTemplate = loader.get_template('gif-monitor.html')
    context = {
        'image': image,
    }
    return HttpResponse(indexTemplate.render(context, request))

def pronto_timer(request):
    return render(request, "pronto-timer.html")

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            image = form.save(commit=False)
            image.addedBy = user
            image.save()
        return redirect('/kwejk/1')
    else:
        form = ImageForm()
    return render(request, "add-image.html", {'form' : form})

@user_passes_test(lambda u : u.is_superuser)
def push_to_gif_monitor(request,pk):
    image = Image.objects.filter(pk=pk).get()
    image.isOnGifMonitor = True
    image.save()
    return redirect('/gif-monitor')

@user_passes_test(lambda u : u.is_superuser)
def delete_image(request,pk):
    image = Image.objects.filter(pk=pk).get()
    image.delete()
    return redirect('/kwejk/1')