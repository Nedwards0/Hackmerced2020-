import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://mystudentrecord.ucmerced.edu/pls/PROD/xhwschedule.p_selectsubject')
time.sleep(2) # Let the user actually see something!
viewclass = driver.find_element_by_xpath("//input[@type='radio' and @value='202010']")
viewclass.click()
time.sleep(2)
viewclass = driver.find_element_by_xpath("//input[@type='radio' and @value='N']")
viewclass.click()
time.sleep(2)
viewclass = driver.find_element_by_xpath("//input[@type='submit' and @value='View Class Schedule']")
viewclass.click()
#viewclass.submit()
time.sleep(2) # Let the user actually see something!
table_rows = driver.find_elements_by_xpath("//tr")
print(len(table_rows))
print(table_rows[0])
driver.quit()