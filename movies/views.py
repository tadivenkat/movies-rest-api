from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

data = Movie.objects.all()

# return list of movies
def movies(request):
    return render(request, 'movies/movies.html', {'movies': data})

def home(request):
    return HttpResponse("Home Page")