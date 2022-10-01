from django.shortcuts import render
# Create your views here.
def index(responce):
    return render(responce, 'site/index.html')
