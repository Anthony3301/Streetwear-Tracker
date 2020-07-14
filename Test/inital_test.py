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
    main = WebDriverWait(browser,30).until(
        EC.presence_of_element_located((By.ID,"products-container"))
    )
    print("search complete")

except:
    browser.quit()

browser.quit()