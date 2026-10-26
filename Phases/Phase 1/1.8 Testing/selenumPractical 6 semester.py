from selenium import webdriver

driver = webdriver.Chrome()

# Open another website
driver.get("https://practice.expandtesting.com")

print("Page Title:", driver.title)

driver.quit()