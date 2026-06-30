import logging
import os
import pytest
from utils.helpers import get_driver, login

logging.getLogger("webdriver_manager").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    logger.info("=== INICIANDO INSTANCIA DEL NAVEGADOR ===")
    driver = get_driver()
    yield driver
    logger.info("Cerrando instancia del navegador...")
    driver.quit()
    logger.info("=== INSTANCIA DEL NAVEGADOR CERRADA ===")

@pytest.fixture
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture
def login_driver(driver, base_url):
    logger.info(f"Navegando a la URL base del sistema: {base_url}")
    driver.get(base_url)
    logger.info("Ejecutando proceso automatizado de Login")
    login(driver, "standard_user", "secret_sauce")
    logger.info("Sesión iniciada correctamente. Redirigiendo a las pruebas")
    return driver


def pytest_html_report_title(report):
    report.title = "API - UI Pytest Selenium"



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("login_driver")
        
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test '{item.name}' FALLÓ. Captura de pantalla guardada en: {screenshot_path}")