from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class BpomPage(BasePage):
    """
    Page Object untuk fitur Pengecekan Produk BPOM.
    
    CATATAN: Fitur ini membuka halaman SEARCH RESULTS dengan query 'Pengecekan Produk BPOM',
    bukan halaman BPOM product checker dengan input field.
    Flow: Beranda → Topik Populer → 'Pengecekan Produk BPOM'
          → Search Results page → tap card → Detail Layanan BPOM
    """

    # ─── Entry point ───
    ITEM_BPOM = (AppiumBy.ACCESSIBILITY_ID, "Pengecekan Produk BPOM")

    # ─── Halaman Search Results (setelah tap Pengecekan Produk BPOM) ───
    HEADER_PENCARIAN = (AppiumBy.ACCESSIBILITY_ID, "Pencarian")
    CHIP_SEMUA = (AppiumBy.XPATH,
        "//*[starts-with(@content-desc, 'Semua')]")
    CHIP_LAYANAN = (AppiumBy.XPATH,
        "//*[starts-with(@content-desc, 'Layanan')]")

    # ─── Card hasil pencarian BPOM ───
    CARD_BPOM = (AppiumBy.XPATH,
        "//android.widget.ImageView[contains(@content-desc, 'Pengecekan Produk BPOM')]")
    CARD_BPOM_LAYANAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'LAYANAN NASIONAL') and "
        "contains(@content-desc, 'Pengecekan Produk BPOM')]")

    # ─── Halaman Detail Layanan BPOM ───
    JUDUL_DETAIL_BPOM = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'BPOM') or contains(@content-desc, 'Produk')]")
    KONTEN_ONLINE = (AppiumBy.ACCESSIBILITY_ID, "ONLINE")
    TOMBOL_WEBSITE = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Website') or contains(@content-desc, 'Akses Layanan')]")
    PERTANYAAN_LAYANAN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Pertanyaan Seputar Layanan')]")
    BERI_RATING = (AppiumBy.ACCESSIBILITY_ID, "Beri Rating")
    LAYANAN_TERKAIT = (AppiumBy.XPATH,
        "(//android.view.View[contains(@content-desc, 'Layanan •')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_search_results_displayed(self) -> bool:
        """Cek halaman search results terbuka."""
        return self.is_element_displayed(self.HEADER_PENCARIAN, timeout=5)

    def is_card_bpom_displayed(self) -> bool:
        return (self.is_element_displayed(self.CARD_BPOM, timeout=3) or
                self.is_element_displayed(self.CARD_BPOM_LAYANAN, timeout=3))

    def tap_card_bpom(self):
        """Tap card BPOM untuk buka Detail Layanan."""
        try:
            self.scroll_and_tap(self.CARD_BPOM, max_swipes=3)
        except Exception:
            self.scroll_and_tap(self.CARD_BPOM_LAYANAN, max_swipes=3)

    def is_detail_bpom_displayed(self) -> bool:
        return self.is_element_displayed(self.JUDUL_DETAIL_BPOM, timeout=5)

    def tap_chip_layanan(self):
        try:
            self.tap(self.CHIP_LAYANAN)
        except Exception:
            pass

    def tap_website_bpom(self):
        self.scroll_and_tap(self.TOMBOL_WEBSITE, max_swipes=5)

    def tap_beri_rating(self):
        self.scroll_and_tap(self.BERI_RATING, max_swipes=8)
