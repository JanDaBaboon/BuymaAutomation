from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import keyboard
from openpyxl import workbook, load_workbook


#-----------------------------------------------------------------------------
#temp code
def pause():
    while True:
        if keyboard.read_key() == 'space':
            break
        
           
        
#-----------------------------------------------------------------------------
#information for website, driver, and xlsx
url = "https://www.buyma.com/login/"
url2 = "https://www.buyma.com/my/sell/new?tab=b"
driver = webdriver.Chrome(executable_path="./chromedriver")
wb = load_workbook(r"C:\Users\junya\Desktop\BuymaAutomation\xlsx\inventory_data.xlsx")
ws = wb["inventory_data_sheet"]
image_location = r"C:\Users\junya\Desktop\BuymaAutomation\images\Malta Gown\img(101).jpg"

#selection elements in order of uses for different input elements
login_id = "txtLoginId"
password_id = "txtLoginPass"
submit_element_id = "login_do"
skip_button_class = "driver-close-btn"
drag_image_xpath = "/html/body/div[3]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/form/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/input"


#-----------------------------------------------------------------------------
#Functions for navigation

def Login(input, id):
    field = driver.find_element(By.ID, id)
    for x in input :
        field.send_keys(x)
    return driver

#Clicking function that clicks on specificied ID
def Click_ID(id) :
    driver.find_element(By.ID, id).click()
    return driver

def Click_Class(class_id) :
    driver.find_element(By.CLASS_NAME, class_id).click()
    return driver
    

def Upload_Photo_xPath(xPath) :
    driver.find_element(By.XPATH, xPath).send_keys(image_location)
    return driver

def AccessSheet(sheet) :
    for col in sheet.iter_cols(min_row=2, max_col=1, max_row=10):
        for cell in col:
            if cell.value != None :
                print (cell.value)
            

# -----------------------------------------------------------------------------
# Order of operations

driver.get(url)    
driver.maximize_window()

Login("kokomimi.buyma@gmail.com", login_id)

Login("koko12345", password_id)

Click_ID(submit_element_id)

driver.get(url2)

Click_Class(skip_button_class)

AccessSheet(ws)

Upload_Photo_xPath(drag_image_xpath)




pause()
time.sleep(1)




