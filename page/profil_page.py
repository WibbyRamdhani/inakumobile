from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class ProfilPage(BasePage):
    # Locators Halaman Profil
    TOMBOL_DETAIL_AKUN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Detail Akun') or contains(@text, 'Detail Akun')]")
    TOMBOL_SENSITIVE_INFO = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Tampilkan Info Sensitif') or contains(@text, 'Tampilkan Info Sensitif')]")
    TOMBOL_EDOKUMEN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'E-Dokumen') or contains(@text, 'E-Dokumen')]")
    TOMBOL_DOKUMEN_SAYA = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Dokumen Saya') or contains(@text, 'Dokumen Saya')]")
    TOMBOL_DOKUMEN_KELUARGA = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Dokumen Keluarga') or contains(@text, 'Dokumen Keluarga')]")
    TOMBOL_STATUS = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Status') or contains(@text, 'Status')]")
    TOMBOL_PENGATURAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Pengaturan') or contains(@text, 'Pengaturan')]")
    
    SEARCH_DOKUMEN = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    DOKUMEN_PERTAMA = (AppiumBy.XPATH, "(//android.view.View[contains(@content-desc, 'Dokumen')])[1]")
    TOMBOL_UNDUH = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Unduh') or contains(@text, 'Unduh')]")
    
    # Locators Tombol Toggle Switch khusus berdasarkan elemen DOM persis:
    # 1. Notifikasi Email Switch: bounds [847,1444][947,1497]
    TOGGLE_NOTIFIKASI_EMAIL = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Notifikasi Email')]/following-sibling::android.view.View[@clickable='true'] | (//android.view.View[@clickable='true' and contains(@bounds, '[847,')])[1]")
    # 2. Pembaruan Permohonan Switch: bounds [847,1649][947,1702]
    TOGGLE_PEMBARUAN_PERMOHONAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Pembaruan Permohonan')]/following-sibling::android.view.View[@clickable='true'] | (//android.view.View[@clickable='true' and contains(@bounds, '[847,')])[2]")
    # 3. Peringatan Keamanan Switch: bounds [847,1866][947,1918]
    TOGGLE_PERINGATAN_KEAMANAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Peringatan Keamanan')]/following-sibling::android.view.View[@clickable='true'] | (//android.view.View[@clickable='true' and contains(@bounds, '[847,')])[3]")
    
    def __init__(self, driver):
        super().__init__(driver)

    def _tap_fast(self, locator: tuple, max_swipes: int = 2):
        """Tap elemen langsung tanpa swipe jika sudah ada di layar. Swipe max 2x jika belum ada."""
        if self.is_element_displayed(locator, timeout=1.5):
            self.tap(locator, timeout=3)
            return
        for _ in range(max_swipes):
            self.swipe_down()
            time.sleep(0.3)
            if self.is_element_displayed(locator, timeout=1.5):
                self.tap(locator, timeout=3)
                return
        self.tap(locator, timeout=3)

    def buka_detail_akun(self):
        self._tap_fast(self.TOMBOL_DETAIL_AKUN)

    def buka_sensitive_info(self):
        self._tap_fast(self.TOMBOL_SENSITIVE_INFO)

    def buka_edokumen(self):
        self._tap_fast(self.TOMBOL_EDOKUMEN)

    def buka_pengaturan(self):
        self._tap_fast(self.TOMBOL_PENGATURAN)

    def buka_dokumen_saya(self):
        self._tap_fast(self.TOMBOL_DOKUMEN_SAYA)

    def buka_dokumen_keluarga(self):
        self._tap_fast(self.TOMBOL_DOKUMEN_KELUARGA)

    def buka_status(self):
        self._tap_fast(self.TOMBOL_STATUS)

    def cari_dokumen(self, keyword: str):
        self.type_text(self.SEARCH_DOKUMEN, keyword)

    def buka_detail_dokumen_pertama(self):
        self._tap_fast(self.DOKUMEN_PERTAMA)

    def unduh_dokumen(self):
        self._tap_fast(self.TOMBOL_UNDUH)

    def toggle_notifikasi_email(self):
        """Toggle Notifikasi Email."""
        self._tap_fast(self.TOGGLE_NOTIFIKASI_EMAIL)

    def toggle_pembaruan_permohonan(self):
        """Toggle Pembaruan Permohonan."""
        self._tap_fast(self.TOGGLE_PEMBARUAN_PERMOHONAN)

    def toggle_peringatan_keamanan(self):
        """Toggle Peringatan Keamanan."""
        self._tap_fast(self.TOGGLE_PERINGATAN_KEAMANAN)

    def tap_toggle(self, toggle_number: int = 1):
        """Tap toggle switch notifikasi ke-n (1: Email, 2: Permohonan, 3: Keamanan)."""
        if toggle_number == 1:
            self.toggle_notifikasi_email()
        elif toggle_number == 2:
            self.toggle_pembaruan_permohonan()
        elif toggle_number == 3:
            self.toggle_peringatan_keamanan()
        else:
            self.toggle_notifikasi_email()
