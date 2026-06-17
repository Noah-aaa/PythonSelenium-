from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理谷歌驱动

# 创建设置浏览器对象
op = Options()
# 禁用沙盒模式(增加系统兼容性)
op.add_argument('--no-sandbox')
# 保持浏览器打开状态(默认是代码执行完毕自动关闭)
op.add_experimental_option('detach', True)

# 创建并启动浏览器
driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=op)




