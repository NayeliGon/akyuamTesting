from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar el servicio de ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://127.0.0.1:8000/") 

    # Espera para que la página cargue completamente
    time.sleep(2) 

    # Ingreso de credenciales
    username_input = driver.find_element(By.NAME, "username") 
    username_input.send_keys("prueba@gmail.com") 
    password_input = driver.find_element(By.NAME, "password") 
    password_input.send_keys("Akyuamprueba") 

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
    login_button.click()

    # Espera a que la página de inicio se cargue
    time.sleep(3) 
    print("Título de la página después del inicio de sesión:", driver.title)

    # Seleccionar "Calcular gastos de alimentación"
    calcular_gastos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'menu-item')]/p[text()='Calcular gastos de alimentación']"))
    )
    calcular_gastos_button.click()

    # Espera a que la página de "Calcular gastos de alimentación" cargue
    time.sleep(3)

    # Llenar el formulario de fechas y costo
    fecha_inicio_input = driver.find_element(By.NAME, "fecha_inicio")
    fecha_inicio_input.clear()  # Limpiar cualquier valor preexistente
    fecha_inicio_input.send_keys("01/01/2024")

    fecha_fin_input = driver.find_element(By.NAME, "fecha_fin")
    fecha_fin_input.clear()  # Limpiar cualquier valor preexistente
    fecha_fin_input.send_keys("31/01/2024")

    costo_comida_input = driver.find_element(By.NAME, "costo_comida")
    costo_comida_input.clear()  # Limpiar cualquier valor preexistente
    costo_comida_input.send_keys("50")

    # Hacer clic en el botón de "Buscar"
    buscar_button = driver.find_element(By.XPATH, "//button[text()='Buscar']")
    buscar_button.click()

    # Espera para ver el resultado (ajusta el tiempo si es necesario)
    time.sleep(3) 
    print("Búsqueda realizada. Título de la página actual:", driver.title)

finally:
    driver.quit()
