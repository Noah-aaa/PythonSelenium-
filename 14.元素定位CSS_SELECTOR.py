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

# 通过css选择器进行定位
# 1.#id=#+id值 通过id定位
dr.find_element(By.CSS_SELECTOR,"#chat-textarea").send_keys("person.akav.cn")
# 2..class = .+class值 通过class定位
dr.find_element(By.CSS_SELECTOR, ".btn")
# 3.不加修饰符 = 标签头
dr.find_elements(By.CSS_SELECTOR, "input")
# 4.通过任意类型定位： "[类型名字=‘精准值’]"
dr.find_element(By.CSS_SELECTOR, "[target='_blank']")
# 4.通过任意类型定位： "[类型名字*='模糊值']"
dr.find_element(By.CSS_SELECTOR, "[target*='_blank']")
# 4.通过任意类型定位： "[类型名字^='开头值']"
dr.find_element(By.CSS_SELECTOR, "[target^='_']")
# 4.通过任意类型定位： "[类型名字$='结尾值']"
dr.find_element(By.CSS_SELECTOR, "[target$='k']")

# 8.更简单的定位方式 谷歌控制台直接复制
dr.find_element(By.CSS_SELECTOR, "#chat-textarea").send_keys("你好 python")
time.sleep(20)

# 关闭当前标签页
# dr.close()
# 退出浏览器并释放驱动
dr.quit()
