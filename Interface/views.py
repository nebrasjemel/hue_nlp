from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Interface.models import FacebookAccount, PhilipsHue
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from  django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login



# Create your views here.

# if already loged-in
@login_required
# render the profile with the parameters
def profile(request):
    title = "Welcome, " + request.user.get_username()
    message = "This is your main page."
    query = PhilipsHue.objects.filter(user = request.user)
    return render(request, "profile.html", {'title': title, 'message': message, 'query': query})

# we don't need csrf because it's Ajax and is not a form
# also require login
@csrf_exempt
@login_required
def social(request):
    title = "Social Settings"
    # get the Facebook account
    query = FacebookAccount.objects.filter(user = request.user)
    # if the user exists, take the first entry
    if query:
        query = query[0]
    # check that the page was reached via POST    
    if request.method == 'POST':
        # create a Facebook form
        form = FacebookAccount(user = request.user, account_id = request.POST['userID'],
                               account_name = request.POST['account_name'])
        # Save the user's form data to the database.
        form.save()
        message = "Account Added Successfully"
        # Print problems to terminal
        print(request.POST['account_name'])
    # Not POST , redirect to needed page
    else:
        message = "Manage Your Social Media Accounts"
    return render(request, "social.html", {'title': title, 'message': message, 'query': query, 'fb': True})

# require login 
@login_required
def hue(request):
    title = "Philips Hue Settings"
    message = "Manage Your Social Media Accounts"
    # get the user's Phillips Hue and Facebook Accounts
    query = PhilipsHue.objects.filter(user = request.user)
    accounts = FacebookAccount.objects.filter(user_id = request.user.id)
    # check that it was issued via POST
    if request.method == 'POST':
        related = FacebookAccount.objects.filter(account_name = request.POST['related_account'])
        form = PhilipsHue(user = request.user, username = request.POST['username'], ip_address = request.POST['ip_address'],
                          related_account = related[0])
        # Save the user's form data to the database.
        # If all good, save the form
        form.save()
        message = "Hue Added Successfully"
        # Print problems to terminal
        print(request.POST['related_account'])


    # Not POST , redirect to needed page
    else:
        message = "Configure your Philips Hue Lamps"
    return render(request, "hue.html", {'title': title, 'message': message, 'query': query, 'accounts': accounts})

# require login for account settings
@login_required
def account(request):
    title = "Account Settings"
    message = "Edit your personal Settings"
    if request.method == 'POST':
        u = User.objects.get(username=request.user.username)
        passw = request.POST.get('old_password', 0)
        if passw is not 0 :
            test = check_password(passw, u.password)
            if test:
                u.set_password(request.POST["password"])
                u.save()
                newuser=authenticate(username= u.username,password=request.POST["password"])
                message = "Password Successfully changed"
                login(request,newuser)
            else:
                message = "Old Password is incorrect"
        else :
            fname = request.POST.get('first_name', 0)
            if fname is not 0 :
                u.first_name = fname
                message= "First Name Successfully changed"
            else :
                lname = request.POST.get('last_name',0)
                if lname is not 0:
                    u.last_name = lname
                    message = "Last Name Successfully changed"
                else: 
                    mail = request.POST.get('email',0)
                    if mail is not 0:
                        u.email= mail
    return render(request, "account.html", {'title': title, 'message' : message})

# require login for preferences
@login_required
def preferences(request):
    title = "Color Preferences"
    return render(request, "color.html", {'title': title})
