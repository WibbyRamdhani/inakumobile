from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class SearchPage(BasePage):
    """
    Page Object untuk halaman Cari (Search).
    Diakses via bottom tab "Cari".
    
    UI Reference: ui_dumps/cari_actual.xml
    """

    # ─── Search Field ───
    SEARCH_FIELD = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    
    # ─── Filter & Sort ───
    TOMBOL_FILTER = (AppiumBy.ACCESSIBILITY_ID, "Filter")
    TOMBOL_SORT = (AppiumBy.XPATH, 
        "//android.widget.Button[contains(@content-desc, 'Terbaru') or "
        "contains(@content-desc, 'A-Z')]")
    
    # ─── Category chips (format: "Semua\n2", "Layanan\n0", "Informasi\n2") ───
    CHIP_SEMUA = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Semua')]")
    CHIP_LAYANAN = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Layanan\n')]")
    CHIP_INFORMASI = (AppiumBy.XPATH, "//*[starts-with(@content-desc, 'Informasi\n')]")
    
    # ─── Search results ───
    # Hasil pencarian: card clickable besar (android.view.View dengan content-desc panjang)
    # Chip kategori punya format "Semua\n2", "Layanan\n0", "Informasi\n2" (starts-with)
    # Kartu hasil punya format "Informasi Layanan\n..." (panjang, tidak starts-with chip pattern)
    HASIL_PENCARIAN_PERTAMA = (AppiumBy.XPATH, 
        "(//android.view.View[@clickable='true' and "
        "string-length(@content-desc) > 20 and "
        "not(starts-with(@content-desc, 'Tab')) and "
        "not(starts-with(@content-desc, 'Beranda')) and "
        "not(starts-with(@content-desc, 'Cari')) and "
        "not(starts-with(@content-desc, 'Layanan')) and "
        "not(starts-with(@content-desc, 'Informasi')) and "
        "not(starts-with(@content-desc, 'Semua')) and "
        "not(starts-with(@content-desc, 'Pilih')) and "
        "not(starts-with(@content-desc, 'Filter')) and "
        "not(starts-with(@content-desc, 'Terbaru')) and "
        "not(starts-with(@content-desc, 'A-Z'))])[1]")
    
    # ─── Clear search ───
    CLEAR_SEARCH_BUTTON = (AppiumBy.XPATH, 
        "//android.widget.EditText/android.widget.Button[1]")
    
    # ─── Empty state ───
    EMPTY_STATE_INDICATOR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak ditemukan') or "
        "contains(@content-desc, 'Tidak ada') or "
        "contains(@content-desc, 'Tidak ditemukan') or "
        "contains(@content-desc, 'Belum ada') or "
        "contains(@content-desc, 'tidak cocok') or "
        "contains(@content-desc, 'Coba gunakan kata kunci')]")
    
    # ─── Detail page indicators ───
    DETAIL_INDICATOR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Detail') or "
        "contains(@content-desc, 'Bagikan') or "
        "contains(@content-desc, 'Diterbitkan')]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_keyword(self, keyword: str):
        self.type_text(self.SEARCH_FIELD, keyword)
        try:
            self.driver.execute_script(
                'mobile: performEditorAction', {'action': 'search'})
        except Exception:
            pass
        self.driver.press_keycode(66)
        time.sleep(2)  # Tunggu hasil search muncul

    def tap_filter(self):
        self.tap(self.TOMBOL_FILTER)

    def tap_sort(self):
        """Tap sort button (toggle antara Terbaru dan A-Z)."""
        self.tap(self.TOMBOL_SORT)

    # Alias untuk backward compatibility
    def tap_sort_az(self):
        self.tap_sort()

    def tap_hasil_pencarian_pertama(self):
        """Tap hasil pencarian pertama setelah tunggu hasil muncul."""
        time.sleep(3)  # Tunggu hasil search render sempurna
        self.scroll_and_tap(self.HASIL_PENCARIAN_PERTAMA, max_swipes=3)

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
        return self.is_element_displayed(self.DETAIL_INDICATOR, timeout=timeout)

    def get_search_field_text(self) -> str:
        element = self.find_element(self.SEARCH_FIELD)
        return element.text
