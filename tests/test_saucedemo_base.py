from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(login_driver):
    #Valida que estoy en la pantalla principal, utiliza el fixture login_driver
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in login_driver.current_url
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo == 'Products'
    titulo_pagina = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"app_logo"))).text
    assert titulo_pagina == 'Swag Labs'


def test_menu_productos(login_driver):
    #Valida menu lateral en pantalla principal
    wait = WebDriverWait(login_driver, 10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_btn.click()
    menu_contenido = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "bm-item")))
    assert len(menu_contenido) == 4
    menu_cruz_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-cross-btn")))
    menu_cruz_btn.click()

def test_filtros_productos(login_driver):
    #Valida filtros en pantalla principal
    wait = WebDriverWait(login_driver, 10)
    filtros = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']")))
    opciones = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='product-sort-container'] option")))
    assert len(opciones) == 4

def test_carrito_productos(login_driver):
    #Valida logo carrito en pantalla principal
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))

def test_footer_productos(login_driver):
    #Valida el footer de la pantalla principal
    wait = WebDriverWait(login_driver,10)
    footer_texto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='footer-copy']"))).text
    assert "Sauce Labs. All Rights Reserved." in footer_texto
    redes = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".social a")))
    assert len(redes) == 3


def test_catalogo_productos(login_driver):
    #Valida que se visualicen los productos en la pantalla principal
    wait = WebDriverWait(login_driver, 10)
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo == 'Products'
    productos = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test='inventory-list']")))
    assert len(productos) > 0
    primer_producto_nombre = productos[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']").text
    primer_producto_precio = productos[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-price']").text
    assert primer_producto_nombre == 'Sauce Labs Backpack'
    assert primer_producto_precio == '$29.99'

def test_logout(login_driver):
    #Valida cierre de sesion
    wait = WebDriverWait(login_driver,10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_btn.click()
    logout_btn = wait.until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))
    logout_btn.click()
    assert "https://www.saucedemo.com/" in login_driver.current_url
