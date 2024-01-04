import pytest

from appium import webdriver
from config.appConfig import AppConfig


@pytest.fixture(scope='class')
def setup(request):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '小米11',
        'udid': 'b2fc4235',
        'platformVersion': '13',
        'appPackage': 'com.jiliguala.niuwa',
        'appActivity': 'com.jiliguala.niuwa.module.splash.SplashActivity',
        'ignoreHiddenApiPolicyError': True,
        'noReset': False,
    }

    driver = webdriver.Remote(AppConfig.APPIUM_SERVER_URL, desired_caps)

    yield driver

    driver.quit()
