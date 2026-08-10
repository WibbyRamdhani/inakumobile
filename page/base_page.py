from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time

class BasePage:
    APP_PACKAGE = "com.example.portal_layanan_publik_mobile"

    TAB_BERANDA = (AppiumBy.ACCESSIBILITY_ID, "Beranda")
    TAB_CARI = (AppiumBy.ACCESSIBILITY_ID, "Cari")
    TAB_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Layanan")
    TAB_PROFIL = (AppiumBy.ACCESSIBILITY_ID, "Profil")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def ensure_app_in_foreground(self):
        """Memastikan aplikasi utama aktif di foreground (bila terlempar ke PlayStore/Browser)."""
        try:
            current_app = self.driver.current_package
            if current_app and current_app != self.APP_PACKAGE:
                self.driver.activate_app(self.APP_PACKAGE)
        except Exception:
            pass

    def find_element(self, locator: tuple, timeout: int = 5):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def tap(self, locator: tuple, timeout: int = 5):
        for attempt in range(3):
            try:
                element = self.find_element(locator, timeout)
                element.click()
                return
            except (StaleElementReferenceException, TimeoutException):
                if attempt == 2:
                    raise
                self.ensure_app_in_foreground()
                time.sleep(0.2)

    def handle_permission_alert(self, timeout: int = 0.3) -> bool:
        """Menangani alert/dialog izin sistem Android secara cepat."""
        locators = [
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"),
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"),
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button"),
            (AppiumBy.XPATH, "//*[contains(@text, 'While using the app') or contains(@text, 'Saat aplikasi digunakan') or contains(@text, 'Izinkan') or contains(@text, 'Allow')]")
        ]
        for loc in locators:
            if self.is_element_displayed(loc, timeout=timeout):
                try:
                    element = self.find_element(loc, timeout=1)
                    element.click()
                    return True
                except Exception:
                    pass
        return False

    def _navigate_to_tab(self, tab_locator: tuple, tab_name: str = ""):
        """Navigasi ke tab bottom nav secara sangat cepat."""
        if self.is_element_displayed(tab_locator, timeout=0.8):
            self.tap(tab_locator, timeout=2)
            return
        for _ in range(2):
            try:
                self.driver.back()
            except Exception:
                pass
            if self.is_element_displayed(tab_locator, timeout=0.8):
                self.tap(tab_locator, timeout=2)
                return
        self.ensure_app_in_foreground()
        self.tap(tab_locator, timeout=3)

    def go_to_beranda(self):
        self._navigate_to_tab(self.TAB_BERANDA, "Beranda")

    def go_to_cari(self):
        self._navigate_to_tab(self.TAB_CARI, "Cari")

    def go_to_layanan(self):
        self._navigate_to_tab(self.TAB_LAYANAN, "Layanan")

    def go_to_profil(self):
        self._navigate_to_tab(self.TAB_PROFIL, "Profil")

    def type_text(self, locator: tuple, text: str, timeout: int = 5):
        try:
            element = self.find_element(locator, timeout)
            element.click()
            element.clear()
            element.send_keys(text)
        except (StaleElementReferenceException, TimeoutException):
            self.ensure_app_in_foreground()
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(text)

    def is_element_displayed(self, locator: tuple, timeout: int = 2) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def swipe_down(self, duration: int = 350):
        """Scroll sedang (35% tinggi layar) agar cepat dan efisien."""
        self.ensure_app_in_foreground()
        try:
            size = self.driver.get_window_size()
            sx = size['width'] * 0.5
            self.driver.swipe(sx, size['height'] * 0.70, sx, size['height'] * 0.35, duration)
        except Exception:
            pass

    def scroll_to_element(self, locator: tuple, max_swipes: int = 10):
        """Scroll bertahap cepat sampai elemen terlihat."""
        self.ensure_app_in_foreground()
        if self.is_element_displayed(locator, timeout=1.0):
            return
        for _ in range(max_swipes):
            self.swipe_down()
            time.sleep(0.3)
            if self.is_element_displayed(locator, timeout=1.0):
                return

    def scroll_and_tap(self, locator: tuple, max_swipes: int = 10):
        self.scroll_to_element(locator, max_swipes)
        self.tap(locator)

    def swipe_up(self, duration: int = 350):
        """Scroll ke atas (ke arah top layar)."""
        try:
            size = self.driver.get_window_size()
            sx = size['width'] * 0.5
            self.driver.swipe(sx, size['height'] * 0.35, sx, size['height'] * 0.75, duration)
        except Exception:
            pass

    def scroll_to_top(self, max_swipes: int = 5):
        """Scroll kembali ke bagian paling atas layar."""
        for _ in range(max_swipes):
            self.swipe_up()
            time.sleep(0.2)

    def press_back(self):
        try:
            self.driver.back()
        except Exception:
            pass
        self.ensure_app_in_foreground()
