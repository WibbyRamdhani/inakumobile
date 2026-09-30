from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class LayananPage(BasePage):
    """
    Page Object untuk halaman Layanan Publik.
    Diakses via bottom tab "Layanan" atau sidebar "Layanan Publik".
    
    UI Reference: ui_dumps/layanan_actual.xml
    """

    # ─── Breadcrumb ───
    BREADCRUMB_BERANDA = (AppiumBy.XPATH, 
        "//android.widget.ScrollView//android.view.View[@content-desc='Beranda']")
    BREADCRUMB_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Layanan Publik")

    # ─── Page Header ───
    JUDUL_LAYANAN = (AppiumBy.XPATH, 
        "//android.view.View[@content-desc='Layanan Publik' and @clickable='false']")

    # ─── Search & Filter ───
    SEARCH_FIELD = (AppiumBy.XPATH, 
        "//android.widget.EditText[@hint='Cari layanan atau program']")
    TOMBOL_FILTER = (AppiumBy.ACCESSIBILITY_ID, "Filter")
    TOMBOL_SORT_TERBARU = (AppiumBy.ACCESSIBILITY_ID, "Terbaru")

    # ─── Kategori (HorizontalScrollView) ───
    KATEGORI_SEMUA = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Semua')]")
    KATEGORI_BANTUAN_SOSIAL = (AppiumBy.XPATH, 
        "//*[contains(@content-desc, 'Bantuan Sosial')]")
    KATEGORI_PENDIDIKAN = (AppiumBy.XPATH, 
        "//*[contains(@content-desc, 'Pendidikan')]")
    KATEGORI_KESEHATAN = (AppiumBy.XPATH, 
        "//*[contains(@content-desc, 'Kesehatan')]")

    # ─── Layanan Cards ───
    LAYANAN_PERTAMA = (AppiumBy.XPATH, 
        "(//android.widget.ImageView[starts-with(@content-desc, 'LAYANAN')])[1]")
    DETAIL_LAYANAN_LIHAT = (AppiumBy.XPATH, 
        "(//*[@content-desc='Lihat detail'])[1]")

    # ─── Info Banner ───
    INFO_WILAYAH = (AppiumBy.XPATH, 
        "//*[contains(@content-desc, 'melihat layanan dari wilayah')]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_layanan(self, text):
        """Cari layanan dengan keyword."""
        self.type_text(self.SEARCH_FIELD, text)
        try:
            self.driver.execute_script(
                'mobile: performEditorAction', {'action': 'search'})
        except Exception:
            self.driver.press_keycode(66)
        time.sleep(2)

    def tap_filter(self):
        self.tap(self.TOMBOL_FILTER)

    def tap_sort(self):
        self.tap(self.TOMBOL_SORT_TERBARU)

    def pilih_kategori_bantuan_sosial(self):
        self.tap(self.KATEGORI_BANTUAN_SOSIAL)

    def pilih_kategori_pendidikan(self):
        self.tap(self.KATEGORI_PENDIDIKAN)

    def pilih_kategori_kesehatan(self):
        self.tap(self.KATEGORI_KESEHATAN)

    def tap_kategori(self, nama_kategori="Semua"):
        """Tap kategori berdasarkan nama."""
        if nama_kategori.lower() == "semua":
            self.tap(self.KATEGORI_SEMUA)
        else:
            locator = (AppiumBy.XPATH, 
                f"//*[contains(@content-desc, '{nama_kategori}')]")
            self.tap(locator)

    def buka_detail_layanan_pertama(self):
        """Buka detail layanan pertama yang muncul."""
        if self.is_element_displayed(self.DETAIL_LAYANAN_LIHAT, timeout=3):
            self.scroll_and_tap(self.DETAIL_LAYANAN_LIHAT, max_swipes=3)
        else:
            self.scroll_and_tap(self.LAYANAN_PERTAMA, max_swipes=3)

    def tap_layanan_pertama(self):
        self.scroll_and_tap(self.LAYANAN_PERTAMA, max_swipes=3)

    def is_layanan_page_displayed(self, timeout=5):
        return self.is_element_displayed(self.BREADCRUMB_LAYANAN, timeout=timeout)

    def get_jumlah_layanan(self):
        """Get jumlah layanan dari text."""
        try:
            elements = self.driver.find_elements(
                AppiumBy.XPATH, "//*[contains(@content-desc, 'Layanan')]")
            for el in elements:
                desc = el.get_attribute('content-desc') or ''
                if 'Layanan' in desc and any(c.isdigit() for c in desc):
                    return desc
        except Exception:
            pass
        return None

    def tap_breadcrumb_beranda(self):
        self.tap(self.BREADCRUMB_BERANDA)