from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage

class SearchPage(BasePage):
    # Locators — verified against DOM dumps
    SEARCH_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    # Filter & Sort buttons — confirmed as android.widget.Button with content-desc
    TOMBOL_FILTER = (AppiumBy.ACCESSIBILITY_ID, "Filter")
    # Sort button alternates between 'Terbaru' (default) and 'A-Z'
    TOMBOL_SORT_AZ = (AppiumBy.XPATH, "//*[@content-desc='Terbaru' or @content-desc='A-Z']")
    # Category chips — confirmed format from DOM: "Layanan\n0", "Informasi\n2"
    CHIP_LAYANAN = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Layanan\n')]")
    CHIP_INFORMASI = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Informasi\n')]")
    # Clear button inside EditText
    CLEAR_SEARCH_BUTTON = (AppiumBy.XPATH, "//android.widget.EditText/android.widget.Button[1]")
    # Empty state — "Tidak ada" / "tidak ditemukan" / "Belum ada"
    EMPTY_STATE_INDICATOR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak ditemukan') or "
        "contains(@content-desc, 'Tidak ada') or "
        "contains(@content-desc, 'Tidak ditemukan') or "
        "contains(@content-desc, 'Belum ada') or "
        "contains(@content-desc, 'tidak cocok') or "
        "contains(@content-desc, 'hasil')]")
    # Detail page indicators
    DETAIL_LAYANAN_INDICATOR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Detail') or contains(@content-desc, 'Bagikan')]")
    # "Lihat detail" button on search result cards
    HASIL_PENCARIAN_PERTAMA = (AppiumBy.XPATH, "(//*[@content-desc='Lihat detail'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_keyword(self, keyword: str):
        self.type_text(self.SEARCH_FIELD, keyword)
        try:
            self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        except Exception:
            pass
        self.driver.press_keycode(66)

    def tap_filter(self):
        self.tap(self.TOMBOL_FILTER)

    def tap_sort_az(self):
        self.tap(self.TOMBOL_SORT_AZ)

    def tap_hasil_pencarian_pertama(self):
        self.scroll_and_tap(self.HASIL_PENCARIAN_PERTAMA)

    def tap_kategori_layanan(self):
        self.tap(self.CHIP_LAYANAN)

    def tap_kategori_informasi(self):
        self.tap(self.CHIP_INFORMASI)

    def clear_search(self):
        try:
            self.tap(self.CLEAR_SEARCH_BUTTON, timeout=3)
        except Exception:
            element = self.find_element(self.SEARCH_FIELD)
            element.clear()

    def is_empty_state_displayed(self, timeout: int = 5) -> bool:
        return self.is_element_displayed(self.EMPTY_STATE_INDICATOR, timeout=timeout)

    def is_detail_layanan_displayed(self, timeout: int = 5) -> bool:
        return self.is_element_displayed(self.DETAIL_LAYANAN_INDICATOR, timeout=timeout)

    def get_search_field_text(self) -> str:
        element = self.find_element(self.SEARCH_FIELD)
        return element.text
