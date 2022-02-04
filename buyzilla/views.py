from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def webscrape(request):
    return HttpResponse("<em>Scraper started</em>") 