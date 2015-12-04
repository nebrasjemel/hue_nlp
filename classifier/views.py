from django.shortcuts import render
from classifier.models import Database
import os
from django.conf import settings


# Create your views here.

def scrap(request):
    f = open(os.path.join(settings.PROJECT_ROOT, 'Data.txt'))
    counter = 10
    word = Database(word='nebras')
    for line in f:
        sp = line.split()
        if counter == 10:
            try:
                word.save()
            except:
                pass
            word = Database(word=sp[0])
            word.anger = sp[2]
            counter == 1
        elif counter == 1:
            word.anticipation = sp[2]
            counter += 1
        elif counter == 2:
            word.disgust = sp[2]
            counter += 1
        elif counter == 3:
            word.fear = sp[2]
            counter += 1
        elif counter == 4:
            word.joy = sp[2]
            counter += 1
        elif counter == 5:
            word.sadness = sp[2]
            counter += 1
        elif counter == 6:
            counter += 1
        elif counter == 7:
            counter += 1
        elif counter == 8:
            word.surprise = sp[2]
            counter += 1
        elif counter == 9:
            word.trust = sp[2]
            counter += 1
    f.close()
    return render(request, "home.html", {'title': "Scrap Successful"})
