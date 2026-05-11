from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto(login_driver):
    #Agrego el primer producto al carrito
    wait = WebDriverWait(login_driver,10)
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_btn.click()
    #Valido que aparezca el botón 'Remover' y que haya aumentado el numero en el carrito
    wait.until(EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
    badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")))
    assert badge.text == "1"

    #Redirijo al carrito y valido producto agregado
    badge.click()
    assert "cart.html" in login_driver.current_url
    title_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert title_cart == "Your Cart"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-quantity-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-desc-label']")))
    product_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']"))).text
    assert product_name == "Sauce Labs Backpack"
    product_price = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-price']"))).text
    assert "$29.99" in product_price
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='inventory-item']")))
    wait.until(EC.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
    wait.until(EC.visibility_of_element_located((By.ID,"continue-shopping")))

    #Redirijo a la proxima pantalla, completo los campos
    checkout_btn = wait.until(EC.visibility_of_element_located((By.ID,"checkout")))
    checkout_btn.click()
    assert "checkout-step-one.html" in login_driver.current_url
    title_checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert title_checkout == "Checkout: Your Information"
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
    wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Doe")
    wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("123")
    wait.until(EC.visibility_of_element_located((By.ID,"cancel")))

    #Redirijo a la pantalla de confirmacion, valido los datos del producto
    continue_btn = wait.until(EC.visibility_of_element_located((By.ID,"continue")))
    continue_btn.click()
    assert "checkout-step-two.html" in login_driver.current_url
    title_checkout_overview = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert title_checkout_overview == "Checkout: Overview"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-quantity-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-desc-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='inventory-item']")))
    total_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-info-label']"))).text
    item_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='subtotal-label']"))).text
    tax_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='tax-label']"))).text
    price_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))).text
    assert total_section == "Price Total"
    assert "$29.99" in item_total
    assert "$2.40" in tax_total
    assert "$32.39" in price_total
    wait.until(EC.visibility_of_element_located((By.ID,"cancel")))

    #Redirijo a la pantalla de finalizacion del pedido, valido el mensaje y redirijo a pantalla principal
    finish_btn = wait.until(EC.visibility_of_element_located((By.ID,"finish")))
    finish_btn.click()
    assert "checkout-complete.html" in login_driver.current_url
    title_checkout_complete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert title_checkout_complete == "Checkout: Complete!"
    finish_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='complete-header']"))).text
    assert "Thank you for your order!" in finish_text
    back_btn = wait.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    back_btn.click()
    assert "inventory.html" in login_driver.current_url

