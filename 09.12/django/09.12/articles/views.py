from django.shortcuts import render

# Create your views here.

def index(request):
    print("1")
    context = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    return render(request, 'articles/index.html', context)