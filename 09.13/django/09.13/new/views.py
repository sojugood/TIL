from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def res(request):
    return render(request, 'new/res.html')