from django.urls import path
from schedule import views

urlpatterns = [
    path('', views.home_sched, name='home_sched'),
]