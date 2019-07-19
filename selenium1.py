from selenium import webdriver
import time

driver_path = '/home/rain/my_soft/chromedriver'  # 谷歌浏览器驱动路径
browser = webdriver.Chrome(driver_path)

time.sleep(1)

browser.get('http://www.baidu.com')
browser.save_screenshot('baidu.png')  # 保存浏览器快照，会显示浏览器访问过程

browser.quit()　  # 千万记得退出
