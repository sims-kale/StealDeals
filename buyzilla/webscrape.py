from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape(amz_link,  flip_link):
    return amazonscrape(amz_link).append(flipkartscrape(flip_link))

def amazonscrape(amz_link):
    driver = webdriver.Firefox()
    driver.get(amz_link)
    amz_product = driver.find_element_by_id("productTitle").get_attribute('innerText')
    amz_price = driver.find_element_by_class_name("a-offscreen").get_attribute("innerText")
    print([amz_product,amz_price])
    return [amz_product,amz_price]

def flipkartscrape(flip_link):
    driver = webdriver.Firefox()
    driver.get(flip_link)
    flipkart_product = driver.find_element_by_class_name("B_NuCI").get_attribute("innerText")

    # flipkart_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "_30jeq3 _16Jk6d"))) #This is a dummy element
    # print(flipkart_element.__name__)
    flipkart_price = driver.find_element(By.CSS_SELECTOR(".30jeq3 _16Jk6d"))
    
    # print([flipkart_product,flipkart_price])
    # return [flipkart_product,flipkart_price]

scrape("https://www.amazon.in/Melomane-Melophones-Headphone-Power-Packed-Ergonomic/dp/B08PZ7KF2H/?_encoding=UTF8&pd_rd_w=FD54X&pf_rd_p=af3269f8-dfce-4b62-bd10-bf6b79632555&pf_rd_r=R8CZ6MA8X4V93BCFMH8F&pd_rd_r=ab8dce6d-28cb-47fd-9ed0-b04af5a051cb&pd_rd_wg=iArZu&ref_=pd_gw_unk&th=1",
"https://www.flipkart.com/teddy-sport-5-feet-pink-bear-gift-152-cm-pink/p/itm8e6ded7514591?pid=STFFKHJHM5REAWMH&lid=LSTSTFFKHJHM5REAWMHH6CZQW&marketplace=FLIPKART&store=tng%2Fclb%2Fxv3&srno=b_1_1&otracker=hp_reco_Trending%2BOffers_4_13.dealCard.OMU_cid%3AS_F_N_tng_clb_xv3__o_nb_mp_00b7091228__NONE_ALL%3Bnid%3Atng_clb_xv3_%3Bet%3AS%3Beid%3Atng_clb_xv3_%3Bmp%3AF%3Bct%3Ao%3B_6&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FC2_Trending%2BOffers_DESKTOP_HORIZONTAL_dealCard_cc_4_NA_view-all_6&fm=personalisedRecommendation%2FC2&iid=en_wbm96%2BtjEzINSJ0wV4FFJlVR0UoZdVvlFQmjKc59Ou8Rm%2Bh59n94g6WxyphVP5MwDARzhTkuG497jr0L%2FH6KaA%3D%3D&ppt=browse&ppn=browse&ssid=gkjh6kcqtc0000001644151178049")



a1 = "seema"
a1.getText()