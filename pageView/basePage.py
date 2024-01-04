import datetime
import time
import logging
import allure

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.all_path import picturePath


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 封装定位元素
    def find_element(self, *locator, doc=""):
        """
        查找单个元素方法
        :type doc : 定位元素界面位置：例如：首页
        :type locator: 元素定位，如（By.ID, "kw"）
        """
        try:
            logging.info("在{} 页面开始查找元素{}".format(doc, locator))
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
            ele = self.driver.find_element(*locator)
            logging.info("在{} 页面查找元素{}成功！".format(doc, locator))
            return ele
        except Exception as e:
            logging.error("在{} 定位元素 {}出现未知错误！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def find_elements(self, *locator, doc=""):
        """
        查找多个元素方法
        """
        try:
            logging.info("在{} 页面开始查找一组元素{}".format(doc, locator))
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
            ele = self.driver.find_elements(*locator)
            logging.info("在{} 页面查找元素{}成功！".format(doc, locator))
            return ele
        except Exception as e:
            logging.error("在{} 页面定位元素 {}出现未知错误！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def click_element(self, *locator, doc=""):
        """
        元素点击方法
        """
        ele = self.find_element(*locator, doc=doc)
        try:
            logging.info("在{} 页面点击元素{}".format(doc, locator))
            ele.click()
            logging.info("在{} 页面点击元素{}成功！".format(doc, locator))
        except Exception as e:
            logging.error("在{} 页面点击元素 {} 失败！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def send_keys(self, *locator, doc="", value):
        """
        元素输入方法
        """
        ele = self.find_element(*locator, doc=doc)
        try:
            logging.info("在{} 页面输入框输入{}".format(doc, locator))
            ele.send_keys(value)
            logging.info("在{} 页面输入框输入{}成功！".format(doc, locator))
        except Exception as e:
            logging.error("在{} 页面定位元素 {}出现未知错误！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def is_toast_exist(self, text, doc=""):
        """
        判断toast是否存在
        :param doc:
        :param text: toast的部分内容
        :return: True or False
        """
        try:
            toast_loc = (MobileBy.XPATH, ".//*[contains(@text,'%s')]" % text)
            logging.info("在{} 页面开始查找 toast {}".format(doc, text))
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(toast_loc))
            logging.info("在{} 页面查找 toast {}成功！".format(doc, text))
            return True
        except Exception as e:
            logging.error("在{} 页面查找 toast {}未出现！ 错误为：{}".format(doc, text, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            return False

    def is_element_exist(self, *locator, doc=""):
        """
        判断元素是否存在
        """
        try:
            logging.info("在{} 页面开始查找元素{}".format(doc, locator))
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(locator))
            logging.info("在{} 页面查找元素{}成功！".format(doc, locator))
            return True
        except Exception as e:
            logging.error("在{} 页面定位元素 {}出现未知错误！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            return None

    def get_text(self, *locator, doc=""):
        """
        获取文本方法
        """
        ele = self.find_element(*locator, doc=doc)
        try:
            logging.info("在{} 页面开始获取 {} 文本".format(doc, locator))
            text = ele.text
            logging.info("在{} 页面获取文本 {}成功！".format(doc, locator))
            return text
        except Exception as e:
            logging.error("在{} 页面定位元素 {}出现未知错误！ 错误为：{}".format(doc, locator, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def get_texts(self, *locators, doc=""):
        """
        获取多个文本方法
        """
        try:
            logging.info("在{} 页面开始获取文本 {}".format(doc, locators))
            texts = [self.find_element(*locator, doc=doc).text for locator in locators]
            logging.info("在{} 页面获取文本 {} 成功！".format(doc, locators))
            return texts
        except Exception as e:
            logging.error("在{} 页面定位元素 {} 出现未知错误！ 错误为：{}".format(doc, locators, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            # 在实际应用中，你可能需要根据你的需求进行错误处理或者抛出异常
            raise

    def get_size(self):
        """
        获取屏幕大小
        :return: 屏幕大小
        """
        try:
            logging.info("开始获取设备屏幕大小")
            size = self.driver.get_window_size()
            width = size.get("width")
            height = size.get("height")
            logging.info("获取设备屏幕大小完成。{} {}".format(width, height))
            return width, height
        except Exception as e:
            logging.error("获取设备屏幕大小失败！ 错误为：{}".format(e))
            return None

    def swipe_to_left(self, doc=""):
        """
        左滑屏幕
        :param doc:
        :return:
        """
        width, height = self.get_size()
        try:
            logging.info("{} 开始左滑屏幕".format(doc))
            self.driver.swipe(width * 0.9, height * 0.5, width * 0.1, height * 0.5, 1000)
            logging.info("{} 左滑屏幕成功".format(doc))
            time.sleep(1)
        except Exception as e:
            logging.error("{} 左滑屏幕失败！ 错误为：{}".format(doc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_right(self, doc=""):
        """
        右滑屏幕
        :param doc:
        :return:
        """
        width, height = self.get_size()
        try:
            logging.info("{} 开始右滑屏幕".format(doc))
            self.driver.swipe(width * 0.1, height * 0.5, width * 0.9, height * 0.5, 1000)
            logging.info("{} 右滑屏幕成功".format(doc))
            time.sleep(1)
        except Exception as e:
            logging.error("{} 右滑屏幕失败！ 错误为：{}".format(doc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_up(self, doc=""):
        """
        上滑屏幕
        :param doc:
        :return:
        """
        width, height = self.get_size()
        try:
            logging.info("{} 开始上滑屏幕".format(doc))
            self.driver.swipe(width * 0.5, height * 0.9, width * 0.5, height * 0.1, 1000)
            logging.info("{} 上滑屏幕成功".format(doc))
            time.sleep(1)
        except Exception as e:
            logging.error("{} 上滑屏幕失败！ 错误为：{}".format(doc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def swipe_to_down(self, doc=""):
        """
        下滑屏幕
        :param doc:
        :return:
        """
        width, height = self.get_size()
        try:
            logging.info("{} 开始下滑屏幕".format(doc))
            self.driver.swipe(width * 0.5, height * 0.1, width * 0.5, height * 0.9, 1000)
            logging.info("{} 下滑屏幕成功".format(doc))
            time.sleep(1)
        except Exception as e:
            logging.error("{} 下滑屏幕失败！ 错误为：{}".format(doc, e))
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))

    def hide_keyboard(self):
        """
        隐藏键盘
        :return:
        """
        try:
            logging.info("开始隐藏键盘")
            self.driver.hide_keyboard()
            logging.info("隐藏键盘成功")
        except Exception as e:
            logging.error("隐藏键盘失败！ 错误为：{}".format(e))

    def get_screenshot(self, doc):
        """
        截图
        :param doc:
        :return:
        """
        logging.info("开始截图..")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
        pic_name = picturePath + r"\{}".format(doc) + now + ".png"
        self.driver.get_screenshot_as_file(pic_name)
        logging.info("截图成功，图片为：{}".format(pic_name))
        with open(pic_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, doc, allure.attachment_type.PNG)
        return pic_name

    def result_assert(self, res, expect, doc=""):
        """
        断言
        :param res: 实际结果
        :param expect: 期望结果
        :param doc: 页面
        :return:
        """
        try:
            print(f"实际结果: {res}, 期望结果: {expect}")
            assert res == expect
        except AssertionError:
            screen_name = self.get_screenshot(doc)
            logging.info("截图成功，图片为：{}".format(screen_name))
            raise
