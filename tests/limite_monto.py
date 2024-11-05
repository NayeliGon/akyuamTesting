from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración del modo headless para evitar errores en Jenkins
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Configurar el servicio de ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("http://127.0.0.1:8000/")

    time.sleep(2)
    
    # Ingresar las credenciales válidas
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("prueba@gmail.com")
    
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Akyuamprueba")

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(3)

    # Imprimir el título de la página después del inicio de sesión
    print("Título de la página después del inicio de sesión:", driver.title)

finally:
    driver.quit()
