from appium import webdriver
from selenium.webdriver.common.by import By

from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap:Dict[str, Any] = {
  "platformName": "Android",
  "platformVersion": "15",
  "deviceName": "emulator-5554",
  "automationName": "UiAutomator2",
  "appium:appActivity": "com.android.calculator2.Calculator",
  "appium:appPackage": "com.google.android.calculator"
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)

driver.find_element(By.ID, "com.google.android.calculator:id/digit_5").click()

driver.find_element(By.ID, "com.google.android.calculator:id/op_mul").click()

driver.find_element(By.ID, "com.google.android.calculator:id/digit_5").click()

driver.find_element(By.ID, "com.google.android.calculator:id/eq").click()

