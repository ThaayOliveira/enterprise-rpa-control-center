import os
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


def run_report_bot():
    os.makedirs("reports", exist_ok=True)

    options = Options()
    options.add_argument("--window-size=1920,1080")

    options.add_argument("--headless=new")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-password-manager-reauthentication")

    # CONFIG PRODUÇÃO (Render)
    if os.getenv("RENDER"):
        options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service("/usr/bin/chromedriver")

    # CONFIG LOCAL
    else:
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    try:
        driver.execute_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """)

        driver.get("https://the-internet.herokuapp.com/login")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("tomsmith")

        driver.find_element(By.ID, "password").send_keys(
            "SuperSecretPassword!"
        )

        driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/secure")
        )

        nome = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = f"reports/login_{nome}.png"
        driver.save_screenshot(caminho)

        logging.info("Report bot executado com sucesso")

        return {
            "status": "success",
            "message": "Report Bot executado com sucesso"
        }

    except Exception as e:
        logging.error(str(e))

        return {
            "status": "error",
            "message": "Erro ao executar o Report Bot"
        }

    finally:
        driver.quit()