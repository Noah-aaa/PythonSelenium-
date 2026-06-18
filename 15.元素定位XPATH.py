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

# 复制谷歌浏览器 XPATH 也可以复制完整XPATH路径（通过属性+路径定位 如果属性是随机的，可能定位不到）
dr.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div/div[1]/div[4]/div[1]/div[2]/textarea').send_keys("人生苦短 我学python")



time.sleep(20)

# 关闭当前标签页
# dr.close()
# 退出浏览器并释放驱动
dr.quit()
