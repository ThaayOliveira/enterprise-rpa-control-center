import logging
import os
from datetime import datetime

import app.utils.logger

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

def run_report_bot():
    logging.info("Bot Selenium iniciado")

    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless=new")  #  para rodar sem abrir navegador

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        # Aguarda campo usuário aparecer
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys("tomsmith")

        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Aguarda mensagem de sucesso
        mensagem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        ).text.strip()

        # Screenshot com timestamp
        nome_arquivo = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho = f"reports/login_{nome_arquivo}.png"
        driver.save_screenshot(caminho)

        logging.info("Login realizado com sucesso")
        logging.info(f"Screenshot salva em {caminho}")

        return {
            "status": "success",
            "message": mensagem
        }

    except Exception as e:
        logging.error(f"Falha no bot Selenium: {str(e)}")

        return {
            "status": "error",
            "message": str(e)
        }

    finally:
        driver.quit()