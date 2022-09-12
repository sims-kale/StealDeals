from inspect import formatannotationrelativeto
from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from django.views.decorators.csrf import csrf_exempt
from .webscrape import flipkartscrape,amazonscrape
from .dbhandler import writeIntoDatabase
from selenium.webdriver.chrome.options import Options

def index(request):
    return render(request,'index.html')

@csrf_exempt 
def webscrape(request):

    
    if request.method == 'POST':
        amz_link = request.POST.get('amazon')
        flip_link = request.POST.get('flipkart')
        c = webdriver.ChromeOptions()
        # c.add_argument("--headless")
        c.add_argument("--ignore-certificate-error")
        c.add_argument("--ignore-ssl-errors")
        driver = webdriver.Chrome(chrome_options = c, executable_path= "C:/chromedriver.exe")
        
        amz_prices = amazonscrape(amz_link, driver)
        flip_prices = flipkartscrape(flip_link, driver)
        writeIntoDatabase(amz_link,flip_link,amz_prices,flip_prices)
        return render(request, 'dashboard.html',{"contex": dashboard,  })
    # return HttpResponse("<em>Your product is added for tracking</em>")
def dashboard(request):
    return render (request, 'dashboard.html')
    