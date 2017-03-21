# python
#coding=utf-8
from appium import webdriver
from time import sleep
import unittest
# 配置web driver并启动webview应用
browser_caps = {}
browser_caps['platformName'] = 'Android'
browser_caps['platformVersion'] = '4.4.2'
browser_caps['deviceName'] = 'Android Emulator'
browser_caps['browserName'] = 'Browser'

driver = webdriver.Remote('http://localhost:4723/wd/hub', browser_caps)

# 跳转到指定页面并在该页面所以用元素id进行交互
driver.get('http://saucelabs.com/test/guinea-pig');
div = driver.find_element_by_id('i_am_an_id')
# 检查文本是否符合预期

assertEqual('I am a div', div.text)

# 通过id查找评论框并输入
driver.find_element_by_id('comments').send_keys('My comment')

# 关闭应用
driver.quit()
