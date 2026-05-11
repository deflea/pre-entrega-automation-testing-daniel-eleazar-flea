from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto(login_driver):
    #Agrego el primer producto al carrito
    wait = WebDriverWait(login_driver,10)
    agregar_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    agregar_btn.click()
    #Valido que aparezca el botón 'Remover' y que haya aumentado el numero en el carrito
    wait.until(EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
    badge = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")))
    assert badge.text == "1"

    #Redirijo al carrito y valido producto agregado
    badge.click()
    assert "cart.html" in login_driver.current_url
    titulo_carrito = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo_carrito == "Your Cart"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-quantity-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-desc-label']")))
    producto_nombre = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-name']"))).text
    assert producto_nombre == "Sauce Labs Backpack"
    producto_precio = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='inventory-item-price']"))).text
    assert "$29.99" in producto_precio
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='inventory-item']")))
    wait.until(EC.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
    wait.until(EC.visibility_of_element_located((By.ID,"continue-shopping")))

    #Redirijo a la proxima pantalla, completo los campos
    checkout_btn = wait.until(EC.visibility_of_element_located((By.ID,"checkout")))
    checkout_btn.click()
    assert "checkout-step-one.html" in login_driver.current_url
    titulo_checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo_checkout == "Checkout: Your Information"
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
    wait.until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("Doe")
    wait.until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys("123")
    wait.until(EC.visibility_of_element_located((By.ID,"cancel")))

    #Redirijo a la pantalla de confirmacion, valido los datos del producto
    continuar_btn = wait.until(EC.visibility_of_element_located((By.ID,"continue")))
    continuar_btn.click()
    assert "checkout-step-two.html" in login_driver.current_url
    titulo_checkout_overview = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo_checkout_overview == "Checkout: Overview"
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-quantity-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='cart-desc-label']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='inventory-item']")))
    total_seccion = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-info-label']"))).text
    item_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='subtotal-label']"))).text
    impuesto_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='tax-label']"))).text
    precio_total = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='total-label']"))).text
    assert total_seccion == "Price Total"
    assert "$29.99" in item_total
    assert "$2.40" in impuesto_total
    assert "$32.39" in precio_total
    wait.until(EC.visibility_of_element_located((By.ID,"cancel")))

    #Redirijo a la pantalla de finalizacion del pedido, valido el mensaje y redirijo a pantalla principal
    finalizar_btn = wait.until(EC.visibility_of_element_located((By.ID,"finish")))
    finalizar_btn.click()
    assert "checkout-complete.html" in login_driver.current_url
    titulo_checkout_complete = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='title']"))).text
    assert titulo_checkout_complete == "Checkout: Complete!"
    finalizar_texto = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-test='complete-header']"))).text
    assert "Thank you for your order!" in finalizar_texto
    atras_btn = wait.until(EC.visibility_of_element_located((By.ID, "back-to-products")))
    atras_btn.click()
    assert "inventory.html" in login_driver.current_url

