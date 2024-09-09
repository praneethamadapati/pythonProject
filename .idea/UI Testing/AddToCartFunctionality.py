from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://www.apple.com/store')
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, 'globalnav-menubutton-link-search'))
search_box.click()

search_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.ID, 'globalnav-searchfield-src'))
search_input.send_keys('iPhone 14' + Keys.ENTER)

phone_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(By.PARTIAL_LINK_TEXT, 'iPhone 14'))
phone_item.click()

buy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Buy '))
buy.click()

phone_sub_category = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.ID, ':r7:_label'))
phone_sub_category.click()

color = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Midnight'))
color.click()

storage = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, '128'))
storage.click()

no_trade_in = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.ID, 'noTradeIn_label'))
no_trade_in.click()

payment_option = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Buy'))
payment_option.click()

connectivity = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Connect to any carrier later'))
connectivity.click()

apple_care_coverage = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, 'No AppleCare+ coverage'))
apple_care_coverage.click()

add_to_bag = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Add to Bag'))
add_to_bag.click()

item_add_confirmation = WebDriverWait.until(driver, 10).until(EC.visibility_of_element_located(By.CLASS_NAME, 'rc-summaryheader-left'))
assert 'iPhone 14 128GB Midnight' in item_add_confirmation.text
assert 'One-time payment' in item_add_confirmation.text

review_bag = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(By.LINK_TEXT, 'Review Bag'))
review_bag.click()



driver.quit()