import os

base_path = os.path.dirname(os.path.dirname(__file__))

appPath = os.path.join(base_path, 'app')
dataPath = os.path.join(base_path, 'data')
configPath = os.path.join(base_path, 'config')
logPath = os.path.join(base_path, 'outputs', 'logs')
picturePath = os.path.join(base_path, 'outputs', 'picture')
reportsPath = os.path.join(base_path, 'outputs', 'reports')
