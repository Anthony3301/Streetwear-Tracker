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

if EC.presence_of_element_located((By.CLASS_NAME,"BrowseSearchDescription__SearchConfirmation-sc-1mt8qyd-1 dcjzxm")):
    print("Item Located")
else:
    print("No Results")

browser.quit()