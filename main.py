from selenium import webdriver  # 导入驱动
from selenium.webdriver.common.by import By
# 建立第一个脚本 script

def first_script():
    driver = webdriver.Chrome()
    driver.get("https://wenda.zhihuishu.com/stu/courseInfo/studyResource?courseId=10869286")
    title = driver.title
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(By.CSS_SELECTOR, "continue-study-btn")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    driver.quit()

if __name__ == '__main__':
    first_script()
