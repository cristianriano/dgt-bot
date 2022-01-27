from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def list_all_select_options(driver: webdriver, id: str):
  select_element = Select(driver.find_element(By.ID, id))

  for opt in select_element.options:
    print(opt.get_attribute('text'))