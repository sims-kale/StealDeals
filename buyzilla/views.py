from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .webscrape import scrape


def index(request):
    return render(request,'index.html')

@csrf_exempt 
def webscrape(request):
    if request.method == 'POST':
        amz_link = request.POST.get('amazon')
        flip_link = request.POST.get('flipkart')
        prices = scrape(amz_link, flip_link)
        return HttpResponse("<ol> <li>Amazon product is "+prices[0]+ "</li>" "<li>Amazon price is "+prices[1]+"</li>") 

    return HttpResponse("<em>Your product is added for tracking</em>") 