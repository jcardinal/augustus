import requests
from django.shortcuts import render
from django.http import HttpResponse
from vocab.models import Word, Definition, Example
from django.contrib.auth.models import User
from django.conf import settings


def home(request):
    return render(request, 'vocab/home.html')


def word(request, word):
    w = Word.objects.filter(word=word).first()
    if w and w.word == word:
        defs = w.data[0]['shortdef']
    else:
        r = requests.get(
            f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={settings.MW_DICT_API_KEY}')
        new_entry = Word(word=word, data=r.json(), user=User.objects.first())
        new_entry.save()
        defs = r.json()[0]['shortdef']
        for defn in defs:
            d = Definition(word=new_entry, text=defn)
            d.save()

    context = {
        'word': word,
        'definitions': defs
    }
    return render(request, 'vocab/word.html', context)
