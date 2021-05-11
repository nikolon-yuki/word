from django.shortcuts import render
from django.views import generic
from .models import Word,Answer

# Create your views here.
class IndexView(generic.ListView):
    model = Answer
    paginate_by = 10
    template_name = 'englishapp/list.html'

    def get_queryset(self):
        return Answer.objects.order_by('-created_at')

class CategoryView(generic.ListView):
    model = Answer
    paginate_by = 10

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        queryset = Answer.objects.order_by('-created_at').filter(category_pk=category_pk)
        return queryset

class Detailview(generic.DeleteView):
    model = Answer