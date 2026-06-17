# 元素输入
# 元素
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
dr.get("https://www.bilibili.com")

# 元素定位通过CLASS_NAME classnamevalue值不能有空格 如果有两个类名 只需要其中一个就好了
elements = dr.find_elements(By.CLASS_NAME, "channel-link")
print(elements)  # 有多个重复元素需要切片处理
# 有的网站class值是随机 无法定位
elements[0].click()






time.sleep(20)

# 关闭当前标签页
# dr.close()
# 退出浏览器并释放驱动
dr.quit()
