from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestSauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)

    def test_empty_password(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("Tobeto")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
    
    def test_locked_out(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
    def test_inventory(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)

test = TestSauce()
test.test_invalid_login()
test.test_empty_password()
test.test_locked_out()
test.test_inventory()

