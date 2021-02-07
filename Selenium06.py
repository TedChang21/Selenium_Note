from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
web = webdriver.Chrome(r'd:chromedriver.exe')
web.implicitly_wait(5)
"""
web.get('http://cdn1.python3.vip/files/selenium/test2.html')

element = web.find_element_by_css_selector('#s_radio input[checked="checked"]')
print('當前選中的是:  '+ element.get_attribute('value'))
web.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()
"""
"""
elements = web.find_elements_by_css_selector('#s_checkbox input[checked="checked"]')

for element in elements:
    element.click()

web.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()
"""
"""
select = Select(web.find_element_by_id("ss_single"))
select.select_by_visible_text("小雷老师")
"""
"""
select = Select(web.find_element_by_id("ss_multi"))
select.deselect_all()

select.select_by_visible_text("小雷老师")
select.select_by_visible_text("小江老师")
"""

"""
web.get('http://www.baidu.com/')
ac = ActionChains(web)
ac.move_to_element(web.find_element_by_css_selector('[name="tj_briicon"]')).perform()
"""

web.get('http://cdn1.python3.vip/files/selenium/test4.html')
web.find_element_by_id('b1').click()
print(web.switch_to.alert.text)
web.switch_to.alert.accept()

web.find_element_by_id('b2').click()
print(web.switch_to.alert.text)
web.switch_to.alert.accept()
web.find_element_by_id('b2').click()
web.switch_to.alert.dismiss()

web.find_element_by_id('b3').click()
print(web.switch_to.alert.text)
alert = web.switch_to.alert
alert.dismiss()
web.find_element_by_id('b3').click()
alert = web.switch_to.alert
alert.send_keys('web automation - sleenium')
alert.accept()

#web.quit()