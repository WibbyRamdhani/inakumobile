import subprocess
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from page.beranda_page import BerandaPage
from page.login_pages import LoginPage
from page.profil_page import ProfilPage

APPIUM_SERVER_URL = "http://127.0.0.1:4723"


def get_connected_device():
    result = subprocess.run(
        ["adb", "devices"],
        capture_output=True,
        text=True,
        check=True
    )

    devices = []

    for line in result.stdout.splitlines()[1:]:
        line = line.strip()

        if not line:
            continue

        parts = line.split()

        if len(parts) >= 2 and parts[1] == "device":
            devices.append(parts[0])

    if not devices:
        raise RuntimeError(
            "Tidak ada device Android yang terdeteksi. "
            "Jalankan 'adb devices' terlebih dahulu."
        )

    if len(devices) > 1:
        raise RuntimeError(
            f"Terdapat lebih dari satu device: {devices}. "
            "Silakan tentukan device yang ingin digunakan."
        )

    return devices[0]


def detect_app_package(udid):
    """Auto-detect package name dari device (debug atau production)."""
    KNOWN_PACKAGES = [
        "com.kominfo.portallayananpublik",
        "com.example.portal_layanan_publik_mobile",
    ]
    try:
        result = subprocess.run(
            ["adb", "-s", udid, "shell", "pm", "list", "packages"],
            capture_output=True, text=True, check=True
        )
        installed = result.stdout
        for pkg in KNOWN_PACKAGES:
            if f"package:{pkg}" in installed:
                return pkg
    except Exception:
        pass
    return KNOWN_PACKAGES[-1]


def get_capabilities(use_existing_install=True):
    udid = get_connected_device()
    app_package = detect_app_package(udid)

    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",

        "appium:deviceName": "Android Device",
        "appium:udid": udid,

        "appium:appPackage": app_package,
        "appium:appActivity": "com.example.portal_layanan_publik_mobile.MainActivity",

        "appium:autoGrantPermissions": True,
        "appium:forceAppLaunch": True,
        "appium:newCommandTimeout": 120,
        "appium:adbExecTimeout": 20000,
        "appium:noReset": use_existing_install,
    }

    return capabilities


# ─── CLASS-SCOPED FIXTURES ──────────────────────────────────────────────
# Digunakan oleh test class yang butuh satu session Appium per class
# (test_beranda_login, test_beranda_nonlogin, test_footer, test_layanan,
#  test_profil, test_search)

@pytest.fixture(scope="class")
def class_driver(request):
    """Appium driver yang di-share per test class (session dibuat 1x per class)."""
    import time
    APP_PACKAGE = "com.kominfo.portallayananpublik"
    # Kill stale UiAutomator2 processes dari session sebelumnya
    try:
        udid = get_connected_device()
        subprocess.run(
            ["adb", "-s", udid, "shell", "am", "force-stop",
             "io.appium.uiautomator2.server"],
            capture_output=True, timeout=5
        )
        subprocess.run(
            ["adb", "-s", udid, "shell", "am", "force-stop",
             "io.appium.uiautomator2.server.test"],
            capture_output=True, timeout=5
        )
        time.sleep(2)
    except Exception:
        pass

    caps = get_capabilities(use_existing_install=True)
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(5)
    time.sleep(2)  # Tunggu app fully load
    # Clear navigation stack: terminate + activate (bukan back-press yang bisa exit app)
    try:
        driver.terminate_app(APP_PACKAGE)
        time.sleep(1)
        driver.activate_app(APP_PACKAGE)
        time.sleep(3)  # Tunggu app kembali ke root screen
    except Exception:
        pass

    yield driver

    driver.quit()


@pytest.fixture(scope="class")
def class_beranda(class_driver):
    """BerandaPage instance yang di-share per test class."""
    return BerandaPage(class_driver)


@pytest.fixture(scope="class")
def class_login(class_driver):
    """LoginPage instance yang di-share per test class."""
    return LoginPage(class_driver)


@pytest.fixture(scope="class")
def class_profil(class_driver):
    """ProfilPage instance yang di-share per test class."""
    return ProfilPage(class_driver)


# ─── FUNCTION-SCOPED FIXTURES ───────────────────────────────────────────
# Digunakan oleh test class yang butuh session baru per test function
# (test_login, test_sidebar)

@pytest.fixture(scope="function")
def driver(request):
    """Appium driver baru per test function (session fresh tiap test)."""
    import time
    # Kill stale UiAutomator2 processes
    try:
        udid = get_connected_device()
        subprocess.run(
            ["adb", "-s", udid, "shell", "am", "force-stop",
             "io.appium.uiautomator2.server"],
            capture_output=True, timeout=5
        )
        time.sleep(1)
    except Exception:
        pass

    caps = get_capabilities(use_existing_install=True)
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(5)
    time.sleep(2)
    # Clear nav stack: terminate + activate
    try:
        driver.terminate_app("com.kominfo.portallayananpublik")
        time.sleep(1)
        driver.activate_app("com.kominfo.portallayananpublik")
        time.sleep(3)
    except Exception:
        pass

    yield driver

    driver.quit()



@pytest.fixture(scope="function")
def login_page(driver):
    """LoginPage instance per test function."""
    return LoginPage(driver)