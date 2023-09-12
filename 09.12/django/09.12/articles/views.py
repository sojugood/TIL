from django.shortcuts import render
import datetime
# Create your views here.

x = datetime.datetime(2020, 2, 2, 14, 2, 0)
menus = ['치킨', '피자', '햄버거']

def index(request):
    return render(request, 'articles/index.html', {'today':x, 'menus':menus})