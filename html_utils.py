import logging

from constants import *
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

def list_all_select_options(driver: webdriver, id: str):
  select_element = Select(driver.find_element(By.ID, id))

  for opt in select_element.options:
    print(opt.get_attribute('text'))


def select_option_in(driver: webdriver, id: str, text: str):
  element = Select(driver.find_element(By.ID, id))
  element.select_by_visible_text(text)


def click_button(driver: webdriver, label: str):
  try:
    driver.find_element(By.CSS_SELECTOR, f'inpput[value="{label}"]').click()
  except NoSuchElementException as e:
    logging.warning(f"Can't click Button \"{label}\". Not found")
    raise e


def check_message(driver: webdriver, criteria: By, query: str, text: str):
  try:
    return EC.text_to_be_present_in_element((criteria, query), text)(driver)
  except NoSuchElementException:
    logging.warning(f'"{query}" element not found')
    return False

def check_error_message(driver: webdriver, text: str):
  return check_message(driver, By.CSS_SELECTOR, ERROR_MESSAGE_SELECTOR, text)

def save_screenshot(driver: webdriver, name: str):
  driver.save_screenshot(f'{name}-{datetime.now()}.png'.replace(":", "-"))

def click_recaptcha(driver: webdriver):
  try:
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))
    check_box = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, HTML_RECAPTCHA_BOX_ID))
    )

    sleep(0.5)
    check_box.click()
    sleep(2)
  except TimeoutException as e:
    logging.error(e)
  finally:
    driver.switch_to.default_content()
