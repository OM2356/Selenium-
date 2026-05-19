from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Google Opened Successfully")

input("Press Enter to Close Browser...")

driver.quit()