# date : 2508292327
# model: FASTTEXT_300_SMALL
# search width: 5
# beam width: 5
# text weight: 3
# model load time: 37.5964195728302
# generation time: 30.314009428024292
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep

def search_bar_test(driver):
    driver.get('http://localhost:8333')
    driver.implicitly_wait(10)
    driver.save_screenshot('test_script/scratch_exp/screenshots/open_20250829_232709_2768.png')
    driver.find_element(By.ID,'frc-q-1088').screenshot('test_script/scratch_exp/screenshots/enter_20250829_232709_4169.png')
    driver.find_element(By.ID,'frc-q-1088').clear()
    driver.find_element(By.ID,'frc-q-1088').send_keys('cat')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[6]/form/button').screenshot('test_script/scratch_exp/screenshots/click_20250829_232709_9312.png')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/ul/li[6]/form/button').click()
    assert driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div/h1/span').is_displayed()
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div/h1/span').screenshot('test_script/scratch_exp/screenshots/assert_element_20250829_232709_9335.png')

