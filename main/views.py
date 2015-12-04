from django.shortcuts import render, redirect
from main.forms import SignInForm, SignupForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "home.html", )

def webhooks(request):
    if request.method == 'GET':
    if request.method == 'POST':
    return HttpResponse()


def sign_in(request):
    title = "Sign In"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/profile')
            else:
                message = "Account Disabeled"
        else:
            message = "Username/Password do not exist. Please try Again."
    else:
        message = "If you already have an account."
    return render(request, "signin.html", {"message": message, "title": title})


def sign_up(request):
    title = "Sign Up"
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            if request.POST['password'] != request.POST['password2']:
                message= "Passwords did not match. Please try again"
            else :
                # Save the user's form data to the database.
                user = form.save()
                # Hash Password
                user.set_password(user.password)
                user.save()
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect('/profile')

        # Print problems to terminal
        else:
            print(form.errors)
            message = form.errors

    # Not POST , redirect to needed page
    else:
        message = "If not already a Member."
    return render(request, "signup.html", {"message": message, "title": title})



def handler404(request):
    error = "404"
    message = "Oops. The page you're looking for doesn't exist."
    return render(request, 'error.html', {"title": error, "message": message}, context_instance=RequestContext(request))


def handler500(request):
    error = "500"
    message = "Yaiks. Stuff is not working."
    return render(request, 'error.html', {"title": error, "message": message}, context_instance=RequestContext(request))