from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

quotes = driver.find_elements(By.CLASS_NAME, "text")

for q in quotes:
    print(q.text)

driver.quit()