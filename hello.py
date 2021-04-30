from selenium import webdriver
from selenium.webdriver.chrome.options import Options
try:
    print("Opening browser")
    options = Options()
    options.headless=True
    driver = webdriver.Chrome("chromedriver.exe",chrome_options=options)
    driver.get("https://www.google.com")
    print(driver.title)
    driver.close()
    driver.quit()

except:
    print("Hello")
