from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  # Para presionar ENTER
from typing import Any, Dict
from appium.options.common import AppiumOptions

# 🔹 Configuración de Appium
cap: Dict[str, Any] = {
    "platformName": "Android",
    "platformVersion": "15",  # Ajusta según tu emulador/dispositivo
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appActivity": "com.google.android.apps.chrome.Main",
    "appPackage": "com.brave.browser",
    "autoGrantPermissions": True  # Otorga permisos automáticamente
}

# 🔹 URL del servidor Appium
url = 'http://localhost:4723'

try:
    # 🔹 Iniciar sesión en Appium
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    wait = WebDriverWait(driver, 10)  # Esperar hasta 10 segundos

    # 🔹 Aceptar botón de bienvenida si aparece
    try:
        btn_positive = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//android.widget.Button[@resource-id="com.brave.browser:id/btn_positive"]')
        ))
        btn_positive.click()
        print("✅ Botón de bienvenida aceptado.")
    except:
        print("ℹ️ No se encontró botón de bienvenida, continuando...")

    # 🔹 Hacer clic en la barra de búsqueda
    url_bar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@resource-id="com.brave.browser:id/url_bar"]')
    ))
    url_bar.click()
    print("✅ Barra de URL seleccionada.")

    # 🔹 Escribir "google.es" y presionar ENTER
    url_bar.send_keys("https://www.google.es")
    url_bar.send_keys(Keys.ENTER)
    print("✅ Navegando a Google España...")

    # 🔹 Esperar a que cargue Google y hacer clic en la barra de búsqueda de Google
    google_search_bar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.EditText[@name="q"]')  # Campo de búsqueda de Google
    ))
    google_search_bar.click()
    print("✅ Barra de búsqueda de Google seleccionada.")

    # 🔹 Escribir la búsqueda y presionar ENTER
    # 🔹 Escribir la búsqueda y presionar ENTER en un solo paso
    busqueda = "Appium con Python"
    google_search_bar.send_keys(busqueda + "\n")  # ENTER se envía con "\n"
    print(f"✅ Buscando: {busqueda}")

except Exception as e:
    print(f"⚠️ Error durante la ejecución: {e}")

finally:
    # 🔹 🚀 Mantener la sesión abierta hasta que el usuario presione Enter
    input("🔄 La sesión sigue abierta. Presiona Enter para salir...")

    # 🔹 Cerrar la sesión de Appium correctamente
    driver.quit()
