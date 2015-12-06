from django.shortcuts import render
from classifier.models import Database
import os
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from main.views import handler404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def scrap(request):
    Database.objects.all().delete()
    f = open(os.path.join(settings.PROJECT_ROOT, 'Data.txt'))
    counter = 10
    c = 0
    word = Database(word='nebras')
    for line in f:
        sp = line.split()
        if counter == 10:
            try:
                word.save()
                print(sp[0])
            except:
                pass
            c += 1
            word = Database(word=sp[0])
            word.anger = bool(int(sp[2]))
            print("anger", sp[2])
            counter = 1
        elif counter == 1:
            word.anticipation = bool(int(sp[2]))
            print("anti", sp[2], c)
            counter += 1
        elif counter == 2:
            word.disgust = bool(int(sp[2]))
            counter += 1
            print("disg", sp[2], c)
        elif counter == 3:
            word.fear = bool(int(sp[2]))
            counter += 1
            print("fear", sp[2], c)
        elif counter == 4:
            word.joy = bool(int(sp[2]))
            counter += 1
            print("joy", sp[2], c)
        elif counter == 5:
            word.sadness = bool(int(sp[2]))
            counter += 1
            print("sadness", sp[2], c)
        elif counter == 6:
            counter += 1
        elif counter == 7:
            counter += 1
        elif counter == 8:
            word.surprise = bool(int(sp[2]))
            counter += 1
            print("surprise", sp[2], c)
        elif counter == 9:
            word.trust = bool(int(sp[2]))
            counter += 1
            print("trust", sp[2], c)
    f.close()
    return render(request, "home.html", {'title': "Scrap Successful"})


@csrf_exempt
@login_required
def classify(request):
    for key in request.POST:
        value = request.POST[key]
        print(value)
    if request.method == 'POST' and isinstance(request.POST["status"], str):
        words = request.POST["status"].split()
        angers = 0
        disgusts = 0
        joys = 0
        sadnesss = 0
        surprises = 0
        trusts = 0
        neg = False
        for x in words:
            query = Database.objects.filter(word=x)
            if query:
                query = query[0]
                if query.anger or query.fear:
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
                return JsonResponse({'result': "none"})
            return JsonResponse({'result': "anger"})
        elif maximum == disgusts:
            return JsonResponse({'result': "disgust"})
        elif maximum == joys:
            return JsonResponse({'result': "joy"})
        elif maximum == sadnesss:
            return JsonResponse({'result': "sadness"})
        elif maximum == surprises:
            return JsonResponse({'result': "surprise"})
        elif maximum == trusts:
            return JsonResponse({'result': "trust"})
    else:
        return handler404(request)
