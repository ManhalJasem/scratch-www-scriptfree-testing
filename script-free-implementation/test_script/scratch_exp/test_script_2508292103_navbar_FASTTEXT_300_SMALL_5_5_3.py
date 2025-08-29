# date : 2508292103
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 37.93582344055176
# generation time: 14.019301652908325
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def search_bar_test(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250829_210332_5448.png')
    driver.find_element(By.ID,'frc-q-1088').screenshot('test_script/scratch_exp/screenshots/enter_20250829_210332_3223.png')
    driver.find_element(By.ID,'frc-q-1088').clear()
    driver.find_element(By.ID,'frc-q-1088').send_keys('cat')
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[6]/form/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[6]/form/button').screenshot('test_script/scratch_exp/screenshots/assert_element_20250829_210332_5707.png')

