from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

url = "https://search.informatica.com/KBSearch#t=KB&sort=relevancy&f:@athenaproduct=[Cloud%20Data%20Integration]"
browser = webdriver.PhantomJS("C://Python27//Scripts//phantomjs//bin//phantomjs.exe")
browser.get(url)

delay = 10 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'CoveoResultLink')))
except TimeoutException:
    print "Loading took too much time!"

list_of_elements = browser.find_elements_by_class_name('CoveoResultLink')

for element in list_of_elements:
    print element.get_attribute('href')


