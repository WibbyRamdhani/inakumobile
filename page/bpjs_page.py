from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class BpjsPage(BasePage):
    """
    Page Object untuk fitur BPJS - Informasi Status Kepesertaan JKN.
    
    CATATAN: Fitur ini membuka halaman Detail Layanan informatif (bukan tool input NIK).
    Diakses dari Beranda → Layanan Populer → 'Informasi Status Kepesertaan JKN'
    """

    # ─── Entry point ───
    ITEM_BPJS = (AppiumBy.ACCESSIBILITY_ID, "Informasi Status Kepesertaan JKN")

    # ─── Halaman Detail Layanan JKN ───
    JUDUL_HALAMAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'JKN') or contains(@content-desc, 'Kepesertaan') or "
        "contains(@content-desc, 'BPJS')]")
    KONTEN_ONLINE = (AppiumBy.ACCESSIBILITY_ID, "ONLINE")
    KONTEN_NASIONAL = (AppiumBy.ACCESSIBILITY_ID, "NASIONAL")
    TOMBOL_WEBSITE = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Website') or contains(@content-desc, 'website')]")

    # ─── Kanal Pengaduan ───
    KANAL_LAPOR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'LAPOR') or contains(@content-desc, 'lapor')]")

    # ─── QnA / Pertanyaan ───
    PERTANYAAN_LAYANAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Pertanyaan Seputar Layanan')]")
    CARD_JKN = (AppiumBy.XPATH,
        "(//android.view.View[@clickable='true' and "
        "contains(@content-desc, 'Informasi Status Kepesertaan JKN')])[1]")

    # ─── Rating ───
    BERI_RATING = (AppiumBy.ACCESSIBILITY_ID, "Beri Rating")
    FIELD_ULASAN = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'ulasan')]")
    TOMBOL_KIRIM_ULASAN = (AppiumBy.ACCESSIBILITY_ID, "Kirim ulasan")

    # ─── Layanan Terkait ───
    LAYANAN_TERKAIT = (AppiumBy.XPATH,
        "(//android.view.View[contains(@content-desc, 'Layanan •')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_halaman_bpjs_displayed(self) -> bool:
        """Cek halaman detail layanan JKN terbuka."""
        return self.is_element_displayed(self.JUDUL_HALAMAN, timeout=5)

    def is_konten_nasional_displayed(self) -> bool:
        return self.is_element_displayed(self.KONTEN_NASIONAL, timeout=3)

    def tap_website_bpjs(self):
        self.scroll_and_tap(self.TOMBOL_WEBSITE, max_swipes=5)

    def tap_pertanyaan_layanan(self):
        self.scroll_and_tap(self.CARD_JKN, max_swipes=8)

    def tap_beri_rating(self):
        self.scroll_and_tap(self.BERI_RATING, max_swipes=8)

    def isi_dan_kirim_ulasan(self, teks: str):
        self.scroll_and_tap(self.FIELD_ULASAN, max_swipes=10)
        self.type_text(self.FIELD_ULASAN, teks)
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        self.scroll_and_tap(self.TOMBOL_KIRIM_ULASAN, max_swipes=3)

    def tap_layanan_terkait(self):
        self.scroll_and_tap(self.LAYANAN_TERKAIT, max_swipes=10)
