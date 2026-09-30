from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class FaskesPage(BasePage):
    """
    Page Object untuk fitur Pencarian Fasilitas Layanan Kesehatan (Faskes).
    Diakses dari Beranda → Layanan Populer → 'Pencarian Fasilitas Layanan Kesehatan'
    atau dari Layanan → Kategori Kesehatan.
    """

    # ─── Entry point di beranda ───
    ITEM_FASKES = (AppiumBy.ACCESSIBILITY_ID, "Pencarian Fasilitas Layanan Kesehatan")

    # ─── Halaman Faskes ───
    HALAMAN_FASKES = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Fasilitas') or contains(@content-desc, 'Faskes') or "
        "contains(@content-desc, 'Kesehatan')]")
    FIELD_CARI_FASKES = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'cari') or contains(@hint, 'Cari') or "
        "contains(@hint, 'faskes') or contains(@hint, 'nama')]")
    TOMBOL_CARI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Cari') or contains(@content-desc, 'Search')]")

    # ─── Filter ───
    DROPDOWN_PROVINSI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Provinsi') or contains(@content-desc, 'provinsi')]")
    DROPDOWN_KOTA = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Kota') or contains(@content-desc, 'Kabupaten')]")
    DROPDOWN_JENIS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Jenis') or contains(@content-desc, 'Tipe')]")

    # ─── Hasil pencarian ───
    HASIL_FASKES_PERTAMA = (AppiumBy.XPATH,
        "(//android.view.View[@clickable='true' and "
        "(contains(@content-desc, 'Puskesmas') or contains(@content-desc, 'Rumah Sakit') or "
        "contains(@content-desc, 'Klinik') or contains(@content-desc, 'RS'))])[1]")
    PESAN_KOSONG = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak ditemukan') or contains(@content-desc, 'Tidak ada')]")

    # ─── Detail Faskes ───
    DETAIL_FASKES = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Detail') or contains(@content-desc, 'Alamat') or "
        "contains(@content-desc, 'Telepon')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_halaman_faskes_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_FASKES, timeout=5)

    def cari_faskes(self, keyword: str):
        try:
            self.type_text(self.FIELD_CARI_FASKES, keyword)
            self.driver.press_keycode(66)
            time.sleep(2)
        except Exception:
            pass

    def tap_hasil_pertama(self):
        self.scroll_and_tap(self.HASIL_FASKES_PERTAMA, max_swipes=3)

    def is_hasil_displayed(self) -> bool:
        return self.is_element_displayed(self.HASIL_FASKES_PERTAMA, timeout=5)

    def is_kosong_displayed(self) -> bool:
        return self.is_element_displayed(self.PESAN_KOSONG, timeout=5)
