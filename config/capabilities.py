import os

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_APK_PATH = os.getenv("APP_PATH", os.path.join(BASE_DIR, "app.apk"))

def get_capabilities(use_existing_install: bool = False) -> dict:
    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:platformVersion": "16",
        "appium:appPackage": "com.example.portal_layanan_publik_mobile",
        "appium:appActivity": "com.example.portal_layanan_publik_mobile.MainActivity",
        "appium:autoGrantPermissions": True,
        "appium:newCommandTimeout": 120,
        "appium:adbExecTimeout": 20000,
    }

    if use_existing_install:
        caps["appium:noReset"] = True
    else:
        caps["appium:app"] = DEFAULT_APK_PATH
        caps["appium:noReset"] = False

    return caps