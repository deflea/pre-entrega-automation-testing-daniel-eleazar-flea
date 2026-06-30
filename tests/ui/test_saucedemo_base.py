import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def test_login(login_driver):
    logger.info("Ejecutando validación: Pantalla principal de productos (Login)")
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in login_driver.current_url
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo == 'Products'
    titulo_pagina = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"app_logo"))).text
    assert titulo_pagina == 'Swag Labs'
    logger.info("Validación de pantalla principal finalizada con éxito")


def test_menu_productos(login_driver):
    logger.info("Ejecutando validación: Despliegue de menú lateral de navegación")
    wait = WebDriverWait(login_driver, 10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_btn.click()
    menu_contenido = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "bm-item")))
    assert len(menu_contenido) == 4
    menu_cruz_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-cross-btn")))
    menu_cruz_btn.click()
    logger.info("Validación del menú completada con éxito")

def test_filtros_productos(login_driver):
    logger.info("Ejecutando validación: Filtro de productos")
    wait = WebDriverWait(login_driver, 10)
    filtros = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']")))
    opciones = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='product-sort-container'] option")))
    assert len(opciones) == 4
    logger.info("Validación finalizada con éxito")

def test_carrito_productos(login_driver):
    logger.info("Ejecutando validación: Carrito de compras")
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))
    logger.info("Validación finalizada con éxito")

def test_footer_productos(login_driver):
    logger.info("Ejecutando validaci+ón: Footer")
    wait = WebDriverWait(login_driver,10)
    footer_texto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='footer-copy']"))).text
    assert "Sauce Labs. All Rights Reserved." in footer_texto
    redes = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".social a")))
    assert len(redes) == 3
    logger.info("Validación finalizada con éxito")
    


def test_catalogo_productos(login_driver):
    logger.info("Ejecutando validación: Estructura y precios del catálogo principal")
    wait = WebDriverWait(login_driver, 10)
    titulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo == 'Products'
    productos = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test='inventory-list']")))
    assert len(productos) > 0
    primer_producto_nombre = productos[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']").text
    primer_producto_precio = productos[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-price']").text
    assert primer_producto_nombre == 'Sauce Labs Backpack'
    assert primer_producto_precio == '$29.99'
    logger.info("Validación del catálogo completada con éxito")

def test_logout(login_driver):
    logger.info("Ejecutando procedimiento: Cierre de sesión (Logout)")
    wait = WebDriverWait(login_driver,10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_btn.click()
    logout_btn = wait.until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link")))
    logout_btn.click()
    assert "https://www.saucedemo.com/" in login_driver.current_url
    logger.info("Cierre de sesión verificado con éxito")
