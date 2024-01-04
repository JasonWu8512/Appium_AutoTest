import os
import time

from multiprocessing import Process

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.onboarding
class TestOutPutCodeEn0(object):
    # dm = Domains()
    #
    # @classmethod
    # def setup_class(cls):
    #     # # 【代码提交用】从环境变量获取env
    #     # env = os.environ.get('env')
    #     # # 【代码提交用】获取环境变量
    #     # cls.config = cls.dm.set_env_path(env)
    #     # # 【代码提交用】
    #     # print(env)
    #     cls.config = cls.dm.set_env_path('prod')
    #     cls.dm.set_domain(cls.config['url'])
    #     print(cls.config['url'])

    @pytest.fixture
    def device_name(self):
        return '小米11'  # 替换为你实际的设备名

    @pytest.fixture
    def udid(self):
        return 'b2fc4235'

    @pytest.fixture
    def platform_version(self):
        return '13'

    @staticmethod
    def test_en_0(device_name, udid, platform_version, mobile='11100000060'):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': device_name,
            'udid': udid,  # 设备的唯一标识符
            'platformVersion': platform_version,
            'appPackage': 'com.android.chrome',
            'appActivity': 'com.google.android.apps.chrome.Main',
            'ignoreHiddenApiPolicyError': True,
            'noReset': True
        }

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 切换到Web Context
        web_contexts = driver.contexts
        print("Available contexts:", web_contexts)

        # 选择第一个Web Context
        if len(web_contexts) > 1:
            driver.switch_to.context(web_contexts[1])
        else:
            print("List does not contain enough elements.")

        url = "https://fatspa.jiliguala.com/store/share/index.html#/item?targetPage=item&spuId=K1_K3MAFC_0_SPU&source=test"
        driver.get(url)

        # 在WebView中执行一些操作，比如查找元素、点击等
        wait = WebDriverWait(driver, 10)
        el = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout[1]/android.widget.FrameLayout['
                           '2]/android.webkit.WebView/android.view.View/android.view.View['
                           '2]/android.view.View[3]/android.view.View/android.widget.Button'))
        )
        el.click()

        # 输入手机号
        el = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout[1]/android.widget.FrameLayout['
                           '2]/android.webkit.WebView/android.view.View/android.view.View['
                           '4]/android.view.View[2]/android.widget.EditText'))
        )
        el.click()
        el.send_keys('11110000101')  # 11110000102

        time.sleep(2)

        # 获取验证码
        el = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout[1]/android.widget.FrameLayout['
                           '2]/android.webkit.WebView/android.view.View/android.view.View['
                           '4]/android.view.View[3]/android.view.View[2]'))
        )
        el.click()
        time.sleep(5)

        el = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                           '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                           '.FrameLayout[1]/android.widget.FrameLayout['
                           '2]/android.webkit.WebView/android.view.View/android.view.View['
                           '4]/android.view.View[3]/android.view.View[1]'))
        )
        el.click()
        el.send_keys('7429')
        time.sleep(5)

        # 立即领取
        el = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                           '/android.widget.FrameLayout[1]/android.widget.FrameLayout['
                           '2]/android.webkit.WebView/android.view.View/android.view.View[4]/android.view.View[4]'))
        )
        el.click()

        # 切换回Native Context
        driver.switch_to.context(web_contexts[0])

        # 在原生应用中执行一些原生操作，比如点击按钮、输入框等
        # driver.find_element_by_id("your_native_element_id").click()

        # # 关闭应用
        # driver.quit()


if __name__ == '__main__':
    output_code = TestOutPutCodeEn0()
    output_code.setup_class()
    # 配置设备信息
    devices = [
        # {'device_name': 'VIVO Y55', 'udid': '3474740888002TH', 'platform_version': '13'},
        {'device_name': '小米11', 'udid': 'b2fc4235', 'platform_version': '13'}
    ]

    # 启动并行测试
    processes = []
    for device in devices:
        p = Process(target=output_code.test_en_0,
                    args=(device['device_name'], device['udid'], device['platform_version']))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
