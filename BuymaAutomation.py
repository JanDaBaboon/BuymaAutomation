from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#information for website and driver
url = "https://www.buyma.com/login/"
driver = webdriver.Chrome(executable_path="./chromedriver")

#opens the website
driver.get(url)

#ids for different input elements
login_id = "txtLoginId"
password_id = "txtLoginPass"
submit_element_id = "login_do"

#Function for logging in. Used for both email and password.
def Login(input, id):
    field = driver.find_element(By.ID, id)
    for x in input :
        field.send_keys(x)
    return driver

#Clicking function that clicks on specificied ID
def Click(id) :
    driver.find_element(By.ID, id).click()
    return driver
    

Login("kokomimi.buyma@gmail.com", login_id)
Login("koko12345", password_id)
Click(submit_element_id)
time.sleep(5)