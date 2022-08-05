from inspect import formatannotationrelativeto
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .webscrape import flipkartscrape,amazonscrape
from .dbhandler import writeIntoDatabase




def index(request):
    return render(request,'index.html')

@csrf_exempt 
def webscrape(request):
    
    if request.method == 'POST':
        amz_link = request.POST.get('amazon')
        flip_link = request.POST.get('flipkart')
        amz_prices = amazonscrape(amz_link)
        flip_prices = flipkartscrape(flip_link)
        writeIntoDatabase(amz_link,flip_link,amz_prices,flip_prices)
        
        return render(request, 'dashboard.html')
    # return HttpResponse("<em>Your product is added for tracking</em>")
