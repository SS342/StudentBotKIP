# python 3.10.
# inst : allelleo
# project version 0.1
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
import datetime
import telebot
from schedule import every, repeat, run_pending
LOGIN = ''
PASSWORD = ''
MYTELEGRAMID = int("") # u telegram id
TOKEN = ''

def getDate():
    now = datetime.datetime.now()
    date = f"{'0' if int(now.day) < 10 else ''}{now.day}.{'0' if int(now.month) < 10 else ''}{now.month}"
    return date

def authorization(LOGIN, PASSWORD):
    driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[1]/div/input')[0].send_keys(LOGIN)
    driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[1]/div[2]/div/input')[0].send_keys(PASSWORD)
    driver.find_elements(By.XPATH, '/html/body/div/div/main/div/div/div/div/form/div[2]/button')[0].click() 
    time.sleep(2)

bot = telebot.TeleBot(TOKEN)


options = Options()
#options.headless = True
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(executable_path=r'C:\Users\alex2\Desktop\MNSK_v1\geckodriver.exe', options=options)
driver.get('https://kip.eljur.ru/')
time.sleep(2)
authorization(LOGIN, PASSWORD)
driver.find_elements(By.XPATH, '//*[@id="layout"]/div[2]/header/div/div/div[1]/nav/div/a[1]')[0].click()

days = {
    1 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div/div[1]",
    2 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div[1]",
    3 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div[1]/div",
    4 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div[1]/div",
    5 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[6]/div[1]/div",
    6 : "/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div[3]/div[6]/div[1]"
}


def main():
    lessons = ""
    day : int = -1
    if getDate() in (driver.find_elements(By.XPATH, days[1])[0].text): day = 1
    elif getDate() in (driver.find_elements(By.XPATH, days[2])[0].text): day = 2
    elif getDate() in (driver.find_elements(By.XPATH, days[3])[0].text): day = 3
    elif getDate() in (driver.find_elements(By.XPATH, days[4])[0].text): day = 4
    elif getDate() in (driver.find_elements(By.XPATH, days[5])[0].text): day = 5
    elif getDate() in (driver.find_elements(By.XPATH, days[6])[0].text): day = 6
    if day == -1 :
        day = 7
    try:
        message = driver.find_elements(By.XPATH, "/html/body/div[1]/nav[2]/div[2]/div/div[2]/a[1]/div")[0].text
    except: message = 0
    try:
        lessons = driver.find_elements(By.CLASS_NAME, 'dnevnik-day')[day-1].text
    except:
        if day == 7 :
            lessons = ("Выходной!!")
    
    print(lessons)
    print(message)
 
main()
