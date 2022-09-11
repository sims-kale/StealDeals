from fileinput import filename
from gettext import gettext
from lib2to3.pgen2 import driver
import time
from tkinter import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

# def scrape(amz_link,  flip_link):
#return amazonscrape(amz_link),flipkartscrape(flip_link)

def amazonscrape(amz_link,driver):
    # driver = webdriver.Firefox()
    # c = Options()
    # c.add_argument("--headless")
    # driver = webdriver.Firefox(options=c)
    
    #passing headless parameter
    
    driver.get(amz_link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(0)   # sleep_between_interactions
    amz_product = driver.find_element_by_id("productTitle").get_attribute('innerText')
    amz_price = driver.find_element_by_class_name("a-offscreen").get_attribute("innerText")
    # amz_img = (WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.a-list-item>span.a-declarative>div.imgTagWrapper>img.a-dynamic-image"))).get_attribute('src'))
    # driver.quit()
    # print([amz_img])
    return [amz_product, amz_price]

def flipkartscrape(flip_link,driver):
    # c = Options()
    # c.add_argument("--headless")
    # driver = webdriver.Firefox(options=c)
    driver.get(flip_link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    flipkart_product = driver.find_element_by_class_name("B_NuCI").get_attribute("innerText")
    # flipkart_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_30jeq3 _16Jk6d"))) #This is a dummy element
    # print(flipkart_element.__name__)
    flipkart_price = driver.find_element(By.CLASS_NAME, "_16Jk6d").get_attribute("innerText")
    driver.quit()
    #print([flipkart_product,flipkart_price])
    return [flipkart_product,flipkart_price]

