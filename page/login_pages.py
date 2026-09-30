from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time

class LoginPage(BasePage):
    """
    Page Object untuk flow login.
    
    Flow login non-IKD (email):
      Beranda → tap Profil tab → halaman "Masuk Akun" →
      tap "Masuk dengan Email dan Password" → form email/password →
      isi email + password → tap "Masuk dengan Email"
    
    UI Reference: ui_dumps/login_email_form.xml
    """

    # ─── Halaman pilihan login (Masuk Akun) ───
    TOMBOL_MASUK_HEADER = (AppiumBy.ACCESSIBILITY_ID, "Masuk")
    TOMBOL_MASUK_IKD = (AppiumBy.ACCESSIBILITY_ID, "Masuk dengan akun IKD")
    TOMBOL_MASUK_EMAIL_PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Masuk dengan Email dan Password")

    # ─── Halaman login email (form) ───
    LOGIN_PAGE_INDICATOR = (AppiumBy.ACCESSIBILITY_ID, "Masuk ke akun Anda")
    EMAIL_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@hint='Masukkan alamat email']")
    PASSWORD_FIELD = (AppiumBy.XPATH, "//android.widget.EditText[@password='true']")
    TOMBOL_MASUK = (AppiumBy.ACCESSIBILITY_ID, "Masuk dengan Email")
    TOGGLE_PASSWORD = (AppiumBy.XPATH, "//android.widget.EditText[@password='true']/android.widget.Button")
    LINK_DAFTAR_SEKARANG = (AppiumBy.ACCESSIBILITY_ID, "Belum memiliki akun? Daftar sekarang")
    TOMBOL_KEMBALI_KE_IKD = (AppiumBy.ACCESSIBILITY_ID, "Masuk menggunakan akun IKD")

    # ─── Indikator berhasil login (beranda setelah login) ───
    # Setelah login, user di-redirect ke beranda yang punya section khusus user
    HOME_INDICATOR = (AppiumBy.ACCESSIBILITY_ID, "Layanan apa yang Anda butuhkan hari ini?")

    # ─── Error messages ───
    ERROR_NO_INTERNET = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'internet') or "
        "contains(@content-desc, 'network') or "
        "contains(@content-desc, 'koneksi')]")
    ERROR_EMPTY_FIELDS = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'wajib') or "
        "contains(@content-desc, 'harus') or "
        "contains(@content-desc, 'required')]")
    ERROR_INVALID_LOGIN = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'salah') or "
        "contains(@content-desc, 'tidak valid') or "
        "contains(@content-desc, 'invalid') or "
        "contains(@content-desc, 'gagal') or "
        "contains(@content-desc, 'incorrect')]")

    def __init__(self, driver):
        super().__init__(driver)

    # ─── NAVIGASI ─────────────────────────────────────────────────────

    def navigate_to_login(self):
        """
        Navigasi ke halaman login email.
        Handle 3 state: (1) sudah di login form, (2) belum login, (3) sudah login.
        Jika logged in, clear app data via ADB karena tidak ada tombol logout di UI.
        """
        # Shortcut: sudah di halaman login email?
        if self.is_element_displayed(self.LOGIN_PAGE_INDICATOR, timeout=2):
            return

        # Shortcut: sudah di halaman pilihan login?
        if self.is_element_displayed(self.TOMBOL_MASUK_EMAIL_PASSWORD, timeout=2):
            self.tap(self.TOMBOL_MASUK_EMAIL_PASSWORD)
            time.sleep(1)
            self.find_element(self.LOGIN_PAGE_INDICATOR, timeout=5)
            return

        # Normal flow: tap tab Profil
        self.go_to_profil()
        time.sleep(1.5)

        # Case A: Belum login — tombol "Masuk dengan Email dan Password" muncul
        if self.is_element_displayed(self.TOMBOL_MASUK_EMAIL_PASSWORD, timeout=3):
            self.tap(self.TOMBOL_MASUK_EMAIL_PASSWORD)
            time.sleep(1)
            self.find_element(self.LOGIN_PAGE_INDICATOR, timeout=5)
            return

        # Case B: Sudah login — scroll ke bawah untuk cari 'Keluar dari Akun'
        self._logout_from_profil()
        time.sleep(2)
        
        # Setelah logout, go to Profil → login
        self.go_to_profil()
        time.sleep(1.5)
        if self.is_element_displayed(self.TOMBOL_MASUK_EMAIL_PASSWORD, timeout=5):
            self.tap(self.TOMBOL_MASUK_EMAIL_PASSWORD)
            time.sleep(1)
        self.find_element(self.LOGIN_PAGE_INDICATOR, timeout=10)

    def _logout_from_profil(self):
        """Scroll ke bawah di Profil, tap 'Keluar dari Akun', lalu confirm di popup."""
        TOMBOL_KELUAR_AKUN = (AppiumBy.ACCESSIBILITY_ID, "Keluar dari Akun")
        TOMBOL_KONFIRMASI = (AppiumBy.ACCESSIBILITY_ID, "Keluar")

        # Scroll sampai ketemu tombol 'Keluar dari Akun'
        for _ in range(15):
            if self.is_element_displayed(TOMBOL_KELUAR_AKUN, timeout=1):
                self.tap(TOMBOL_KELUAR_AKUN)
                time.sleep(1.5)
                # Handle confirmation popup — tap 'Keluar' di popup
                if self.is_element_displayed(TOMBOL_KONFIRMASI, timeout=3):
                    self.tap(TOMBOL_KONFIRMASI)
                time.sleep(2)
                return
            self.swipe_down()
            time.sleep(0.5)

        # Fallback: langsung tap (misal sudah visible)
        self.tap(TOMBOL_KELUAR_AKUN, timeout=5)
        time.sleep(1.5)
        if self.is_element_displayed(TOMBOL_KONFIRMASI, timeout=3):
            self.tap(TOMBOL_KONFIRMASI)
        time.sleep(2)

    def navigate_to_login_ikd(self):
        """Navigasi ke halaman login IKD dari beranda."""
        self.go_to_profil()
        time.sleep(1)
        if self.is_element_displayed(self.TOMBOL_MASUK_IKD, timeout=5):
            self.tap(self.TOMBOL_MASUK_IKD)
            time.sleep(1)

    # ─── INPUT ────────────────────────────────────────────────────────

    def enter_email(self, email: str):
        self.type_text(self.EMAIL_FIELD, email)

    def enter_password(self, password: str):
        self.type_text(self.PASSWORD_FIELD, password)

    def tap_login_button(self):
        self.tap(self.TOMBOL_MASUK)

    def tap_toggle_password(self):
        self.tap(self.TOGGLE_PASSWORD)

    # ─── ACTIONS ──────────────────────────────────────────────────────

    def login(self, email: str, password: str):
        """Input email + password dan submit. Panggil setelah navigate_to_login()."""
        self.enter_email(email)
        self.enter_password(password)
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass
        self.tap_login_button()

    def full_login(self, email: str, password: str):
        """Login lengkap dari beranda: navigasi + input + submit."""
        self.navigate_to_login()
        self.login(email, password)

    def logout(self):
        """Logout via tombol 'Keluar dari Akun' di halaman Profil."""
        self.go_to_profil()
        time.sleep(1.5)
        self._logout_from_profil()

    # ─── ASSERTIONS ───────────────────────────────────────────────────

    def is_login_page_displayed(self, timeout=5):
        return self.is_element_displayed(self.LOGIN_PAGE_INDICATOR, timeout=timeout)

    def is_home_screen_displayed(self, timeout=8):
        """Cek apakah beranda tampil (berhasil login atau kembali ke beranda)."""
        return self.is_element_displayed(self.HOME_INDICATOR, timeout=timeout)

    def is_no_internet_error_displayed(self):
        return self.is_element_displayed(self.ERROR_NO_INTERNET, timeout=5)

    def is_empty_fields_error_displayed(self):
        return self.is_element_displayed(self.ERROR_EMPTY_FIELDS, timeout=5)

    def is_invalid_login_error_displayed(self):
        return self.is_element_displayed(self.ERROR_INVALID_LOGIN, timeout=5)

    def is_still_on_login_page(self, timeout=3):
        """Cek apakah masih di halaman login (login gagal)."""
        return self.is_element_displayed(self.LOGIN_PAGE_INDICATOR, timeout=timeout)
