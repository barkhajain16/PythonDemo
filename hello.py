from selenium import webdriver

try:
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://www.google.com")
    
    driver.close()
    driver.quit()

except:
    print("Hello")
