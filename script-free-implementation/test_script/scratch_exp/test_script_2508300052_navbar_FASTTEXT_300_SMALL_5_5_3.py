# date : 2508300052
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 37.6409227848053
# generation time: 27.53771734237671
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def create_when_signed_out(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250830_005238_9138.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[2]/a').screenshot('test_script/scratch_exp/screenshots/click_20250830_005238_4327.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[2]/a').click()
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/label/input').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]/div[1]/label/input').screenshot('test_script/scratch_exp/screenshots/assert_element_20250830_005238_8355.png')

