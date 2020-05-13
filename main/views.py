from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import skills, bigpp, Video, category, series#,vserver,vclient
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import newForm, contact_form
from django.views.generic.base import RedirectView
from subprocess import run,PIPE
import sys
import subprocess
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.

def single_slug(request, single_slug):
    Cat=[c.Cslug for c in category.objects.all()]
    if single_slug in Cat:
        matching_series=series.objects.filter(Category__Cslug=single_slug)
        Series_urls={}
        
        for m in matching_series.all():
            part_one=skills.objects.filter(Series__Stitle=m.Stitle)[0]
        
            Series_urls[m] = part_one.slug
        return render(request, "main/categories.html", {"part_ones": Series_urls})
    
    ski=[t.slug for t in skills.objects.all()]
    if single_slug in ski:
        this_tutorial = skills.objects.get(slug=single_slug)
        skfs=skills.objects.filter(Series__Stitle=this_tutorial.Series)

        this_tutorial_idx=list(skfs).index(this_tutorial)

        return render(request = request,
                      template_name="main/tutorial.html",
                      context = {"skills":this_tutorial, "sidebar":skfs, "this_tutorial_idx":this_tutorial_idx})

    
    return HttpResponse("no category found!!")


def homepage(request):
    return render(request,"main/category.html",context={"category": category.objects.all})

def register(request):
    if request.user.is_authenticated:
        return redirect("main:homepage")
    else:
        if request.method == "POST":
            form=newForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                messages.success(request, f"Account created successfully {username}")
                login(request, user)
                return redirect("main:homepage")
                
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])
        form=newForm
        return render(request, "main/register.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!!")
    return redirect("main:homepage")

def login_request(request):
    if request.user.is_authenticated:
        return redirect("main:homepage")
    else:
        if request.method == "POST":
            form=AuthenticationForm(request, request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username='username', password='password')
                if user is not None:
                    login(request, user)
                    messages.info(request, f"Account logged in successfully for {username}")
                    return redirect("main:homepage")
                    
                else:
                    messages.error(request, "invalid username or password")
            else:
                    messages.error(request, "invalid username or password")

        form=AuthenticationForm()
        return render(request, "main/login.html", {"form":form})

def bigppp(request):
    if not request.user.is_authenticated:
        return redirect("main:login")
    else:
        return render(request, "main/makeppbig.html",context={"bigpp": bigpp.objects.all})

def bshow(request):
    if not request.user.is_authenticated:
        return redirect("main:login")
    else:
        return render(request, "main/blogshow.html",context={"Video": Video.objects.all})

def membership(request):
    if not request.user.is_authenticated:
        return redirect("main:login")
    else:
        return render(request, "main/membership.html")
    
