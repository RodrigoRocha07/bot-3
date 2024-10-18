from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import random
import string
import time
import subprocess
import requests
from fastapi import FastAPI, Path
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service) 


driver.get("https://betsalfa.vip/home?id=510015589&type=1&currency=BRL")
time.sleep(60)
#//*[@id="js_tabbarWraps"]/div[5]/div/strong/div/svg/path[2]
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[5]/div[2]/div[5]/div/strong/div/svg/path[1]"))
).click()

driver.quit()
