from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def profile(request):
    title = "Welcome, " + request.user.get_username()
    message = "This is your settings page."
    return render(request, "profile.html", {'title': title, 'message': message})


@login_required
def social(request):
    title = "Social Settings"
    message = "Manage Your Social Media Accounts"
    return render(request, "social.html", {'title': title, 'message': message})


@login_required
def hue(request):
    title = "Philips Hue Settings"
    return render(request, "hue.html", {'title': title})


@login_required
def account(request):
    title = "Account Settings"
    return render(request, "account.html", {'title': title})


@login_required
def preferences(request):
    title = "Color Preferences"
    return render(request, "account.html", {'title': title})