# -*- encoding: utf-8 -*-



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import *
from .models import *

@login_required(login_url="/login/")
def index(request):
    form = RationCardInput(request.POST or None)
    msg = None
    found = None
    step = None
    if request.method == "POST":
        if form.is_valid():
            rationcard_rx = form.cleaned_data.get("rationcard_rx")
            try:
                benificiary = RationCard.objects.get(number=rationcard_rx)
            except RationCard.DoesNotExist:
                benificiary = None
            if benificiary is not None:
                msg = 'Found'
                fps_set = request.user.fps_set.all()
                print(fps_set)
                return render(request, "index.html", {"form": form, "msg": msg, "found": benificiary})
            else:
                msg = 'Ration Card with said number not found'
        else:
            msg = 'Invalid Ration card number'
    return render(request, "index.html", {"form": form, "msg": msg, "found": found})


@login_required(login_url="/login/")
def index(request):
    form = RationCardInput(request.POST or None)
    msg = None
    found = None
    step = None
    if request.method == "POST":
        if form.is_valid():
            rationcard_rx = form.cleaned_data.get("rationcard_rx")
            try:
                benificiary = RationCard.objects.get(number=rationcard_rx)
            except RationCard.DoesNotExist:
                benificiary = None
            if benificiary is not None:
                msg = 'Found'
                fps_set = request.user.fps_set.all()
                print(fps_set)
                return render(request, "index.html", {"form": form, "msg": msg, "found": benificiary})
            else:
                msg = 'Ration Card with said number not found'
        else:
            msg = 'Invalid Ration card number'
    return render(request, "index.html", {"form": form, "msg": msg, "found": found})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
