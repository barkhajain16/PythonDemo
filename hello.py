from selenium import webdriver
import sys
try:
    print("Opening browser")
    print(sys.path)
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.com")
    
    driver.close()
    driver.quit()

except:
    print("Hello")
