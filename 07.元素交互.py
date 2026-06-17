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
dr.get("https://www.baidu.com")

# 定位一个元素 通过ID找
chat_input_area = dr.find_element(By.ID, value="chat-textarea")
# 元素清空内容
chat_input_area.clear()
time.sleep(1)
# 元素输入
chat_input_area.send_keys("伊朗最新状况")
# 查找到一个按钮
chat_submit_button = dr.find_element(By.ID, value="chat-submit-button")
chat_submit_button.click()
chat_submit_button.submit()




time.sleep(20)

# 关闭当前标签页
# dr.close()
# 退出浏览器并释放驱动
dr.quit()
