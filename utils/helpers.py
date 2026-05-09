from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    return driver

def login(driver, username, password):
    wait = WebDriverWait(driver,10)

    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    ).send_keys(password)

    wait.until(
        EC.presence_of_element_located((By.ID, "login-button"))
    ).click()
