from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordList = fulltext.split(' ')

    word_dict = {}

    for word in wordList:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    num = len(wordList)
    return render(request, 'count.html', {'fulltext': fulltext, 'num': num, 'sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')

