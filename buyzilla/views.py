from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .webscrape import flipkartscrape,amazonscrape



def index(request):
    return render(request,'index.html')

@csrf_exempt 
def webscrape(request):
    if request.method == 'POST':
        amz_link = request.POST.get('amazon')
        flip_link = request.POST.get('flipkart')
        amz_prices = amazonscrape(amz_link)
        flip_prices = flipkartscrape(flip_link)
        return HttpResponse("<ol><li> Amazon product is "+amz_prices[0]+ "<br>" "price" +amz_prices[1]+ "</li>"
         "<li> Flipkart product is "+flip_prices[0]+ "<br>" "price" +flip_prices[1]+ "</li></ol>") 

    return HttpResponse("<em>Your product is added for tracking</em>") 