from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F
from .forms import NewForm

def show_all_movies(request):
    movies =Movie.objects.order_by(F('rating').asc())    
    return render(request, 'movie_app/all_movies.html', {'movies':movies})

def show_one_movie(request, id_movie):
    movie = get_object_or_404(Movie, id=id_movie)
    return render(request, 'movie_app/one_movie.html', {'movie':movie})

def add_movie(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'movie_app/one_movie.html', {'movie':form.cleaned_data})
    else:
        form = NewForm()
    return render(request, 'movie_app/add_movie.html', {'form':form})