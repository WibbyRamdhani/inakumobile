from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class LayananBantuanPage(BasePage):
    """
    Page Object untuk fitur Layanan Bantuan / Aduan (Tiket Bantuan).
    Diakses dari: tab 'Bantuan' di navbar bawah atau tombol 'Buat Tiket'.
    """

    # ─── Navigasi ke halaman ───
    TAB_BANTUAN = (AppiumBy.ACCESSIBILITY_ID, "Bantuan")

    # ─── Halaman Bantuan ───
    HALAMAN_BANTUAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Bantuan') or contains(@content-desc, 'Aduan') or "
        "contains(@content-desc, 'Tiket')]")
    TOMBOL_BUAT_TIKET = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Buat Tiket') or contains(@content-desc, 'Buat tiket')]")

    # ─── Form Tiket ───
    FIELD_JUDUL = (AppiumBy.XPATH,
        "(//android.widget.EditText)[1]")
    FIELD_DESKRIPSI = (AppiumBy.XPATH,
        "(//android.widget.EditText)[2]")
    DROPDOWN_KATEGORI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Kategori') or contains(@content-desc, 'kategori')]")
    TOMBOL_KIRIM_TIKET = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Kirim') or contains(@content-desc, 'Submit') or "
        "contains(@content-desc, 'Buat')]")
    TOMBOL_BATAL = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Batal') or contains(@content-desc, 'Kembali')]")

    # ─── Daftar tiket ───
    TIKET_PERTAMA = (AppiumBy.XPATH,
        "(//android.view.View[@clickable='true' and "
        "(contains(@content-desc, 'Tiket') or contains(@content-desc, '#'))])[1]")
    FILTER_STATUS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Status') or contains(@content-desc, 'Filter')]")

    # ─── Detail tiket ───
    DETAIL_TIKET = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Detail') or contains(@content-desc, 'detail')]")
    FIELD_BALAS = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'balas') or contains(@hint, 'Balas')]")
    TOMBOL_BALAS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Balas') or contains(@content-desc, 'Reply')]")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_bantuan(self):
        """Navigasi ke tab Bantuan."""
        self.tap(self.TAB_BANTUAN)
        time.sleep(1)

    def is_halaman_bantuan_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_BANTUAN, timeout=5)

    def tap_buat_tiket(self):
        self.scroll_and_tap(self.TOMBOL_BUAT_TIKET, max_swipes=3)

    def isi_form_tiket(self, judul: str, deskripsi: str):
        try:
            self.type_text(self.FIELD_JUDUL, judul)
        except Exception:
            pass
        try:
            self.type_text(self.FIELD_DESKRIPSI, deskripsi)
        except Exception:
            pass
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def kirim_tiket(self):
        self.scroll_and_tap(self.TOMBOL_KIRIM_TIKET, max_swipes=3)

    def tap_tiket_pertama(self):
        self.scroll_and_tap(self.TIKET_PERTAMA, max_swipes=3)

    def balas_tiket(self, pesan: str):
        self.scroll_and_tap(self.FIELD_BALAS, max_swipes=5)
        self.type_text(self.FIELD_BALAS, pesan)
        self.tap(self.TOMBOL_BALAS)
