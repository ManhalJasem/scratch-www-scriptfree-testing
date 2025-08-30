# date : 2508282354
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 36.27895212173462
# generation time: 23.440442085266113
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def featured_studios_link(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250828_235412_6255.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/img').screenshot('test_script/scratch_exp/screenshots/click_20250828_235412_9009.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[2]/div/img').click()
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[4]/div[1]/div[1]').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[4]/div[1]/div[1]').screenshot('test_script/scratch_exp/screenshots/assert_element_20250828_235412_9217.png')

