from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(login_driver):
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in login_driver.current_url
    title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']")))
    title = title_element.text
    assert title == 'Products'
    page_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"app_logo"))).text
    assert page_text == 'Swag Labs'


def test_menu_productos(login_driver):
    wait = WebDriverWait(login_driver, 10)
    menu_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
    menu_btn.click()
    menu_content = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "bm-item")))
    assert len(menu_content) == 4
    menu_cross_btn = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-cross-btn")))
    menu_cross_btn.click()

def test_filtros_productos(login_driver):
    wait = WebDriverWait(login_driver, 10)
    filters = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-sort-container']")))
    options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='product-sort-container'] option")))
    assert len(options) == 4

def test_carrito_productos(login_driver):
    wait = WebDriverWait(login_driver,10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-link']")))

def test_footer_productos(login_driver):
    wait = WebDriverWait(login_driver,10)
    footer_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='footer-copy']"))).text
    assert "Sauce Labs. All Rights Reserved." in footer_text
    socials = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".social a")))
    assert len(socials) == 3


def test_catalogo_productos(login_driver):
    wait = WebDriverWait(login_driver, 10)
    title_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert title_element == 'Products'
    products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"[data-test='inventory-list']")))
    assert len(products) > 0
    first_product_name = products[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-name']").text
    first_product_price = products[0].find_element(By.CSS_SELECTOR,"[data-test='inventory-item-price']").text
    assert first_product_name == 'Sauce Labs Backpack'
    assert first_product_price == '$29.99'
