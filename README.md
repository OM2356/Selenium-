# 🚀 Selenium Automation Project

<div align="center">

# 🤖 Selenium Python Automation

✨ Browser Automation Using Selenium & Python ✨

</div>

---

# 📂 Project Structure

```bash
Selenium/
│
├── open_google.py
├── search_youtube.py
├── get_title.py
├── get_data.py
├── requirements.txt
│
└── screenshots/
```

---

# 🎯 About Project

This project demonstrates basic browser automation using Selenium WebDriver.

You will learn how to:

✅ Open websites automatically  
✅ Search on YouTube  
✅ Get webpage titles  
✅ Extract webpage data  
✅ Take screenshots using Selenium  

Perfect for beginners learning Web Automation 🤖

---

# ⚙️ Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
```

Or manually install Selenium:

```bash
pip install selenium
```

---

# 📄 requirements.txt

```txt
selenium
```

---

# ▶️ Run Python Files

## Open Google

```bash
python open_google.py
```

## Search on YouTube

```bash
python search_youtube.py
```

## Get Website Title

```bash
python get_title.py
```

## Extract Data

```bash
python get_data.py
```

---

# 🧠 Example Codes

---

## 📌 open_google.py

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Google Opened Successfully")

driver.quit()
```

---

## 📌 search_youtube.py

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.youtube.com")

time.sleep(2)

search = driver.find_element(By.NAME, "search_query")

search.send_keys("Python Selenium Tutorial")

search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
```

---

## 📌 get_title.py

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print("Website Title:", driver.title)

driver.quit()
```

---

## 📌 get_data.py

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com")

quotes = driver.find_elements(By.CLASS_NAME, "text")

for quote in quotes:
    print(quote.text)

driver.quit()
```

---

# 📸 Screenshots Folder

The `screenshots/` folder can be used to save automated screenshots.

Example:

```python
driver.save_screenshot("screenshots/google.png")
```

---

# 🌟 Features

✨ Browser Automation  
✨ YouTube Search Automation  
✨ Data Scraping  
✨ Screenshot Capture  
✨ Beginner Friendly  
✨ Real Browser Interaction  

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python 🐍 | Programming Language |
| Selenium 🤖 | Browser Automation |
| ChromeDriver 🌐 | WebDriver |

---

# 🔥 Future Improvements

- Add login automation
- Add Instagram automation
- Add WhatsApp automation
- Add headless browser mode
- Add automatic screenshot capture
- Add web scraping projects

---

# 📌 Important Note

Make sure:

✅ Google Chrome is installed  
✅ ChromeDriver version matches your Chrome browser version  

---

<div align="center">

# ⭐ Star This Project If You Like It ⭐

Made with ❤️ by Omkar Sathe

</div>
