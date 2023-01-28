from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.buyma.com/login/"
driver = webdriver.Chrome(executable_path="./chromedriver")


driver.get(url)

login_id = "txtLoginId"
password_id = "txtLoginPass"
submit_element_id = "login_do"

def Login(input, id):
    field = driver.find_element(By.ID, id)
    for x in input :
        field.send_keys(x)
    return driver

def Click(id) :
    driver.find_element(By.ID, id).click()
    return driver
    


Login("kokomimi.buyma@gmail.com", login_id)
Login("koko12345", password_id)
Click(submit_element_id)
time.sleep(5)