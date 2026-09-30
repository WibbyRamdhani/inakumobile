from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class CariDokterPage(BasePage):
    """
    Page Object untuk fitur Pencarian Dokter.
    Diakses dari Beranda → Layanan Populer → 'Pencarian Dokter'
    Status: 🔵 In Progress
    """

    # ─── Entry point ───
    ITEM_CARI_DOKTER = (AppiumBy.ACCESSIBILITY_ID, "Pencarian Dokter")

    # ─── Halaman Pencarian Dokter ───
    HALAMAN_CARI_DOKTER = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Dokter') or contains(@content-desc, 'dokter')]")
    FIELD_CARI_DOKTER = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'dokter') or "
        "contains(@hint, 'Dokter') or contains(@hint, 'nama') or contains(@hint, 'spesialis')]")
    DROPDOWN_SPESIALISASI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Spesialisasi') or contains(@content-desc, 'spesialis')]")
    DROPDOWN_LOKASI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Lokasi') or contains(@content-desc, 'Kota')]")
    TOMBOL_CARI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Cari') or contains(@content-desc, 'Search')]")

    # ─── Hasil ───
    HASIL_DOKTER_PERTAMA = (AppiumBy.XPATH,
        "(//android.view.View[@clickable='true' and "
        "(contains(@content-desc, 'dr.') or contains(@content-desc, 'Dr.') or "
        "contains(@content-desc, 'dokter'))])[1]")
    PESAN_TIDAK_DITEMUKAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak ditemukan') or contains(@content-desc, 'Tidak ada')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_halaman_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_CARI_DOKTER, timeout=5)

    def cari_dokter(self, keyword: str):
        try:
            self.type_text(self.FIELD_CARI_DOKTER, keyword)
            self.driver.press_keycode(66)
            time.sleep(2)
        except Exception:
            pass

    def tap_hasil_pertama(self):
        self.scroll_and_tap(self.HASIL_DOKTER_PERTAMA, max_swipes=3)

    def is_hasil_displayed(self) -> bool:
        return self.is_element_displayed(self.HASIL_DOKTER_PERTAMA, timeout=5)
