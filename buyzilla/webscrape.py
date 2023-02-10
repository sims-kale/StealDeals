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
    
    driver.get(amz_link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(0)   # sleep_between_interactions
    amz_product = driver.find_element_by_id("productTitle").get_attribute('innerText')
    amz_price = driver.find_element_by_class_name("a-offscreen").get_attribute("innerText")
    # print(amz_product, amz_price)
    amz_img = (WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.a-list-item>span.a-declarative>div.imgTagWrapper>img.a-dynamic-image"))).get_attribute('src'))
    amz_rate = (WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.a-icon-row:nth-child(1)"))).get_attribute("innerText"))
    # amz_rate = driver.find_element_by_class_name("a-size-medium a-color-base a-text-beside-button a-text-bold").get_attibute("innerText")
    # driver.quit() 
    print(amz_rate)
    return [amz_link,amz_product, amz_price, amz_img, amz_rate]

def flipkartscrape(flip_link,driver):
    # c = Options()
    # c.add_argument("--headless")
    # driver = webdriver.Firefox(options=c)
    driver.get(flip_link)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # flipkart_product = (WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME,"B_NuCI"))).get_attribute('innerText'))
    flipkart_product = driver.find_element(By.CLASS_NAME,"B_NuCI").get_attribute("innerText")
    print(flipkart_product)
    flipkart_price = driver.find_element(By.CLASS_NAME, "_30jeq3._16Jk6d").get_attribute("innerText")
    print(flipkart_price)
    parent_element = (WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, '_3kidJX'))))
    img_element = parent_element.find_element_by_xpath('.//img')
    flip_img = img_element.get_attribute('src')
    flip_rate = (WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._3LWZlK"))).get_attribute("innerText"))

    print(flip_rate, "\n", flip_img)
    driver.quit()
 
    return [flip_link, flipkart_product,flipkart_price, flip_img, flip_rate]



