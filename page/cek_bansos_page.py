from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class CekBansosPage(BasePage):
    """
    Page Object untuk fitur Cek Bantuan Sosial (Bansos).
    Diakses dari Beranda → 'Mengecek Bantuan Sosial'
    Status: ⚙️ API belum terintegrasi
    NIK Test: 1902015511940006
    """

    # ─── Entry point ───
    ITEM_BANSOS = (AppiumBy.ACCESSIBILITY_ID, "Mengecek Bantuan Sosial")

    # ─── Halaman Bansos ───
    HALAMAN_BANSOS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Bansos') or contains(@content-desc, 'Bantuan Sosial') or "
        "contains(@content-desc, 'Bantuan') or contains(@content-desc, 'PKH')]")
    FIELD_NIK = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'NIK') or contains(@hint, 'nik') or "
        "contains(@hint, 'Nomor Induk') or contains(@hint, 'KTP')]")
    TOMBOL_CEK = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Cek') or contains(@content-desc, 'Periksa') or "
        "contains(@content-desc, 'Cari')]")

    # ─── Hasil ───
    HASIL_BANSOS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'PKH') or contains(@content-desc, 'BPNT') or "
        "contains(@content-desc, 'bansos') or contains(@content-desc, 'Penerima')]")
    PESAN_TIDAK_MENERIMA = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak menerima') or "
        "contains(@content-desc, 'Tidak terdaftar')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_halaman_bansos_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_BANSOS, timeout=5)

    def cek_bansos(self, nik: str):
        try:
            self.type_text(self.FIELD_NIK, nik)
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass
            self.scroll_and_tap(self.TOMBOL_CEK, max_swipes=2)
            time.sleep(5)
        except Exception:
            pass

    def is_hasil_displayed(self) -> bool:
        return self.is_element_displayed(self.HASIL_BANSOS, timeout=5)
