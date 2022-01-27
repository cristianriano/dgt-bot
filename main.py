from distutils.command.clean import clean
import logging
import constants

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def init_driver():
  logging.info('Initializing driver')
  webdriver.Chrome()

def clean_cookies_and_session_data(driver: webdriver):
  driver.delete_all_cookies()
  try:
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
  except Exception as e:
    logging.error(f'Error cleaning local storage: {e}')
    pass

driver = init_driver()
clean_cookies_and_session_data(driver)
driver.get(constants.BASE_URL)
