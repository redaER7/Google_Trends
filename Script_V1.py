

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import codecs

####################################################################################
url='https://trends.google.com/trends/?geo=US'

chrome_driver_binary = "/usr/local/bin/chromedriver"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-dev-shm-usage')

#chrome_options.binary_location = "/usr/bin/google-chrome"

#driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome(chrome_driver_binary, options=chrome_options)

driver.get(url)
time.sleep(np.random.randint(8,15))
driver.save_screenshot('screen0.png')
####################################################################################
search_box = driver.find_element_by_id('input-1')

keyword_1 = 'Tensorflow'
search_box.send_keys(keyword_1)
search_box.send_keys(Keys.ENTER)
time.sleep(np.random.randint(8,15))

driver.save_screenshot('screen1.png')


compare = driver.find_element_by_xpath("//button[@class='compare-term-container add-term-button pill-outline md-button md-ink-ripple']")
compare.click()
time.sleep(2)
driver.save_screenshot('screen2.png')


search_box_2 = driver.find_element_by_id('input-52')
keyword_2 = 'Keras'
search_box_2.send_keys(keyword_2)
search_box_2.send_keys(Keys.ENTER)
time.sleep(np.random.randint(8,15))


#action = webdriver.ActionChains(driver)
#action.move_to_element(compare).click().perform()

driver.save_screenshot('screen3.png')

####################################################################################
f = codecs.open("page_source.txt", "w", "utf−8")
h = driver.page_source
f.write(h)
#
#
#
#
#
#
#
#