"""
Script untuk dump UI hierarchy dari HP untuk mendapatkan locator yang benar.
Jalankan saat app sudah terbuka di HP.
"""
import subprocess
import json
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

APPIUM_URL = "http://127.0.0.1:4723"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "ui_dumps")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_device():
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True, check=True)
    for line in result.stdout.splitlines()[1:]:
        parts = line.strip().split()
        if len(parts) >= 2 and parts[1] == "device":
            return parts[0]
    raise RuntimeError("No device found")


def detect_package(udid):
    result = subprocess.run(
        ["adb", "-s", udid, "shell", "pm", "list", "packages"],
        capture_output=True, text=True, check=True
    )
    for pkg in ["com.kominfo.portallayananpublik", "com.example.portal_layanan_publik_mobile"]:
        if f"package:{pkg}" in result.stdout:
            return pkg
    return "com.example.portal_layanan_publik_mobile"


def dump_page(driver, name):
    """Dump page source dan screenshot."""
    filepath = os.path.join(OUTPUT_DIR, f"{name}.xml")
    screenshot = os.path.join(OUTPUT_DIR, f"{name}.png")
    
    source = driver.page_source
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(source)
    
    driver.save_screenshot(screenshot)
    print(f"  [OK] Dumped: {name} ({len(source)} bytes)")
    return source


def swipe_down(driver):
    size = driver.get_window_size()
    driver.swipe(
        size['width'] * 0.5, size['height'] * 0.70,
        size['width'] * 0.5, size['height'] * 0.35, 350
    )
    time.sleep(1)


def tap_element(driver, locator, timeout=5):
    try:
        el = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        el.click()
        time.sleep(2)
        return True
    except:
        return False


def main():
    udid = get_device()
    pkg = detect_package(udid)
    print(f"Device: {udid}, Package: {pkg}")

    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android Device",
        "appium:udid": udid,
        "appium:appPackage": pkg,
        "appium:appActivity": "com.example.portal_layanan_publik_mobile.MainActivity",
        "appium:autoGrantPermissions": True,
        "appium:newCommandTimeout": 300,
        "appium:noReset": True,
    }

    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote(APPIUM_URL, options=options)
    driver.implicitly_wait(3)

    try:
        print("\n=== DUMPING UI HIERARCHY ===\n")

        # 1. Beranda (non-login / awal)
        print("[1/8] Beranda - Top")
        time.sleep(3)
        dump_page(driver, "01_beranda_top")

        # 2. Beranda scroll down
        print("[2/8] Beranda - Scroll Down")
        swipe_down(driver)
        swipe_down(driver)
        dump_page(driver, "02_beranda_middle")
        swipe_down(driver)
        swipe_down(driver)
        dump_page(driver, "03_beranda_bottom")

        # 3. Tab Cari
        print("[3/8] Tab Cari")
        tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Cari"))
        dump_page(driver, "04_tab_cari")

        # 4. Tab Layanan
        print("[4/8] Tab Layanan")
        tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Layanan"))
        dump_page(driver, "05_tab_layanan")

        # 5. Tab Profil
        print("[5/8] Tab Profil")
        tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Profil"))
        dump_page(driver, "06_tab_profil")

        # 6. Back to Beranda, try Login
        print("[6/8] Login Page")
        tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Beranda"))
        time.sleep(1)
        if tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Masuk"), timeout=3):
            time.sleep(2)
            dump_page(driver, "07_login_page")
            
            # Try login
            print("[7/8] Attempting Login...")
            try:
                fields = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
                if len(fields) >= 2:
                    fields[0].click()
                    fields[0].clear()
                    fields[0].send_keys("hernanda17@hotmail.com")
                    fields[1].click()
                    fields[1].clear()
                    fields[1].send_keys("Bebas884422")
                    try:
                        driver.hide_keyboard()
                    except:
                        pass
                    tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Masuk ke akun IKD"), timeout=5)
                    time.sleep(8)
                    dump_page(driver, "08_after_login_beranda")
                    
                    # Scroll beranda after login
                    swipe_down(driver)
                    swipe_down(driver)
                    dump_page(driver, "09_after_login_middle")
                    swipe_down(driver)
                    swipe_down(driver)
                    dump_page(driver, "10_after_login_bottom")
                    
                    # Profil after login
                    tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Profil"))
                    dump_page(driver, "11_profil_logged_in")
                    swipe_down(driver)
                    dump_page(driver, "12_profil_scrolled")
            except Exception as e:
                print(f"  ⚠️ Login failed: {e}")
                dump_page(driver, "07_login_error")
        else:
            print("  ⚠️ Tombol Masuk tidak ditemukan (mungkin sudah login)")
            dump_page(driver, "07_already_logged_in")

        # 8. Sidebar
        print("[8/8] Sidebar")
        tap_element(driver, (AppiumBy.ACCESSIBILITY_ID, "Beranda"))
        time.sleep(1)
        # Try burger menu / hamburger icon
        try:
            burger = driver.find_elements(AppiumBy.XPATH, 
                "//android.widget.Button[1] | //android.widget.ImageView[1]")
            if burger:
                burger[0].click()
                time.sleep(1)
                dump_page(driver, "13_sidebar")
        except:
            print("  ⚠️ Sidebar tidak ditemukan")

        print(f"\n✅ Selesai! UI dumps tersimpan di: {OUTPUT_DIR}")
        print(f"   Total files: {len(os.listdir(OUTPUT_DIR))}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
