from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from .models import Movie

# data = {
#   'movies': [
#     {
#         'id' : 5,
#         'title': 'Jaws',
#         'year': 1669
#     },
#     {
#         'id' : 6,
#         'title': 'Sharknado',
#         'year': 1669
#     },
#     {
#         'id' : 7,
#         'title': 'The Meg',
#         'year': 2000
#     },
#   ]
# }


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies' : data} ) 

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request,'movies/detail.html',{'movie': data}) 

def add(request):
    # data = Movie.objects.all()
    title = request.POST.get('title')
    year = request.POST.get('year')

    print (title, year)

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return redirect('movies')

    return render(request, 'movies/add.html') 

def delete(request,id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return redirect('movies')


