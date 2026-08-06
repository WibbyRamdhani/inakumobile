from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage

class LayananPage(BasePage):
    # Locators
    # Hint berubah: di halaman Layanan tab, field cari punya hint berbeda
    SEARCH_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    TOMBOL_FILTER = (AppiumBy.ACCESSIBILITY_ID, "Filter")
    TOMBOL_SORT = (AppiumBy.XPATH, "//*[@content-desc='A-Z' or @content-desc='Terbaru']")
    TOMBOL_KATEGORI = (AppiumBy.ACCESSIBILITY_ID, "Kategori")
    KATEGORI_BANTUAN_SOSIAL = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Bantuan Sosial')]")
    # Kartu layanan: content-desc starts with "LAYANAN\n" or "Layanan\n"
    LAYANAN_PERTAMA = (AppiumBy.XPATH, "(//*[starts-with(@content-desc, 'LAYANAN') or starts-with(@content-desc, 'Layanan')])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_layanan(self, keyword: str):
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
        self.scroll_and_tap(self.LAYANAN_PERTAMA)