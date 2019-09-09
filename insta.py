import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/kadri/Desktop/pycharm/chromedriver/chromedriver');
driver.get('https://www.instagram.com/accounts/login/');
driver.find_element_by_name('username').send_keys('vision_of_mate');
driver.find_element_by_name('password').send_keys('lost24/7');
driver.find_element_by_css_selector('.L3NKy').click();
time.sleep(5);
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/button[1]').click();
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys("#photography");
time.sleep(3);
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER);

#driver.find_element_by_css_selector('.glyphsSpriteSafari__outline__24__grey_9').click();
#question=BeautifulSoup("#loginForm > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(1) > span:nth-child(1)").contents.copy();

#print(question);/html/body/div[2]/div/div/div[3]/button[1]
