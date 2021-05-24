from django.shortcuts import render
from .models import GetWord
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup


class Create(CreateView):
   template_name = 'getwords/home.html'
   model = GetWord
   fields = ('spell',)
   success_url = reverse_lazy('get')


def getfunc(request):
    for post in GetWord.objects.all():
        spell = post.spell
    
    url = "https://ejje.weblio.jp/content/" 
    list=[]
    source = requests.get(url)
    source.encoding = source.apparent_encoding



    data = BeautifulSoup(source.text, "html.parser")
    explanation_list = data.select("td.content-explanation")

    for idx, txt in enumerate(explanation_list):
        list.append(explanation_list[idx].text)

    context = {'list': list,}
    return render(request, 'getwords/get.html', context)