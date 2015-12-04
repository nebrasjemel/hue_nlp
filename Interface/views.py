from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Interface.models import FacebookAccount, PhilipsHue
from Interface.forms import FbForm
import socket


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
    query = FacebookAccount.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = FbForm(data=request.POST)
        form.user = request.user
        if form.is_valid():
            # Save the user's form data to the database.
            form.save()
            message = "Hue Added Successfully"

        # Print problems to terminal
        else:
            print(form.errors)
            message = form.errors

    # Not POST , redirect to needed page
    else:
        message = "Configure your Social Accounts"
    return render(request, "social.html", {'title': title, 'message': message, 'query': query})


@login_required
def hue(request):
    title = "Philips Hue Settings"
    message = "Manage Your Social Media Accounts"
    query = PhilipsHue.objects.filter(user_id=request.user.id)
    accounts = FacebookAccount.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        related = FacebookAccount.objects.filter(account_name=request.POST['related_account'])
        form = PhilipsHue(user=request.user, username=request.POST['username'], ip_address=request.POST['ip_address'],
                          related_account=related[0])
        # Save the user's form data to the database.
        form.save()
        message = "Hue Added Successfully"
        # Print problems to terminal
        print(request.POST['related_account'])


    # Not POST , redirect to needed page
    else:
        message = "Configure your Philips Hue Lamps"
    return render(request, "hue.html", {'title': title, 'message': message, 'query': query, 'accounts': accounts})


@login_required
def account(request):
    title = "Account Settings"
    return render(request, "account.html", {'title': title})


@login_required
def preferences(request):
    title = "Color Preferences"
    return render(request, "color.html", {'title': title})
