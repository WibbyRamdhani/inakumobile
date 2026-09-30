from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class SidebarComponent(BasePage):
    TOMBOL_BURGER = (AppiumBy.XPATH, "(//android.widget.Button)[1]")
    
    # Sidebar items - simple ACCESSIBILITY_ID
    BERANDA = (AppiumBy.ACCESSIBILITY_ID, "Beranda")
    LAYANAN_PUBLIK = (AppiumBy.ACCESSIBILITY_ID, "Layanan Publik")
    INFORMASI_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Informasi Layanan")
    ADUAN_BANTUAN = (AppiumBy.ACCESSIBILITY_ID, "Aduan dan Bantuan")
    
    # Sidebar-specific elements (only visible when sidebar is open)
    SIDEBAR_SEARCH = (AppiumBy.XPATH, "//android.widget.EditText[@hint='Cari']")
    SYARAT_KETENTUAN = (AppiumBy.ACCESSIBILITY_ID, "Syarat dan Ketentuan")

    def tap_burger(self):
        """Buka sidebar dengan retry — pastikan sidebar benar-benar terbuka."""
        for attempt in range(3):
            self.tap(self.TOMBOL_BURGER)
            time.sleep(1.5)
            # Verify sidebar opened by checking for sidebar-specific element
            if self.is_element_displayed(self.SYARAT_KETENTUAN, timeout=3):
                return
            # Sidebar belum terbuka, coba lagi
            time.sleep(0.5)
        # Last attempt - don't check, just proceed
        raise Exception("Sidebar gagal dibuka setelah 3 percobaan")

    def is_sidebar_open(self, timeout=3):
        return self.is_element_displayed(self.SYARAT_KETENTUAN, timeout=timeout)

    def tap_beranda(self):
        self.tap(self.BERANDA)

    def tap_layanan_publik(self):
        self.tap(self.LAYANAN_PUBLIK)

    def tap_informasi_layanan(self):
        self.tap(self.INFORMASI_LAYANAN)

    def tap_aduan_bantuan(self):
        self.tap(self.ADUAN_BANTUAN)