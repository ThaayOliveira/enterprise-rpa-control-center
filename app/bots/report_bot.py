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

     # configuração para Render
    if os.getenv("RENDER"):
        options.binary_location = "/usr/bin/chromium"
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
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

        mensagem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text.strip()

        nome = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = f"reports/login_{nome}.png"

        driver.save_screenshot(caminho)

        return {
            "status": "success",
            "message": mensagem
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        driver.quit()