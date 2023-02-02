from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard

def pause():
    while True:
        if keyboard.read_key() == 'space':
            break
        
        
        
        
        

#information for website and driver
url = "https://www.buyma.com/login/"
url2 = "https://www.buyma.com/my/sell/new?tab=b"
driver = webdriver.Chrome(executable_path="./chromedriver")

#selection elements in order of uses for different input elements
login_id = "txtLoginId"
password_id = "txtLoginPass"
submit_element_id = "login_do"
skip_button_class = "driver-close-btn"


#Function for logging in. Used for both email and password.
def Login(input, id):
    field = driver.find_element(By.ID, id)
    for x in input :
        field.send_keys(x)
    return driver

#Clicking function that clicks on specificied ID
def Click_ID(id) :
    driver.find_element(By.ID, id).click()
    return driver

def Click_Class(id) :
    driver.find_element(By.CLASS_NAME, id).click()
    return driver
    

driver.get(url)    

Login("kokomimi.buyma@gmail.com", login_id)

Login("koko12345", password_id)

Click_ID(submit_element_id)

driver.get(url2)

Click_Class(skip_button_class)


pause()
time.sleep(5)




