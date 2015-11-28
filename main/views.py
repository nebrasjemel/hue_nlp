from django.shortcuts import render, redirect
from main.forms import SignInForm, SignupForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "home.html", )


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/profile')
            else:
                return render(request, "signin.html", {"message": "Account Disabled."})
        else:
            return render(request, "signin.html", {"message": "Username/Password do not exist. Please try Again."})
    else:
        return render(request, "signin.html", {"message": "If you already have an account."})


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            if request.POST['password'] != request.POST['password2']:
                return render(request, "signup.html", {"message": "Passwords did not match. Please try again"})
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
            return render(request, "signup.html", {"message": form.errors})

    # Not POST , redirect to needed page
    else:
        return render(request, "signup.html", {"message": "If not already a Member."})
