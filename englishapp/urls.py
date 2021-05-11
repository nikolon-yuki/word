from django.urls import path
from . import views

app_name = 'englishapp'

urlpatterns = [
    path('',views.IndexView.as_view(), name = 'index'),
    path('category/<int:pk>/',views.CategoryView.as_view(), name='category'),
    path('detail_<int:pk>/',views.Detailview.as_view(),name='detail'),
    path('wordregistration', views.wordregistration, name="wordregistration"),
]