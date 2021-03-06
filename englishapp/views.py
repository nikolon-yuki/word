from django.shortcuts import render
from django.views import generic
from .models import Word,Answer
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import RegistrationForm,InquiryForm
# from . import forms


class IndexView(generic.ListView):
    model = Answer
    paginate_by = 10
    template_name = 'englishapp/list.html'

    def get_queryset(self):
        query = super().get_queryset()
        question = self.request.GET.get('question',None)
        if question:
            query=query.filter(
                question=question
            )
        return query
        # return Answer.objects.order_by('-created_at')

# class CategoryView(generic.ListView):
#     model = Answer
#     paginate_by = 10

#     def get_queryset(self):
#         category_pk = self.kwargs['pk']
#         queryset = Answer.objects.order_by('-created_at').filter(category_pk=category_pk)
#         return queryset

class FormView(FormView):
    template_name = 'englishapp/form.html'
    form_class = InquiryForm


class Detailview(generic.DeleteView):
    model = Answer

def wordregistration(request):
    if(request.method == 'POST'):
        regi_question = request.POST['question']
        regi_answer = request.POST['answer']
        # regi_category = request.POST['category']
        exist = Answer.objects.filter(question=regi_question)
        if(len(exist) == 0):
            mw = Answer()
            mw.question = regi_question
            mw.answer = regi_answer
            # mw.category = regi_category
            mw.save()
            messages.success(request, '登録しました。')
        else:
            messages.error(request, '登録できませんでした')

    form = RegistrationForm()

    params = {
        'form':form,
    }

    return render(request, 'englishapp/registration.html', params)
 