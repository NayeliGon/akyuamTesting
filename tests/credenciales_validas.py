from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


try:

    driver.get("http://127.0.0.1:8000/") 

    time.sleep(2)  
    username_input = driver.find_element(By.NAME, "username") 
    username_input.send_keys("prueba@gmail.com") 
    password_input = driver.find_element(By.NAME, "password") 
    password_input.send_keys("Akyuamprueba") 

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  
    login_button.click()


    time.sleep(3)  

    print("Título de la página después del inicio de sesión:", driver.title)
    
finally:
    driver.quit()
