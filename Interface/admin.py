from django.contrib import admin

# Register your models here.

def index(request):
    return render(request, "index.html", {})