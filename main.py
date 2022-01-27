import logging
import pdb

from constants import *
from html_utils import *
from sys import exit
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

def check_limit_reached(driver: webdriver):
  if check_error_message(driver, LIMIT_REACHED_MSG):
    logging.error('You reached the limit of requests! Try later')
    exit(1)

def wait():
  logging.info("Waiting....")
  sleep(WAIT_BETWEEN_ATTEMPTS_IN_MIN * 60)

# First step. Choose office and procedure
def test_office_availability(driver: webdriver):
  fill_select_boxes(driver)
  click_recaptcha(driver)
  click_by(driver, By.CSS_SELECTOR, 'input[value="Continuar"]')
  return not check_error_message(driver, OFFICE_FULL_MSG)

def run():
  try:
    driver = init_driver()

    for i in range(MAX_ATTEMPTS):
      logging.info(f'Attempt #{i}')
      clean_cookies_and_session_data(driver)
      driver.get(BASE_URL)

      check_limit_reached(driver)
      if not test_office_availability(driver):
        wait()
        continue
      else:
        pdb.set_trace()

  finally:
    driver.quit()

if __name__ == '__main__':
  run()
