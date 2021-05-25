from django.urls import path
from .views import inputwords, getfunc

app_name='getwords'

urlpatterns = [
   path('inputwords/', inputwords, name='inputwords'),
   path('get/', getfunc, name='list'),
]