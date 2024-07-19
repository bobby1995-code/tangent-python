import os

# Configuration settings
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH', '/Users/pc/Downloads/chromedriver')
TARGET_URL = os.getenv('TARGET_URL', 'https://www.kurtosys.com/')
SCREENSHOT_PATH = os.getenv('SCREENSHOT_PATH', '/Users/pc/Downloads/screenshot.png')
