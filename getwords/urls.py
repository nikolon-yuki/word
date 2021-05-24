from django.urls import path
from .views import Create, getfunc

app_name='getwords'

urlpatterns = [
   path('create/', Create.as_view(), name='home'),
   path('get/', getfunc, name='get'),
]