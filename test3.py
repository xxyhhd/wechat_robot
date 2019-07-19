from selenium import webdriver
import time
# from selenium .webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

# chrome_path = '/usr/bin/google-chrome-stable'  # 本地chrome位置，因为已经添加到path,所以不需要
# chrome_options.binary_location = chrome_path
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/rain/my_soft/chromedriver')

# url = 'www.baidu.com'
browser.get('https://www.baidu.com')
button = browser.find_element_by_id('su')
print(button.tag_name)
browser.quit()

# 12
# from selenium import webdriver
  
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox') # 这个配置很重要
# client = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/chromedriver')    # 如果没有把chromedriver加入到PATH中，就需要指明路径
  
# client.get("https://www.baidu.com")
# print (client.page_source.encode('utf-8'))
  
# client.quit()