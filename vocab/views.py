import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from vocab.models import Word, Definition, Example
from vocab.forms import AddExampleForm
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


def home(request):
    return render(request, 'vocab/home.html')


def word(request, word):
    w = Word.objects.filter(word=word).first()
    if w and w.word == word:
        defs = w.data[0]['shortdef']
        examples_qs = Example.objects.filter(word=w)
        examples = []
        for example in examples_qs:
            examples.append(example.text)
    else:
        r = requests.get(
            f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={settings.MW_DICT_API_KEY}')
        new_word = Word(word=word, data=r.json(), user=User.objects.first())
        new_word.save()
        defs = r.json()[0]['shortdef']
        for defn in defs:
            d = Definition(word=new_word, text=defn)
            d.save()
        examples = []

    if request.method == 'POST':
        form = AddExampleForm(request.POST)

        if form.is_valid():
            example_text = form.cleaned_data['text']
            example_source = form.cleaned_data['source']
            new_example = Example(word=w, text=example_text, source=example_source)
            new_example.save()
            return redirect(reverse('word', kwargs={'word': word}))
    else:
        form = AddExampleForm()

    context = {
        'word': word,
        'definitions': defs,
        'examples': examples,
        'form': form
    }

    return render(request, 'vocab/word.html', context)
