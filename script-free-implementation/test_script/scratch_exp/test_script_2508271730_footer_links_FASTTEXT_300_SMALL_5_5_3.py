# date : 2508271730
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 39.875285387039185
# generation time: 24.416807174682617
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def click_DSA_requirements_link(driver):
    driver.get('http://localhost:8333/')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250827_173032_8635.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div/div/dl[4]/dd[5]/a').screenshot('test_script/scratch_exp/screenshots/click_20250827_173032_6907.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div/div/dl[4]/dd[5]/a').click()
    assert 'DSA-PoC@scratch.org' in driver.page_source, 'string "DSA-PoC@scratch.org" is not exist'
    driver.save_screenshot('test_script/scratch_exp/screenshots/assert_string_20250827_173032_2516.png')

