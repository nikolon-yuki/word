from django.urls import path
from .views import signupview, loginview, logoutview
from englishapp.views import IndexView

app_name='user'

urlpatterns = [
    path('signup/',signupview,name='signup'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    # path('list/',IndexView.as_view(), name='list'),
]