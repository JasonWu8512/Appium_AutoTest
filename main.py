import os
from multiprocessing import Process

import pytest


def run_test():
    pytest.main(['-s', '-v', '--alluredir', 'outputs/reports/data'])
    os.system('allure generate outputs/reports/data -o outputs/reports/html --clean')


if __name__ == '__main__':
    # 配置设备信息
    devices = [
        # {'device_name': 'VIVO Y55', 'udid': '3474740888002TH', 'platform_version': '13'},
        {'device_name': '小米11', 'udid': 'b2fc4235', 'platform_version': '13'}
    ]

    # # 安装不同版本的应用程序
    # for device in devices:
    #     # 为每台设备指定不同版本的应用程序路径
    #     if device['device_name'] == 'VIVO Y55':
    #         app_path = '/Users/jasonwu/Downloads/JLGL_V113101_11.31.1_202310131840_NOCHANNEL_JG.apk'
    #     elif device['device_name'] == '小米11':
    #         app_path = '/Users/jasonwu/Downloads/JLGL_V113200_11.32.0_202310241714_NOCHANNEL_JG.apk'
    #
    #     # 使用多进程安装应用程序
    #     p = Process(target=install_app, args=(device['device_name'], device['udid'], app_path))
    #     p.start()
    #     p.join()

    # 启动并行测试
    processes = []
    for device in devices:
        p = Process(target=run_test)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
