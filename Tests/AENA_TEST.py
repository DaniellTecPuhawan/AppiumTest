from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any, Dict
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appActivity": "es.aena.mobile.ui.homeActivity.HomeActivity",
    "appPackage": "es.aena.mobile",
    "autoGrantPermissions": True
}

url = 'http://localhost:4723'

# Iniciar sesión en Appium
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

try:
    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos

    # 🔹 Hacer click en "Next page" tres veces
    element1 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//android.widget.Button[@content-desc='Next page']")
    ))
    element1.click()
    element1.click()
    element1.click()
    print("✅ ¡Click realizado tres veces en 'Next page'!")

    # 🔹 Hacer click en "Login with my user"
    element2 = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//android.widget.TextView[@content-desc='Login with my user. The login screen will open on a new page.']")
    ))
    element2.click()
    print("✅ ¡Click realizado en 'Login with my user'!")

    # 🔹 Escribir en el campo de correo electrónico
    email_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//android.widget.EditText[@resource-id='es.aena.mobile:id/et_fragment_log_in_acc_email']")
    ))
    email_input.send_keys("daniell.tec@entelgy.com")
    print("✅ ¡Correo electrónico ingresado!")

    # 🔹 Escribir en el campo de contraseña
    password_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//android.widget.EditText[@resource-id='es.aena.mobile:id/et_fragment_log_in_acc_pass']")
    ))
    password_input.send_keys("Arbust0@EN@1")
    print("✅ ¡Contraseña ingresada!")

    # 🔹 Hacer click en el botón de login
    login_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//android.widget.Button[@resource-id='es.aena.mobile:id/btn_fragment_log_in_acc']")
    ))
    login_button.click()
    print("✅ ¡Click realizado en el botón de login!")

except Exception as e:
    print(f"⚠️ Error durante la ejecución: {e}")

# 🔹 🚀 Mantener la sesión abierta (espera a que el usuario presione Enter)
input("🔄 La sesión sigue abierta. Presiona Enter para salir...")
