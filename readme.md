# Taro

## 项目介绍

Taro是python语言，基于PO模式的pytest、Appium二次封装的Android自动化框架，多进程方式在多台手机上同时执行测试，自动获取已连接设备信息，
自动启动多个appium服务，同一套测试用例在不同手机上执行，用例执行失败自动截图、收集报错信息，allure插件生成测试报告。

# 框架目录说明
```
pyAppium		# 项目根目录
├─app			# 测试APP存放目录
├─common		# 公共模块目录
├─config		# 配置文件目录
├─data			# 测试数据目录
├─outputs		# 测试输出目录
│  ├─logs		# 日志目录
│  ├─picture	# 截图存放目录
│  └─reports	# 测试报告存放目录
├─pageViwe		# PO模式页面封装模块
└─testcase		# 测试用例目录
```

## 主要功能

 1. 自动启动appium server和杀掉appium server
 2. 自动获取电脑连接设备信息，如设备版本、设备udid
 3. 自动检测端口是否可用、释放占用端口
 4. 自动获取测试APP应用相关信息，如：appPackage、launchable_activity
 5. 自动安装APP和卸载APP
 6. 测试用例无需配置，自动获取用例执行，测试人员只需编写相关case
 7. 用例执行失败自动截图、收集错误日志信息，自动加到测试报告对应case下面
 8. 启动一次APP，执行所有测试用例，缩短测试用例执行间隔，提高测试执行效率
 9. 多进程方式在多台手机上同时执行测试，大幅提高测试效率

## 框架使用
### 测试环境
测试环境
1. python v3.8
2. node v20.5.1
3. Appium-Python-Client v2.0.0
4. pytest v7.4.2
5. allure-pytest v2.8.10 
6. requests v2.31.0
### 使用说明
 - 启动项目：直接运行`main.py`文件即可。