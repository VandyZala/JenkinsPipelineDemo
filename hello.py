print('Hello World')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://websites.co.in/login")
driver.maximize_window()
# time.sleep(10)
driver.find_element(By.ID, "email").send_keys("rdygxnoysm@exelica.com")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

if driver.title == "Welcome Subscribed User For Testing| Lets get you online.":
    print("Successful log in.")
else:
    print("Unsuccessful script.")
