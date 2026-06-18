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
    # 启用无头模式
    # op.add_argument("--headless")
    # 创建并启动浏览器
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=op)
    return driver


dr = browse_setting()

# 打开指定网站
dr.get("https://www.baidu.com")

# 通过文本连接<a>标签的文本内容准确找到元素
# 可能是重复的，因此可能还需要切片等操作
values = dr.find_element(By.LINK_TEXT, "新闻")
values.click()
print(values)

time.sleep(20)

# 关闭当前标签页
# dr.close()
# 退出浏览器并释放驱动
dr.quit()
