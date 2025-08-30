# date : 2508300043
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 38.10564589500427
# generation time: 28.49951457977295
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def create_when_signed_out(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250830_004323_5531.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[2]/a').screenshot('test_script/scratch_exp/screenshots/click_20250830_004323_5465.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[2]/a').click()
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/button').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[1]/div/div[1]/div[2]/button').screenshot('test_script/scratch_exp/screenshots/assert_element_20250830_004323_9804.png')

