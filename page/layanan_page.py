from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class LayananPage(BasePage):
    # Locators
    # Hint berubah: di halaman Layanan tab, field cari punya hint berbeda
    SEARCH_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    TOMBOL_FILTER = (AppiumBy.ACCESSIBILITY_ID, "Filter")
    TOMBOL_SORT = (AppiumBy.XPATH, "//*[@content-desc='A-Z' or @content-desc='Terbaru']")
    TOMBOL_KATEGORI = (AppiumBy.ACCESSIBILITY_ID, "Kategori")
    KATEGORI_BANTUAN_SOSIAL = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Bantuan Sosial')]")
    # Kartu layanan teratas dari JSON dump: android.widget.ImageView dengan content-desc "LAYANAN\nMengecek Bantuan Sosial..."
    LAYANAN_PERTAMA = (AppiumBy.XPATH, "(//android.widget.ImageView[starts-with(@content-desc, 'LAYANAN')] | //*[@clickable='true' and (starts-with(@content-desc, 'LAYANAN') or starts-with(@content-desc, 'Layanan'))])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_layanan(self, keyword: str):
        # Jika kolom pencarian ter-scroll ke bawah di test sebelumnya, scroll kembali ke atas
        if not self.is_element_displayed(self.SEARCH_FIELD, timeout=1.0):
            self.scroll_to_top()
        self.type_text(self.SEARCH_FIELD, keyword)
        try:
            self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        except Exception:
            pass
        self.driver.press_keycode(66)

    def tap_filter(self):
        self.tap(self.TOMBOL_FILTER)

    def tap_sort(self):
        self.tap(self.TOMBOL_SORT)

    def tap_kategori(self):
        self.tap(self.TOMBOL_KATEGORI)

    def pilih_kategori_bantuan_sosial(self):
        self.tap(self.KATEGORI_BANTUAN_SOSIAL)

    def buka_detail_layanan_pertama(self):
        """Buka detail layanan teratas.
        Jika kartu sudah langsung terlihat di layar atas (seperti posisi setelah test n),
        langsung tekan tombol tersebut. Jika belum terlihat, scroll untuk mencarinya.
        """
        if self.is_element_displayed(self.LAYANAN_PERTAMA, timeout=1.5):
            self.tap(self.LAYANAN_PERTAMA)
            return

        self.scroll_to_element(self.LAYANAN_PERTAMA)
        self.tap(self.LAYANAN_PERTAMA)