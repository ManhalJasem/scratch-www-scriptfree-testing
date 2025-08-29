# date : 2508271446
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 41.39968919754028
# generation time: 23.997161626815796
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def click_DSA_requirements_link(driver):
    driver.get('http://localhost:8333/')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250827_144651_3002.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div/div/dl[4]/dd[5]/a').screenshot('test_script/scratch_exp/screenshots/click_20250827_144651_9975.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/footer/div/div/dl[4]/dd[5]/a').click()
    assert 'DSA-PoC@scratch.org' in driver.page_source, 'string "DSA-PoC@scratch.org" is not exist'
    driver.save_screenshot('test_script/scratch_exp/screenshots/assert_string_20250827_144651_5029.png')

