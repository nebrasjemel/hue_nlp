# import all the libraries, files and the database
from django.shortcuts import render
from classifier.models import Database
import os
import re
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from main.views import handler404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# scrap is taking the dictionary and is loading it into the database
def scrap(request):
    # delete everything that previously existed in the database
    Database.objects.all().delete()
    
    # open the data file and keep it in f
    f = open(os.path.join(settings.PROJECT_ROOT, 'Data.txt'))
    
    # counter is the number of columns in our database
    counter = 10
    # create an entry in the database (as a model)
    word = Database(word = 'nebras')
    
    # we take a line in the file
    for line in f:
        # we split it into its components
        sp = line.split()
        
        # if counter = 10, we have a word; we try to save it; if not, we save the other attributes
        if counter == 10:
            try:
                word.save()
                print(sp[0])
            except:
                pass
            # word is not the first entry in our database and we save it
            word = Database(word = sp[0])
            
            # we take its angry state ( true or false) and save it and modify the counter
            word.anger = bool(int(sp[2]))
            counter = 1
            
        # else the counter is some other number, we simply remember its state( true or false)
        # word.feeling are ment to remember whether a word suggests any feeling or not
        elif counter == 1:
            word.anticipation = bool(int(sp[2]))
            counter += 1
        elif counter == 2:
            word.disgust = bool(int(sp[2]))
            counter += 1
        elif counter == 3:
            word.fear = bool(int(sp[2]))
            counter += 1
        elif counter == 4:
            word.joy = bool(int(sp[2]))
            counter += 1
        elif counter == 5:
            word.sadness = bool(int(sp[2]))
            counter += 1
        elif counter == 6:
            counter += 1
        elif counter == 7:
            counter += 1
        elif counter == 8:
            word.surprise = bool(int(sp[2]))
            counter += 1
        elif counter == 9:
            word.trust = bool(int(sp[2]))
            counter += 1
    # close the file
    f.close()
    
    # return to the home page
    return render(request, "home.html", {'title': "Scrap Successful"})

# we don't need csrf because it's Ajax and is not a form
# we also require login
@csrf_exempt
@login_required

# we know try to classify the request into one of the feelings
def classify(request):
    # check if the user reached via POST
    if request.method == 'POST':
        # split the text into words
        words = request.POST["status"].split()
        
        # we know want to count each occurence of a suggestion in one of the 
        # words of a feeling. We initiaize them to 0
        angers = 0
        disgusts = 0
        joys = 0
        sadnesss = 0
        surprises = 0
        trusts = 0
        
        # we also want to track whether there are some negative words 
        # that could potentially change the meaning of a following word
        # ex: I am not angry does not suggest angriness
        neg = False
        
        # for a word
        for x in words:
            # we get rid of punctuation (in "I am angry.", we want "angry"
            # , not "angry."
            x = re.sub('[\W_]', "", x)
            
            # we check if the word is in our database
            query = Database.objects.filter(word = x)
            
            # if it is, then 
            if query:
                # we take the first entry ( the word)
                query = query[0]
                
                # if angry of fearful
                if query.anger or query.fear:
                    # if it had a negation, the increase trust by 1
                    # the negation no longer applies, so we change it to false
                    if neg:
                        trusts += 1
                        neg = False
                    else:
                        # else, increase the angriness
                        angers += 1
                        
                # we repeat the process for all the other feelings        
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
            # at the end, we check for negations; we check for no, not
            # nor, neither, and last but not least, verbal forms that end in
            # n't
            elif x == 'not' or x == 'no' or x[-3:] == "n't" or x == 'neither' or x == 'nor':
                neg = True
                
        # at the end, we take the maximum of the 6 feelings ( we get only 6 because
        # we coupled some pairs of them because they were very hard to distinguish)
        maximum = max(angers, disgusts, joys, sadnesss, surprises, trusts)
        
        # we check which one is the maximum
        if maximum == angers:
            # if the maximum is 0, the respond with none
            if angers == 0:
                return JsonResponse({'result': "none"})
            # else, respond with anger    
            return JsonResponse({'result': "anger"})
        # similarly, in the other cases, respond with the feeling that
        # has the maximum number of words that indicate it
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
            
    # at the end, if not a POST request, handle it with a 404        
    else:
        return handler404(request)
