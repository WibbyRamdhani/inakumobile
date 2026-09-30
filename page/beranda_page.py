from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class BerandaPage(BasePage):
    # ─── Header ───
    TOMBOL_BURGER_MENU = (AppiumBy.XPATH, "(//android.widget.Button)[1]")
    TOMBOL_MASUK_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Masuk")
    TOMBOL_PILIH_WILAYAH = (AppiumBy.ACCESSIBILITY_ID, "Pilih Wilayah")

    # ─── Beranda Content ───
    JUDUL_BERANDA = (AppiumBy.ACCESSIBILITY_ID, "Layanan apa yang Anda butuhkan hari ini?")
    TOMBOL_PENCARIAN = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    TOMBOL_CARI_ICON = (AppiumBy.ACCESSIBILITY_ID, "Cari")

    # ─── Section Headers ───
    SECTION_LAYANAN_POPULER = (AppiumBy.ACCESSIBILITY_ID, "Layanan Populer")
    SECTION_LAYANAN_POPULER_NASIONAL = (AppiumBy.ACCESSIBILITY_ID, "Layanan Populer Nasional")
    SECTION_TOPIK_POPULER = (AppiumBy.ACCESSIBILITY_ID, "Topik Populer")
    SECTION_JELAJAHI_LAYANAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Kesehatan') and contains(@content-desc, 'Layanan')]")
    SECTION_INFO_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Info Layanan Terbaru")

    # ─── Section Login Only ───
    SECTION_BENEFIT = (AppiumBy.ACCESSIBILITY_ID, "Benefit Anda")
    SECTION_E_DOKUMEN = (AppiumBy.ACCESSIBILITY_ID, "E-Dokumen")

    # ─── Layanan Populer Items (dari UI dump) ───
    ITEM_AKTA_KELAHIRAN = (AppiumBy.ACCESSIBILITY_ID, "Pengurusan Akta Kelahiran")
    ITEM_FASKES = (AppiumBy.ACCESSIBILITY_ID, "Pencarian Fasilitas Layanan Kesehatan")
    ITEM_PENCARIAN_DOKTER = (AppiumBy.ACCESSIBILITY_ID, "Pencarian Dokter")
    ITEM_BPJS = (AppiumBy.ACCESSIBILITY_ID, "Informasi Status Kepesertaan JKN")
    ITEM_ZAKAT = (AppiumBy.ACCESSIBILITY_ID, "Zakat dan Infak")
    ITEM_CEK_BANSOS = (AppiumBy.ACCESSIBILITY_ID, "Mengecek Bantuan Sosial")
    ITEM_LAYANAN_POPULER = (AppiumBy.XPATH, "(//android.view.View[@clickable='true' and ("
        "contains(@content-desc, 'Pengurusan Akta') or "
        "contains(@content-desc, 'Pencarian Fasilitas') or "
        "contains(@content-desc, 'Pencarian Dokter') or "
        "contains(@content-desc, 'Kepesertaan JKN') or "
        "contains(@content-desc, 'Zakat') or "
        "contains(@content-desc, 'Bantuan Sosial'))])[1]")
    TOMBOL_LIHAT_SEMUA = (AppiumBy.ACCESSIBILITY_ID, "Lihat semua")

    # ─── Topik Populer ───
    ITEM_TOPIK_POPULER = (AppiumBy.XPATH, 
        "(//android.view.View[@content-desc='Topik Populer']/"
        "following-sibling::*[@clickable='true'])[1]")
    ITEM_TOPIK_BPOM = (AppiumBy.ACCESSIBILITY_ID, "Pengecekan Produk BPOM")

    # ─── Jelajahi Layanan / Kategori ───
    KATEGORI_KESEHATAN_GIZI = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Kesehatan') and contains(@content-desc, 'Layanan')]")
    KATEGORI_KEPENDUDUKAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Kependudukan') and contains(@content-desc, 'Layanan')]")

    # ─── Info Layanan Terbaru ───
    ITEM_INFO_LAYANAN = (AppiumBy.XPATH, 
        "(//android.widget.ImageView[contains(@content-desc, 'Test_Info') or "
        "contains(@content-desc, 'UNICEF') or "
        "contains(@content-desc, 'Pemerintah')])[1]")
    TOMBOL_LIHAT_SEMUA_INFO = (AppiumBy.ACCESSIBILITY_ID, "Lihat semua informasi")
    DETAIL_INFO_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Detail Informasi")
    DETAIL_LAYANAN_PAGE = (AppiumBy.ACCESSIBILITY_ID, "Detail Layanan")

    # ─── Benefit ───
    CAROUSEL_BENEFIT = (AppiumBy.XPATH, "//android.view.View[@content-desc='Benefit']/following-sibling::android.widget.HorizontalScrollView")
    ITEM_BENEFIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Rp")')
    TOMBOL_LIHAT_SEMUA_BENEFIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Lihat semua benefit")')
    TOMBOL_FILTER = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Filter")')
    TOMBOL_SORT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Sort")')
    KATEGORI_SEMUA = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionStartsWith("Semua")')
    KATEGORI_BANTUAN_SOSIAL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionStartsWith("Bantuan Sosial")')
    KATEGORI_PENDIDIKAN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionStartsWith("Pendidikan")')

    # ─── E-Dokumen ───
    CAROUSEL_EDOKUMEN = (AppiumBy.CLASS_NAME, "android.widget.HorizontalScrollView")
    ITEM_EDOKUMEN = (AppiumBy.XPATH, "//android.widget.HorizontalScrollView/android.view.View[1]")
    TOMBOL_UNDUH_DOKUMEN = (AppiumBy.ACCESSIBILITY_ID, "Unduh dokumen")
    TOMBOL_LIHAT_DOKUMEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Lihat Dokumen")')
    TOMBOL_LIHAT_SEMUA_EDOKUMEN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Lihat semua dokumen")')
    HALAMAN_PROFIL_EDOKUMEN = (AppiumBy.ACCESSIBILITY_ID, "Profil E-Dokumen")

    # ─── Pencarian (hasil) ───
    HASIL_PENCARIAN_LAYANAN = (AppiumBy.XPATH, 
        "(//android.view.View[contains(@content-desc, 'Menampilkan hasil pencarian')]/"
        "following-sibling::*[@clickable='true'])[1]")

    # ─── Sidebar ───
    SIDEBAR_BERANDA = (AppiumBy.XPATH, "//android.widget.FrameLayout[@pane-title='Navigation menu']//android.view.View[@content-desc='Beranda']")
    SIDEBAR_LAYANAN_PUBLIK = (AppiumBy.XPATH, "//android.widget.FrameLayout[@pane-title='Navigation menu']//android.view.View[@content-desc='Layanan Publik']")
    SIDEBAR_INFORMASI_LAYANAN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@pane-title='Navigation menu']//android.view.View[@content-desc='Informasi Layanan']")
    SIDEBAR_ADUAN_BANTUAN = (AppiumBy.XPATH, "//android.widget.FrameLayout[@pane-title='Navigation menu']//android.view.View[@content-desc='Aduan dan Bantuan']")

    # ─── Pagination ───
    PAGINATION_FIRST = (AppiumBy.XPATH, "//android.view.View[@content-desc='1']/../android.view.View[1]")
    PAGINATION_PREV = (AppiumBy.XPATH, "//android.view.View[@content-desc='1']/../android.view.View[2]")
    PAGINATION_NEXT = (AppiumBy.XPATH, "//android.view.View[@content-desc='1']/../android.view.View[last()-1]")
    PAGINATION_LAST = (AppiumBy.XPATH, "//android.view.View[@content-desc='1']/../android.view.View[last()]")

    ITEM_INFORMASI_TERKAIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionMatches("(?i).*informasi terkait.*")')
    TOMBOL_FAQ = (AppiumBy.ACCESSIBILITY_ID, "Lihat pertanyaan umum")
    TOMBOL_LIHAT_SEMUA_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Lihat semua layanan")

    def __init__(self, driver):
        super().__init__(driver)

    def tap_masuk_header(self):
        self.tap(self.TOMBOL_MASUK_HEADER)

    def tap_pencarian_dummy(self):
        self.tap(self.TOMBOL_PENCARIAN)

    def tap_pencarian(self):
        self.tap(self.TOMBOL_PENCARIAN)

    def input_pencarian(self, text):
        self.type_text(self.TOMBOL_PENCARIAN, text)
        try:
            self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        except:
            pass
        self.driver.press_keycode(66)
        
    def tap_hasil_pencarian(self):
        self.tap(self.HASIL_PENCARIAN_LAYANAN)

    def tap_faq(self):
        self.tap(self.TOMBOL_FAQ)

    def is_beranda_displayed(self) -> bool:
        """Cek apakah beranda tampil (ada judul atau layanan populer)."""
        return (self.is_element_displayed(self.JUDUL_BERANDA, timeout=5) or
                self.is_element_displayed(self.SECTION_LAYANAN_POPULER, timeout=3))

    def is_beranda_standar_displayed(self) -> bool:
        return self.is_element_displayed(self.SECTION_LAYANAN_POPULER, timeout=5)

    def is_beranda_nonlogin_displayed(self) -> bool:
        benefit = self.is_element_displayed(self.SECTION_BENEFIT, timeout=5)
        edokumen = self.is_element_displayed(self.SECTION_E_DOKUMEN, timeout=5)
        return (not benefit and not edokumen and self.is_beranda_standar_displayed())

    def is_benefit_section_displayed(self) -> bool:
        return self.is_element_displayed(self.SECTION_BENEFIT, timeout=5)

    def is_edokumen_section_displayed(self) -> bool:
        return self.is_element_displayed(self.SECTION_E_DOKUMEN, timeout=5)

    def scroll_carousel_benefit(self):
        try:
            element = self.find_element(self.SECTION_BENEFIT, timeout=5)
            y = element.location['y']
            y_carousel = y + 400 
        except:
            element = self.find_element(self.ITEM_BENEFIT, timeout=5)
            y = element.location['y']
            y_carousel = y + 100

        window_size = self.driver.get_window_size()
        start_x = window_size['width'] * 0.8
        end_x = window_size['width'] * 0.2
        self.driver.swipe(start_x, y_carousel, end_x, y_carousel, 600)
        
    def tap_item_benefit(self):
        self.tap(self.ITEM_BENEFIT)
        
    def tap_lihat_semua_benefit(self):
        self.tap(self.TOMBOL_LIHAT_SEMUA_BENEFIT)

    def tap_pagination_benefit(self, action="next"):
        if action == "next":
            self.tap(self.PAGINATION_NEXT)
        elif action == "prev":
            self.tap(self.PAGINATION_PREV)
        elif action == "first":
            self.tap(self.PAGINATION_FIRST)
        elif action == "last":
            self.tap(self.PAGINATION_LAST)
            
    def tap_filter_benefit(self):
        self.tap(self.TOMBOL_FILTER)
        
    def tap_sort_benefit(self):
        self.tap(self.TOMBOL_SORT)
        
    def pilih_kategori_benefit(self, kategori="semua"):
        if kategori == "semua":
            self.tap(self.KATEGORI_SEMUA)
        elif kategori == "bantuan sosial":
            self.tap(self.KATEGORI_BANTUAN_SOSIAL)
        elif kategori == "pendidikan":
            self.tap(self.KATEGORI_PENDIDIKAN)
            
    def scroll_carousel_edokumen(self):
        self.driver.swipe(800, 1200, 200, 1200)

    def scroll_ke_bawah(self):
        self.swipe_down()
        
    def tap_item_edokumen(self):
        self.scroll_to_element(self.SECTION_E_DOKUMEN)
        self.tap(self.SECTION_E_DOKUMEN)
        self.tap(self.ITEM_EDOKUMEN)
        
    def tap_lihat_dokumen(self):
        self.scroll_and_tap(self.TOMBOL_LIHAT_DOKUMEN, max_swipes=25)
        
    def tap_unduh_dokumen(self):
        self.tap(self.TOMBOL_UNDUH_DOKUMEN)
        
    def tap_lihat_semua_edokumen(self):
        self.scroll_to_element(self.SECTION_E_DOKUMEN)
        self.tap(self.SECTION_E_DOKUMEN)
        self.tap(self.TOMBOL_LIHAT_SEMUA_EDOKUMEN)
        
    def is_profil_edokumen_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_PROFIL_EDOKUMEN, timeout=5)

    def tap_item_layanan_populer(self):
        self.scroll_and_tap(self.ITEM_LAYANAN_POPULER, max_swipes=3)
        
    def tap_lihat_semua_layanan_populer(self):
        self.scroll_and_tap(self.TOMBOL_LIHAT_SEMUA, max_swipes=3)
        
    def tap_item_topik_populer(self):
        self.scroll_and_tap(self.ITEM_TOPIK_POPULER, max_swipes=3)
        
    def tap_kategori_kesehatan(self):
        self.scroll_and_tap(self.KATEGORI_KESEHATAN_GIZI, max_swipes=8)
        
    def tap_lihat_semua_jelajahi_layanan(self):
        self.scroll_and_tap(self.TOMBOL_LIHAT_SEMUA, max_swipes=5)
        
    def tap_pencarian_dokter(self):
        self.scroll_and_tap(self.ITEM_PENCARIAN_DOKTER, max_swipes=8)
        
    def tap_item_info_layanan(self):
        self.scroll_and_tap(self.ITEM_INFO_LAYANAN, max_swipes=5)
        
    def tap_informasi_terkait(self):
        self.scroll_and_tap(self.ITEM_INFORMASI_TERKAIT, max_swipes=3)
        
    def tap_lihat_semua_info_layanan(self):
        self.scroll_and_tap(self.TOMBOL_LIHAT_SEMUA_INFO, max_swipes=5)
        
    def tap_back(self):
        self.driver.back()

    def safe_tap_back(self):
        try:
            self.driver.back()
        except Exception:
            self.driver.press_keycode(4)

    def open_sidebar(self):
        self.tap(self.TOMBOL_BURGER_MENU)
        time.sleep(1)

    def tap_sidebar_item(self, item_name):
        locator = (AppiumBy.XPATH, 
            f"//android.widget.FrameLayout[@pane-title='Navigation menu']"
            f"//android.view.View[@content-desc='{item_name}']")
        self.tap(locator)
