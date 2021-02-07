from selenium import webdriver
web = webdriver.Chrome(r'd:chromedriver.exe')
web.implicitly_wait(5)

web.get('http://cdn1.python3.vip/files/selenium/sample3.html')


link = web.find_element_by_tag_name("a")
link.click()

mainWindow = web.current_window_handle

for handle in web.window_handles:
    web.switch_to_window(handle)

    if 'Bing' in web.title:
        break

print(web.title)
web.find_element_by_id('sb_form_q').send_keys('干飯')

web.switch_to_window(mainWindow)

web.find_element_by_id('outerbutton').click()
#web.quit()