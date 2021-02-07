from selenium import webdriver
web = webdriver.Chrome(r'd:chromedriver.exe')
web.implicitly_wait(5)
"""
web.get('http://cdn1.python3.vip/files/selenium/sample1.html')
elements = web.find_elements_by_class_name('animal')

for element in elements:
    print(element.text)
"""
web.get('https://www.baidu.com')
web.find_element_by_id('kw').send_keys('干饭')
web.find_element_by_id('su').click()

element = web.find_element_by_id('1')

print(element.get_attribute('outerHTML'))

web.quit()