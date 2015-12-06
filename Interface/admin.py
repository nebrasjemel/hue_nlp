from django.contrib import admin


# Register your models here.

# request the home-page
def index(request):
    return render(request, "index.html", {})
