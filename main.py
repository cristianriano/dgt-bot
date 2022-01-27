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
  sleep(1)
  select_option_in(driver, HTML_SELECT_TRAMITE_ID, TRAMITE)
  sleep(1)
  select_option_in(driver, HTML_SELECT_PAIS_ID, PAIS)
  sleep(1)

def check_limit_reached(driver: webdriver):
  if check_message(driver, By.TAG_NAME, 'body', LIMIT_REACHED_MSG):
    logging.error('You reached the limit of requests! Try later')
    exit(1)

def wait():
  logging.info("Waiting....")
  sleep(WAIT_BETWEEN_ATTEMPTS_IN_MIN * 60)

# First step. Choose office and procedure
def test_office_availability(driver: webdriver):
  fill_select_boxes(driver)
  click_recaptcha(driver)
  sleep(1)
  input()
  click_button(driver, 'Continuar')
  return not check_error_message(driver, OFFICE_FULL_MSG)

def fill_personal_data(driver: webdriver):
  # driver.
  1

def run():
  driver = init_driver()

  for i in range(MAX_ATTEMPTS):
    try:
      logging.info(f'Attempt #{i} in {OFICINA}')
      clean_cookies_and_session_data(driver)
      driver.get(BASE_URL)

      check_limit_reached(driver)
      if not test_office_availability(driver):
        wait()
        continue

      click_button(driver, 'Continuar')
      save_screenshot(driver, 'first-step')
      fill_personal_data()
      pdb.set_trace()
    except Exception as e:
      logging.error(e)
      wait()
      continue

  driver.quit()

if __name__ == '__main__':
  run()
