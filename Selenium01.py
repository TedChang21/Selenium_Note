from selenium import webdriver

web = webdriver.Chrome(r'd:\chromedriver.exe')
web.get('https://www.yahoo.com/')
element = web.find_element_by_id('ybar-sbq')
#element.send_keys('game stop\n')
element.send_keys('game stop')
element = web.find_element_by_id('ybar-search')
element.click()
pass