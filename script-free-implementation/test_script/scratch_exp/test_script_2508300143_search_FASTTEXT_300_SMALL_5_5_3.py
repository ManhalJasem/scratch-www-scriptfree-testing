# date : 2508300143
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 40.76490139961243
# generation time: 28.215623140335083
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def switching_to_studios_maintains_search_string(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250830_014342_2622.png')
    driver.find_element(By.ID,'frc-q-1088').screenshot('test_script/scratch_exp/screenshots/enter_20250830_014342_8949.png')
    driver.find_element(By.ID,'frc-q-1088').clear()
    driver.find_element(By.ID,'frc-q-1088').send_keys('100% pen')
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/nav/div/ul/li[6]/form/button').screenshot('test_script/scratch_exp/screenshots/click_20250830_014342_2692.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/nav/div/ul/li[6]/form/button').click()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div[2]/div/button[2]').screenshot('test_script/scratch_exp/screenshots/click_20250830_014342_2449.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div/div/div[2]/div/button[2]').click()

