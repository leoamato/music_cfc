from django.urls import path
from songs import views

urlpatterns = [
    path('', views.songs_home, name='songs_home'),
    path('list/', views.song_list, name='songs_list'),
    path('add/', views.song_add, name='songs_add'),
    path('add_category/', views.add_category, name='add_category')
]