"""Dump UI BPJS dan BPOM untuk cari locator yang benar."""
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from xml.etree import ElementTree as ET
import time, os

caps = {
    'platformName': 'Android',
    'appium:automationName': 'UiAutomator2',
    'appium:deviceName': '133137051N005543',
    'appium:udid': '133137051N005543',
    'appium:appPackage': 'com.kominfo.portallayananpublik',
    'appium:appActivity': 'com.example.portal_layanan_publik_mobile.MainActivity',
    'appium:noReset': True,
    'appium:forceAppLaunch': True,
    'appium:newCommandTimeout': 120,
}
options = UiAutomator2Options().load_capabilities(caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
driver.implicitly_wait(3)
time.sleep(3)
os.makedirs('ui_dumps', exist_ok=True)

size = driver.get_window_size()
w, h = size['width'], size['height']

def dump_all_elements(label):
    src = driver.page_source
    root = ET.fromstring(src)
    print(f"\n=== [{label}] ===")
    for elem in root.iter():
        cd = elem.get('content-desc', '')
        hint = elem.get('hint', '')
        cls = elem.get('class', '').split('.')[-1]
        clickable = elem.get('clickable', '')
        if cd or hint:
            print(f"  [{cls}] clk={clickable} cd='{cd[:80]}' hint='{hint[:60]}'")
    with open(f'ui_dumps/{label}.xml', 'w', encoding='utf-8') as f:
        f.write(src)
    driver.save_screenshot(f'ui_dumps/{label}.png')

# ── Go to Beranda ──
beranda = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Beranda")
if beranda:
    beranda[-1].click()
    time.sleep(2)

# ── Navigate to BPJS ──
print("\n>>> Navigasi ke BPJS...")
bpjs_el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Informasi Status Kepesertaan JKN")
if not bpjs_el:
    # Scroll down to find
    for _ in range(5):
        driver.swipe(w//2, int(h*0.7), w//2, int(h*0.4), 500)
        time.sleep(0.5)
        bpjs_el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Informasi Status Kepesertaan JKN")
        if bpjs_el:
            break

if bpjs_el:
    bpjs_el[0].click()
    time.sleep(3)
    dump_all_elements("bpjs_page")
    # Scroll dan dump lagi
    for i in range(5):
        driver.swipe(w//2, int(h*0.7), w//2, int(h*0.4), 500)
        time.sleep(0.5)
        dump_all_elements(f"bpjs_scroll{i+1}")
else:
    print("  BPJS element tidak ditemukan di beranda!")

# ── Kembali ke Beranda ──
driver.back()
time.sleep(2)
beranda = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Beranda")
if beranda:
    beranda[-1].click()
    time.sleep(2)

# ── Navigate to BPOM ──
print("\n>>> Navigasi ke BPOM...")
bpom_el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Pengecekan Produk BPOM")
if not bpom_el:
    for _ in range(5):
        driver.swipe(w//2, int(h*0.7), w//2, int(h*0.4), 500)
        time.sleep(0.5)
        bpom_el = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Pengecekan Produk BPOM")
        if bpom_el:
            break

if bpom_el:
    bpom_el[0].click()
    time.sleep(3)
    dump_all_elements("bpom_page")
    for i in range(5):
        driver.swipe(w//2, int(h*0.7), w//2, int(h*0.4), 500)
        time.sleep(0.5)
        dump_all_elements(f"bpom_scroll{i+1}")
else:
    print("  BPOM element tidak ditemukan di beranda!")

driver.quit()
print("\nDone!")
