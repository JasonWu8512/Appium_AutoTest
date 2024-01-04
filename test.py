# from appium import webdriver
# from multiprocessing import Process
# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
#
# # # 定义安装应用程序函数
# # def install_app(device_name, udid, app_path):
# #     desired_caps = {
# #         'platformName': 'Android',
# #         'deviceName': device_name,
# #         'udid': udid,  # 设备的唯一标识符
# #     }
# #
# #     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# #
# #     # 检查应用是否已安装
# #     is_app_installed = driver.is_app_installed('com.jiliguala.niuwa')
# #
# #     if is_app_installed:
# #         # 如果应用已安装，卸载应用
# #         driver.remove_app('com.jiliguala.niuwa')
# #
# #     # 安装应用程序
# #     driver.install_app(app_path)
# #
# #     # 关闭驱动
# #     driver.quit()
#
#
# # 定义测试脚本
# def run_test(device_name, udid, platform_version):
#     desired_caps = {
#         'platformName': 'Android',
#         'deviceName': device_name,
#         'udid': udid,  # 设备的唯一标识符
#         'platformVersion': platform_version,
#         'appPackage': 'com.jiliguala.niuwa',
#         'appActivity': 'com.jiliguala.niuwa.module.splash.SplashActivity',
#         'ignoreHiddenApiPolicyError': True,
#         'noReset': False
#     }
#
#     driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#     # 在这里执行测试步骤
#     ...
#     wait = WebDriverWait(driver, 10)
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/tv_agree'))
#     )
#     button_element.click()
#
#     # 点击密码登录
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/to_secret_login'))
#     )
#     button_element.click()
#
#     time.sleep(3)
#
#     # 隐藏输入法键盘
#     hide_keyboard = driver.hide_keyboard()
#
#     # 勾选同意
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/iv_checkBox')))
#     button_element.click()
#
#     # 点击更多
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/more')))
#     button_element.click()
#
#     # 点击游客试用
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/ll_youke')))
#     button_element.click()
#
#     # 宝贝年龄
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/view3')))
#     button_element.click()
#
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/start_learn')))
#     button_element.click()
#
#     # 通知权限
#     # 不同厂商通知弹窗不同，需要分别处理
#     try:
#         button_element = wait.until(
#             EC.presence_of_element_located((MobileBy.XPATH,
#                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]')))
#         button_element.click()
#     except:
#         button_element = wait.until(
#             EC.presence_of_element_located(
#                 (MobileBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')))
#         button_element.click()
#
#     # 如果有弹窗，则点击运营弹窗进入购买页，否则点击icon进入购买页
#     try:
#         button_element = wait.until(
#             EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/showImage')))
#         button_element.click()
#     except:
#         button_element = wait.until(
#             EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/iv_operation_float_window')))
#         button_element.click()
#
#     # # 验证页面元素，输出结果
#     # assert driver.find_element(MobileBy.ID, 'com.jiliguala.niuwa:id/btn_purchase').text == '立即购买'
#     # assert driver.find_element(MobileBy.ID, 'com.jiliguala.niuwa:id/price').text == '0'
#
#     # 点击立即购买
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/btn_purchase')))
#     button_element.click()
#
#     # 取消登录
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/iv_finish')))
#     button_element.click()
#
#     time.sleep(3)
#
#     button_element = wait.until(
#         EC.presence_of_element_located((MobileBy.ID, 'com.jiliguala.niuwa:id/iv_buy_back')))
#     button_element.click()
#
#     driver.quit()
#
#
# if __name__ == '__main__':
#     # 配置设备信息
#     devices = [
#         # {'device_name': 'VIVO Y55', 'udid': '3474740888002TH', 'platform_version': '13'},
#         {'device_name': '小米11', 'udid': 'b2fc4235', 'platform_version': '13'}
#     ]
#
#     # # 安装不同版本的应用程序
#     # for device in devices:
#     #     # 为每台设备指定不同版本的应用程序路径
#     #     if device['device_name'] == 'VIVO Y55':
#     #         app_path = '/Users/jasonwu/Downloads/JLGL_V113101_11.31.1_202310131840_NOCHANNEL_JG.apk'
#     #     elif device['device_name'] == '小米11':
#     #         app_path = '/Users/jasonwu/Downloads/JLGL_V113200_11.32.0_202310241714_NOCHANNEL_JG.apk'
#     #
#     #     # 使用多进程安装应用程序
#     #     p = Process(target=install_app, args=(device['device_name'], device['udid'], app_path))
#     #     p.start()
#     #     p.join()
#
#     # 启动并行测试
#     processes = []
#     for device in devices:
#         p = Process(target=run_test, args=(device['device_name'], device['udid'], device['platform_version']))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
