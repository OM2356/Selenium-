from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.python.org")

print("Website Title:")
print(driver.title)

driver.quit()