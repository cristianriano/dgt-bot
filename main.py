from distutils.command.clean import clean
import logging
import dgt_utils

from constants import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys

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

def run():
  try:
    driver = init_driver()
    clean_cookies_and_session_data(driver)
    driver.get(BASE_URL)

    dgt_utils.select_option_in(driver, HTML_SELECT_OFICINAS_ID, OFICINA)
    dgt_utils.select_option_in(driver, HTML_SELECT_TRAMITE_ID, TRAMITE)
    dgt_utils.select_option_in(driver, HTML_SELECT_PAIS_ID, PAIS)
  finally:
    driver.quit()

if __name__ == '__main__':
  run()
