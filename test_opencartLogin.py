from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import pytest
from databaseOperations import *

class Test_Opencart:
    def setup_method(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://localhost/opencart/upload/")

    def teardown_method(self):
        self.driver.close()

    @pytest.mark.parametrize("email , password" ,getUserInfo())
    def test_loginOperation(self,email,password):
        myAccountBtn = self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/div/a/span")
        myAccountBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a")))
        userLoginBtn = self.driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[2]/a")
        userLoginBtn.click()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[1]/input")))
        emailInput = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[1]/input")
        emailInput.send_keys(email)
        passwordInput = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[2]/input")
        passwordInput.send_keys(password)
        sleep(2)
        loginBtn = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/div[2]/div/form/div[3]/button")
        loginBtn.click()
        sleep(2)
        contentText = self.driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/h2[1]")
        assert contentText.text == "Hesabım"