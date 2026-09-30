from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class SkmPage(BasePage):
    """
    Page Object untuk fitur SKM (Survei Kepuasan Masyarakat).
    Diakses dari halaman Detail Layanan → tombol 'Isi Survei' atau dari menu Profil.
    """

    # ─── Indikator halaman ───
    HALAMAN_SKM = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Survei') or contains(@content-desc, 'SKM') or "
        "contains(@content-desc, 'Kepuasan')]")

    # ─── Form SKM ───
    TOMBOL_ISI_SURVEI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Isi Survei') or contains(@content-desc, 'Isi survei')]")
    RATING_BINTANG = (AppiumBy.XPATH,
        "(//android.view.View[@clickable='true' and contains(@content-desc, 'bintang')])")
    RATING_BINTANG_5 = (AppiumBy.XPATH,
        "(//*[contains(@content-desc, 'bintang') or contains(@content-desc, '5')])[last()]")
    FIELD_KOMENTAR = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'komentar') or "
        "contains(@hint, 'Komentar') or contains(@hint, 'masukan')]")
    TOMBOL_KIRIM = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Kirim') or contains(@content-desc, 'Submit') or "
        "contains(@content-desc, 'Simpan')]")
    TOMBOL_BATAL = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Batal') or contains(@content-desc, 'Lewati')]")

    # ─── Konfirmasi / sukses ───
    PESAN_SUKSES = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'berhasil') or contains(@content-desc, 'Terima kasih') or "
        "contains(@content-desc, 'sukses')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_halaman_skm_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_SKM, timeout=5)

    def tap_isi_survei(self):
        self.scroll_and_tap(self.TOMBOL_ISI_SURVEI, max_swipes=3)

    def pilih_rating(self, bintang: int = 5):
        """Pilih rating bintang 1-5."""
        locator = (AppiumBy.XPATH,
            f"(//*[contains(@content-desc, '{bintang}') or "
            f"contains(@content-desc, 'bintang')])[{bintang}]")
        try:
            self.scroll_and_tap(locator, max_swipes=2)
        except Exception:
            self.scroll_and_tap(self.RATING_BINTANG_5, max_swipes=2)

    def isi_komentar(self, teks: str):
        try:
            self.type_text(self.FIELD_KOMENTAR, teks)
            try:
                self.driver.hide_keyboard()
            except Exception:
                pass
        except Exception:
            pass

    def kirim_survei(self):
        self.scroll_and_tap(self.TOMBOL_KIRIM, max_swipes=3)

    def is_sukses_displayed(self) -> bool:
        return self.is_element_displayed(self.PESAN_SUKSES, timeout=5)
