from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def create(request):
    pass

def detail(request):
    pass

def update(request):
    pass

def delete(request):
    pass