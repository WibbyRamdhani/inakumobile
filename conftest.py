"""
conftest.py: fixture pytest yang menyalakan session Appium sebelum tiap test
dan menutupnya setelah selesai.
"""

import subprocess
import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage
from page.profil_page import ProfilPage
from config.capabilities import get_capabilities, APPIUM_SERVER_URL

APP_PACKAGE = "com.example.portal_layanan_publik_mobile"


def grant_app_permissions():
    permissions = [
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.ACCESS_COARSE_LOCATION",
        "android.permission.POST_NOTIFICATIONS",
    ]
    for perm in permissions:
        try:
            subprocess.run(
                ["adb", "shell", "pm", "grant", APP_PACKAGE, perm],
                capture_output=True, timeout=5
            )
        except Exception:
            pass


def dismiss_permission_dialog(driver):
    try:
        BerandaPage(driver).handle_permission_alert(timeout=2)
    except Exception:
        pass


@pytest.fixture(scope="session")
def driver_session():
    """Session-scoped driver — dibuat 1x, dipakai seluruh test suite."""
    options = UiAutomator2Options().load_capabilities(get_capabilities(use_existing_install=True))
    drv = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    drv.implicitly_wait(0)
    # Grant permissions sekali di awal session
    grant_app_permissions()
    yield drv
    drv.quit()


@pytest.fixture(scope="class")
def class_driver(driver_session):
    """Class-scoped driver: restart app saja (tanpa clearApp) agar lebih cepat."""
    driver_session.terminate_app(APP_PACKAGE)
    driver_session.activate_app(APP_PACKAGE)
    dismiss_permission_dialog(driver_session)
    yield driver_session


@pytest.fixture(scope="function")
def driver(driver_session):
    """Function-scoped driver: restart app saja (tanpa clearApp)."""
    driver_session.terminate_app(APP_PACKAGE)
    driver_session.activate_app(APP_PACKAGE)
    dismiss_permission_dialog(driver_session)
    yield driver_session


@pytest.fixture
def beranda(driver):
    return BerandaPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def profil_page(driver):
    return ProfilPage(driver)


@pytest.fixture(scope="class")
def class_beranda(class_driver):
    return BerandaPage(class_driver)


@pytest.fixture(scope="class")
def class_login(class_driver):
    return LoginPage(class_driver)


@pytest.fixture(scope="class")
def class_profil(class_driver):
    return ProfilPage(class_driver)