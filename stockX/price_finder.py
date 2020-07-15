from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Users/antho/Documents/selenDriver/chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://stockx.com")

userInput = input()

try:
    search = WebDriverWait(browser,30).until(
        EC.presence_of_element_located((By.ID,"home-search"))
    )
    search.send_keys(userInput)
    search.send_keys(Keys.RETURN)

except:
    browser.quit()

try:
    #waits for the product container to be loaded
    main = WebDriverWait(browser,30).until(
        EC.presence_of_element_located((By.ID,"products-container"))
    )

    #checks if the number of results are present
    isResults = len(browser.find_elements_by_xpath("//*[@id='products-container']/div[1]/div/b")) > 0
    print(isResults)

    result = browser.find_element_by_xpath("//*[@id='products-container']/div[1]/div/b").text
    print(result)

    
except:
    browser.quit()