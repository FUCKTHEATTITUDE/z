import sys
import subprocess
from importlib.resources import path
import threading
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.options import Options
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException



from cgitb import reset
import secrets
import time
import gspread
import colorama
from colorama import Fore, Back, Style
print(Style.BRIGHT + Fore.RESET + "Welcome To Ramgadiya Program")
print(Style.BRIGHT + Fore.RESET +
      "Contact us on Whatsapp For Software Activation +91 8059199600")
print(Style.BRIGHT + Fore.RESET +
      "Visit Site for More detail https://ramgadiya.com")
colorama.init(autoreset=True)

config = configparser.ConfigParser()
config.read('config.ini')
PROXY = []
with open("ip.txt", "r") as ip:
    for i in range(30):
        PROXY.append(ip.readline())

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument(f'user-agent={user_agent}')
options.add_experimental_option("detach", True)
options.add_argument("--window-size=1920,1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-infobars")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--use-fake-device-for-media-stream")
options.add_argument("--start-maximized")

count = 0
number = 2
meet_code = '3069823402'
passcode = 'WARP1d'
sec = 100




lis = []
with open("name.txt", 'r') as f:
    for i in range(51000):
        lis.append(f.readline())


n = 0
def fun(n, count):
    p = PROXY[count]
    if p is not None:
        options.add_argument(f"--proxy-server={p}")
    driver = webdriver.Chrome('chromedriver', options=options)
    return driver

def driver_wait(driver, locator, by, secs=1, condition=ec.element_to_be_clickable):
    wait = WebDriverWait(driver=driver, timeout=secs)
    element = wait.until(condition((by, locator)))
    return element
    
    driver.get(f'https://zoom.us/wc/join/{meet_code}')
    time.sleep(3)
    inp = driver.find_element(By.ID, 'inputname')
    time.sleep(1)
    inp.send_keys(f"{user}")
    btn2 = driver.find_element(By.ID, 'joinBtn')
    btn2.click()
    time.sleep(2)
    inp2 = driver.find_element(By.ID, 'inputpasscode')
    time.sleep(1)
    inp2.send_keys(passcode)
    btn3 = driver.find_element(By.ID, 'joinBtn')
    time.sleep(1)
    btn3.click()

    count += 1
    if count == 30:
        count = 0
    # n+=1
    # time.sleep(2)


while n < number:
    a = threading.Thread(target=fun, args=(n, count,))
    a.start()
    n += 1
    time.sleep(20)

input()
