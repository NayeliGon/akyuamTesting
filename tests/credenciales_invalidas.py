from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importamos las opciones
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuramos las opciones para Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Modo headless
chrome_options.add_argument("--no-sandbox")  # Solución para algunos entornos de CI como Jenkins
chrome_options.add_argument("--disable-dev-shm-usage")  # Solución para sistemas con recursos limitados

service = Service(ChromeDriverManager().install())

# Inicializamos el navegador con las opciones
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://127.0.0.1:8000/")

    time.sleep(2)  
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("akyuam.cejav@yahoo.es")
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("akYu4m1021")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(3)

    print("Título de la página después del inicio de sesión:", driver.title)

finally:
    driver.quit()
