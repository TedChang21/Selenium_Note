from selenium import webdriver
web = webdriver.Chrome(r'd:chromedriver.exe')
web.implicitly_wait(5)
"""
web.get('http://cdn1.python3.vip/files/selenium/sample1a.html)
elements = web.find_elements_by_class_name('animal')

for element in elements:
    print(element.text)
"""
web.get('http://cdn1.python3.vip/files/selenium/sample2.html')
web.switch_to.frame(web.find_element_by_css_selector('iframe[src="sample1.html"]'))

#elements = web.find_elements_by_css_selector('span:nth-child(2)')
#elements = web.find_elements_by_css_selector('#t1 > :nth-child(2)')
#elements = web.find_elements_by_css_selector('p:nth-last-child(1)')
#elements = web.find_elements_by_css_selector('span:nth-of-type(2)')
#elements = web.find_elements_by_css_selector('#t2 p:nth-of-type(even)')
#elements = web.find_elements_by_css_selector('#t1 h3 ~ span')
elements = web.find_elements_by_css_selector('.plant')
for element in elements:
    print('------------------------')
    print(element.get_attribute('outerHTML'))
web.switch_to_default_content()
web.find_element_by_id('outerbutton').click()

#web.quit()