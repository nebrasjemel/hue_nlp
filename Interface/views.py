from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    return render(request, "profile.html", {})

@login_required
def social(request):
    return render(request, "social.html", {})

@login_required
def hue(request):
    return render(request, "hue.html", {})

@login_required
def account(request):
    return render(request, "account.html", {})

@login_required
def preferences(request):
    return render(request, "account.html", {})