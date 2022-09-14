from inspect import formatannotationrelativeto
from django.http import HttpResponse
from django.shortcuts import render
from selenium import webdriver
from django.views.decorators.csrf import csrf_exempt
from .webscrape import flipkartscrape,amazonscrape
from .dbhandler import readIntoDatabase, writeIntoDatabase
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
        c.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(chrome_options = c, executable_path= "C:/drivers/chromedriver.exe")
    


        amz_prodcut = amazonscrape(amz_link, driver)
        flip_prodcut = flipkartscrape(flip_link, driver)
        writeIntoDatabase(amz_prodcut ,flip_prodcut )
        dict={}
        count =0
        for row in readIntoDatabase():
            dict[count] = row
            count +=1
        
        return render(request, 'dashboard.html' , {"contex": dict })
    # return HttpResponse("<em>Your product is added for tracking</em>")
def dashboard(request):
    dict={}
    counter =0
    for row in readIntoDatabase():
        dict[counter]=row
        counter+=1
     
    return render(request, 'dashboard.html',{"contex": dict})
       
