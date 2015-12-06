from django.shortcuts import render, redirect
from main.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponse


# Create your views here.

# redirect to home
def home(request):
    return render(request, "home.html", )

# enable sign in
def sign_in(request):
    title = "Sign In"
    
    # if the page was reached via POST
    if request.method == 'POST':
        # get the user input
        username = request.POST['username']
        password = request.POST['password']
        # authenticate the input
        user = authenticate(username = username, password = password)
        # if User exists
        if user is not None:
            # if User is active, log him in
            if user.is_active:
                login(request, user)
                return redirect('/profile')
            # else error    
            else:
                message = "Account Disabled"
        # if User does not exist, send the error         
        else:
            message = "Username/Password do not exist. Please try Again."
    # if not reached via POST, redirect        
    else:
        message = "If you already have an account."
    return render(request, "signin.html", {"message": message, "title": title})

# define sign_up
def sign_up(request):
    title = "Sign Up"
    #if reached via POST
    if request.method == 'POST':
        # make the SignUpForm
        form = SignupForm(data = request.POST)
        # if the form is valid
        if form.is_valid():
            # check that the input is correct(Passwords match)
            if request.POST['password'] != request.POST['password2']:
                message = "Passwords did not match. Please try again"
            # if passwords do match, (we do not need to check for double 
            # users because django does that 
            else:
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

# handle a 404
def handler404(request):
    error = "404"
    message = "Oops. The page you're looking for doesn't exist."
    return render(request, 'error.html', {"title": error, "message": message}, context_instance=RequestContext(request))

# handle a 500
def handler500(request):
    error = "500"
    message = "Yaiks. Stuff is not working."
    return render(request, 'error.html', {"title": error, "message": message}, context_instance=RequestContext(request))
