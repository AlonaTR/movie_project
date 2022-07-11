from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies, name='all_movies'),
    path('movie/<int:id_movie>', views.show_one_movie, name='one_movie'),    
    path('add_movie', views.add_movie, name='add_movie'),

]
