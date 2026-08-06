from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class FooterComponent(BasePage):
    TOMBOL_LIHAT_PERTANYAAN_UMUM = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Lihat pertanyaan umum') or contains(@text, 'Lihat pertanyaan umum')])[last()]")
    IKON_IG = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Instagram') or contains(@content-desc, 'ig')])[last()]")
    IKON_TIKTOK = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'TikTok')])[last()]")
    IKON_TWITTER = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Twitter') or contains(@content-desc, 'X')])[last()]")
    
    # Target spesifik elemen toggle di area footer (elemen paling bawah / [last()])
    TOGGLE_LAYANAN_PUBLIK = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Layanan Publik') or contains(@text, 'Layanan Publik')])[last()]")
    TOGGLE_BANTUAN = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Bantuan') or contains(@text, 'Bantuan')])[last()]")

    def __init__(self, driver):
        super().__init__(driver)

    def _tap_footer_element(self, locator: tuple, max_swipes: int = 2):
        """Tap elemen footer tanpa scroll berlebihan. Maksimal swipe 2x."""
        if self.is_element_displayed(locator, timeout=1.5):
            self.tap(locator, timeout=3)
            return
        for _ in range(max_swipes):
            self.swipe_down()
            time.sleep(0.3)
            if self.is_element_displayed(locator, timeout=1.5):
                self.tap(locator, timeout=3)
                return
        try:
            self.tap(locator, timeout=2)
        except Exception:
            pass

    def tap_lihat_pertanyaan_umum(self):
        self._tap_footer_element(self.TOMBOL_LIHAT_PERTANYAAN_UMUM)

    def tap_toggle_layanan_publik(self):
        self._tap_footer_element(self.TOGGLE_LAYANAN_PUBLIK)
        
    def tap_toggle_bantuan(self):
        self._tap_footer_element(self.TOGGLE_BANTUAN)
        
    def tap_sosmed(self, nama_sosmed: str):
        if nama_sosmed.lower() == 'ig':
            self._tap_footer_element(self.IKON_IG)
        elif nama_sosmed.lower() == 'tiktok':
            self._tap_footer_element(self.IKON_TIKTOK)
        elif nama_sosmed.lower() == 'twitter':
            self._tap_footer_element(self.IKON_TWITTER)