from distutils.command.clean import clean
import logging
import pdb

from constants import *
from html_utils import *
from selenium import webdriver
from selenium.webdriver.common.by import By

def init_driver():
  logging.info('Initializing driver')
  return webdriver.Chrome()

def clean_cookies_and_session_data(driver: webdriver):
  driver.delete_all_cookies()
  try:
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
  except Exception as e:
    logging.error(f'Error cleaning local storage: {e}')
    pass

def fill_select_boxes(driver: webdriver):
  select_option_in(driver, HTML_SELECT_OFICINAS_ID, OFICINA)
  select_option_in(driver, HTML_SELECT_TRAMITE_ID, TRAMITE)
  select_option_in(driver, HTML_SELECT_PAIS_ID, PAIS)

def run():
  try:
    driver = init_driver()
    clean_cookies_and_session_data(driver)
    driver.get(BASE_URL)

    fill_select_boxes(driver)
    click_recaptcha(driver)
    click_by(driver, By.CSS_SELECTOR, 'input[value="Continuar"]')

    pdb.set_trace()
    check_message(driver, By.CSS_SELECTOR, 'ul>li.msgError', 'robot')
  finally:
    driver.quit()

if __name__ == '__main__':
  run()
