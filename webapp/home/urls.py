from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('signup', views.signup, name='signin'),
    path('signin', views.signin, name='signin'),
]