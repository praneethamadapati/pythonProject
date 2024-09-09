import requests
from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('some url')
    element = driver.find_element_by_id('')
    print('', driver.title)

    response = requests.get('some url')
    if response.status_code == 200:
        data = response.json()
        print('', data)
    else:
        print('Failed')
finally:
    driver.quit()