from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage

class DetailLayananPage(BasePage):
    # --- Elemen Dasar Halaman ---
    JUDUL_LAYANAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Mengecek Bantuan Sosial') or contains(@text, 'Mengecek Bantuan Sosial') or contains(@content-desc, 'Detail') or contains(@content-desc, 'Bagikan')]")
    TOMBOL_BAGIKAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Bagikan') or contains(@text, 'Bagikan')]")
    TAB_PERSYARATAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Persyaratan') or contains(@text, 'Persyaratan')]")
    TAB_CARA_MENGAKSES = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Cara Mengakses') or contains(@text, 'Cara Mengakses')]")
    TAB_INFO_TAMBAHAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Informasi Tambahan') or contains(@text, 'Informasi Tambahan')]")
    TOMBOL_KEMENSOS_AKSES = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Kemensos') or contains(@text, 'Kemensos')]")
    QNA_TERATAS = (AppiumBy.XPATH, "(//*[contains(@content-desc, '?') or contains(@text, '?')])[1]")
    TOMBOL_TIDAK_MENEMUKAN_JAWABAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Tidak menemukan jawaban') or contains(@text, 'Tidak menemukan jawaban')]")
    KARTU_LAYANAN_TERKAIT_TERATAS = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Layanan')])[last()]") 
    TOMBOL_BERI_RATING = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Beri Rating') or contains(@text, 'Beri Rating')]")
    BINTANG_5 = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Beri Rating')]/following-sibling::android.view.View[@clickable='true'])[5]")
    KOLOM_ULASAN = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    TOMBOL_KIRIM_ULASAN = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Kirim ulasan') or contains(@text, 'Kirim ulasan')]")
    ERROR_ULASAN_KOSONG = (AppiumBy.XPATH, "//*[contains(@content-desc, 'wajib diisi') or contains(@content-desc, 'tidak boleh kosong') or contains(@text, 'wajib diisi') or contains(@text, 'tidak boleh kosong')]")
    RT_BOLD = (AppiumBy.ACCESSIBILITY_ID, "B")
    RT_ITALIC = (AppiumBy.ACCESSIBILITY_ID, "I")
    RT_UNDERLINE = (AppiumBy.ACCESSIBILITY_ID, "U")
    PENGADUAN_KEMENSOS = (AppiumBy.XPATH, "(//*[contains(@content-desc, 'Kemensos') or contains(@text, 'Kemensos')])[last()]")
    PENGADUAN_LAPOR = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Website lapor') or contains(@text, 'Website lapor')]")
    UNDUH_PLAYSTORE = (AppiumBy.XPATH, "//*[contains(@content-desc, 'Playstore') or contains(@text, 'Playstore')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_judul_layanan_displayed(self) -> bool:
        return self.is_element_displayed(self.JUDUL_LAYANAN)

    def tap_bagikan(self):
        self.tap(self.TOMBOL_BAGIKAN)

    def navigasi_tab(self, nama_tab: str):
        if nama_tab.lower() == 'persyaratan':
            self.tap(self.TAB_PERSYARATAN)
        elif nama_tab.lower() == 'cara mengakses':
            self.tap(self.TAB_CARA_MENGAKSES)
        elif nama_tab.lower() == 'informasi tambahan':
            self.tap(self.TAB_INFO_TAMBAHAN)
            
    def tap_akses_kemensos(self):
        self.scroll_and_tap(self.TOMBOL_KEMENSOS_AKSES)
        
    def tap_qna_teratas(self):
        self.scroll_and_tap(self.QNA_TERATAS)
            
    def tap_tidak_menemukan_jawaban(self):
        self.scroll_and_tap(self.TOMBOL_TIDAK_MENEMUKAN_JAWABAN)
        
    def tap_layanan_terkait_teratas(self):
        self.scroll_and_tap(self.KARTU_LAYANAN_TERKAIT_TERATAS)
        
    def buka_form_ulasan(self):
        self.scroll_to_element(self.TOMBOL_BERI_RATING)
        self.tap(self.BINTANG_5, timeout=5)

    def buka_form_ulasan_tanpa_bintang(self):
        self.scroll_to_element(self.TOMBOL_BERI_RATING)
        
    def ketik_ulasan(self, teks: str):
        self.tap(self.KOLOM_ULASAN)
        self.type_text(self.KOLOM_ULASAN, teks)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        
    def format_rich_text(self):
        self.scroll_to_element(self.RT_BOLD)
        self.tap(self.RT_BOLD)
        self.tap(self.RT_ITALIC)
        self.tap(self.RT_UNDERLINE)
            
    def kirim_ulasan(self):
        self.tap(self.TOMBOL_KIRIM_ULASAN)
        
    def batal_ulasan(self):
        self.tap(self.TOMBOL_BATAL_ULASAN)
        
    def tap_pengaduan_kemensos(self):
        self.scroll_and_tap(self.PENGADUAN_KEMENSOS)
        
    def tap_pengaduan_lapor(self):
        self.scroll_and_tap(self.PENGADUAN_LAPOR)
        
    def tap_unduh_playstore(self):
        self.scroll_and_tap(self.UNDUH_PLAYSTORE)
