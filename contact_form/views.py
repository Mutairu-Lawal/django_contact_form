from django.shortcuts import render
from django.views import View


def home(resquest):
    return render(resquest, 'index.html')
