from django.shortcuts import render
from .models import GetWord
# from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import InputWordsForm


# class Create(CreateView):
#    template_name = 'getwords/home.html'
#    model = GetWord
#    fields = ('spell',)
#    success_url = reverse_lazy('list')




def inputwords(request):
    if(request.method == 'POST'):
        spell = request.POST['spell']
        exist = GetWord.objects.filter(spell=spell)
        # if(len(exist) == 0):
        mw = GetWord()
        mw.spell = spell
        mw.save()
        #     messages.success(request, '登録しました。')
        # else:
        #     messages.error(request, '登録できませんでした')

    form = InputWordsForm()

    params = {
        'form':form,
    }

    return render(request, 'getwords/inputwords.html', params)





def getfunc(request):
    for i in GetWord.objects.all():
        spell = i.spell

    # spell = GetWord.objects.all()
    list=[]
    # spells = []
    
    url = "https://ejje.weblio.jp/content/" + str(spell)

    source = requests.get(url)
    source.encoding = source.apparent_encoding

    data = BeautifulSoup(source.text, "html.parser")
    explanation_list = data.select("td.content-explanation")

    for tag in explanation_list:
        word = tag.getText()
        list.append(word)

    spell = (spell)

    context = {'list':list,'spell':spell,}
    return render(request, 'getwords/get.html', context)