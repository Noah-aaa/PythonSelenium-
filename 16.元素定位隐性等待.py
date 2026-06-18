import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动
from selenium.webdriver.common.by import By



def browse_setting():
    # 创建设置浏览器对象
    op = Options()
    # 禁用沙盒模式(增加系统兼容性)
    op.add_argument('--no-sandbox')
    # 保持浏览器打开状态(默认是代码执行完毕自动关闭)
    op.add_experimental_option('detach', True)
    # 创建并启动浏览器
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=op)
    return driver


dr = browse_setting()
dr.get("https://person.akav.cn")
# 元素定位隐性等待(多少秒内找到元素，没有找到元素就报错)
dr.implicitly_wait(10)
dr.find_element(By.XPATH,"/html/body/div").click()

dr.quit()