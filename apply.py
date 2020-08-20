import argparse
import time  # to sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DELAY = 60  # seconds
URL = 'http://192.168.31.1/'


def fill_password(driver, password):
    input_password = driver.find_element_by_xpath('//*[@id="password"]')
    input_password.send_keys(password)
    input_password.send_keys(Keys.RETURN)


def restart_router(driver):
    WebDriverWait(driver, DELAY).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="statusInternet"]/b')))
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="sysmenu"]').click()
    WebDriverWait(driver, DELAY).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="toReboot"]')))
    driver.find_element_by_xpath('//*[@id="toReboot"]').click()
    WebDriverWait(driver, DELAY).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="rebootAction"]')))
    driver.find_element_by_id('rebootAction').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[3]/div/a[2]').click()  # NO
    # driver.find_element_by_xpath(
    #     '/html/body/div[1]/div/div[3]/div/a[1]').click()  # YES
    time.sleep(5)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('password', help='mi router password')
    return parser.parse_args()


def main():
    args = parse_args()
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get(URL)
    fill_password(driver, args.password)
    restart_router(driver)
    driver.close()


if __name__ == '__main__':
    main()
