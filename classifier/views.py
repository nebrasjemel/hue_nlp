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


def classify(status):
    words = status.split()
    angers = 0
    disgusts = 0
    joys = 0
    sadnesss = 0
    surprises = 0
    trusts = 0
    neg = False
    for x in words:
        query = Database.objects.get(word=x)
        if query:
            if query.anger or query.fears:
                if neg:
                    trusts += 1
                    neg = False
                else:
                    angers += 1
            elif query.anticipation or query.surprise:
                if neg:
                    disgusts += 1
                    neg = False
                else:
                    surprises += 1
            elif query.disgust:
                if neg:
                    neg = False
                    surprises += 1
                else:
                    disgusts += 1
            elif query.joy:
                if neg:
                    neg = False
                    sadnesss += 1
                else:
                    joys += 1
            elif query.sadness:
                if neg:
                    joys += 1
                    neg = False
                else:
                    sadnesss += 1
            elif query.trust:
                if neg:
                    angers += 1
                    neg = False
                else:
                    trusts += 1
        elif x == 'not' or x == 'no' or x[-3:] == "n't" or x == 'neither' or x == 'nor':
            neg = True
    maximum = max(angers, disgusts, joys, sadnesss, surprises, trusts)
    if maximum == angers:
        if angers == 0:
            return 0
        return 1
    elif maximum == disgusts:
        return 2
    elif maximum == joys:
        return 3
    elif maximum == sadnesss:
        return 4
    elif maximum == surprises:
        return 5
    elif maximum == trusts:
        return 6