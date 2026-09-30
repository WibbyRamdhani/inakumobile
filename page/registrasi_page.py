from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage
import time


class RegistrasiPage(BasePage):
    """
    Page Object untuk fitur Registrasi Non-IKD (daftar akun baru via email).
    Flow: Profil → Masuk Akun → 'Belum punya akun? Daftar sekarang' → Form Registrasi
    """

    # ─── Entry point dari form login ───
    LINK_DAFTAR = (AppiumBy.ACCESSIBILITY_ID,
        "Belum memiliki akun? Daftar sekarang")

    # ─── Halaman Registrasi ───
    HALAMAN_REGISTRASI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Daftar') or contains(@content-desc, 'Registrasi') or "
        "contains(@content-desc, 'Buat Akun')]")

    # ─── Form ───
    FIELD_NAMA = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'nama') or "
        "contains(@hint, 'Nama') or contains(@hint, 'name')]")
    FIELD_EMAIL = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'email') or "
        "contains(@hint, 'Email') or contains(@hint, 'surel')]")
    FIELD_PASSWORD = (AppiumBy.XPATH,
        "(//android.widget.EditText[@password='true'])[1]")
    FIELD_KONFIRMASI_PASSWORD = (AppiumBy.XPATH,
        "(//android.widget.EditText[@password='true'])[2]")
    FIELD_NO_HP = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'nomor') or "
        "contains(@hint, 'HP') or contains(@hint, 'telepon') or contains(@hint, '08')]")
    TOMBOL_DAFTAR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Daftar') or contains(@content-desc, 'Buat Akun') or "
        "contains(@content-desc, 'Register')]")
    CHECKBOX_SETUJU = (AppiumBy.XPATH,
        "//android.widget.CheckBox | //*[contains(@content-desc, 'setuju') or "
        "contains(@content-desc, 'Syarat')]")

    # ─── Validasi error ───
    ERROR_EMAIL_TERDAFTAR = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'sudah terdaftar') or "
        "contains(@content-desc, 'already registered')]")
    ERROR_PASSWORD_TIDAK_COCOK = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'tidak sama') or "
        "contains(@content-desc, 'tidak cocok') or contains(@content-desc, 'mismatch')]")
    ERROR_FIELD_WAJIB = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'wajib') or contains(@content-desc, 'required')]")

    # ─── OTP Verification ───
    FIELD_OTP = (AppiumBy.XPATH,
        "//android.widget.EditText[contains(@hint, 'OTP') or "
        "contains(@hint, 'kode') or contains(@hint, 'verifikasi')]")
    TOMBOL_VERIFIKASI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'Verifikasi') or contains(@content-desc, 'Konfirmasi')]")

    # ─── Sukses ───
    PESAN_SUKSES_REGISTRASI = (AppiumBy.XPATH,
        "//*[contains(@content-desc, 'berhasil') or contains(@content-desc, 'sukses') or "
        "contains(@content-desc, 'Selamat')]")

    def __init__(self, driver):
        super().__init__(driver)

    def tap_link_daftar(self):
        self.tap(self.LINK_DAFTAR)
        time.sleep(1)

    def is_halaman_registrasi_displayed(self) -> bool:
        return self.is_element_displayed(self.HALAMAN_REGISTRASI, timeout=5)

    def isi_form_registrasi(self, nama: str, email: str, password: str,
                             konfirmasi: str, no_hp: str = ""):
        """Isi semua field form registrasi."""
        try:
            self.type_text(self.FIELD_NAMA, nama)
        except Exception:
            pass
        try:
            self.type_text(self.FIELD_EMAIL, email)
        except Exception:
            pass
        try:
            self.type_text(self.FIELD_PASSWORD, password)
        except Exception:
            pass
        try:
            self.type_text(self.FIELD_KONFIRMASI_PASSWORD, konfirmasi)
        except Exception:
            pass
        if no_hp:
            try:
                self.type_text(self.FIELD_NO_HP, no_hp)
            except Exception:
                pass
        try:
            self.driver.hide_keyboard()
        except Exception:
            pass

    def tap_checkbox_setuju(self):
        try:
            self.scroll_and_tap(self.CHECKBOX_SETUJU, max_swipes=3)
        except Exception:
            pass

    def tap_daftar(self):
        self.scroll_and_tap(self.TOMBOL_DAFTAR, max_swipes=3)

    def is_error_displayed(self) -> bool:
        return (self.is_element_displayed(self.ERROR_EMAIL_TERDAFTAR, timeout=3) or
                self.is_element_displayed(self.ERROR_PASSWORD_TIDAK_COCOK, timeout=3) or
                self.is_element_displayed(self.ERROR_FIELD_WAJIB, timeout=3))

    def is_sukses_displayed(self) -> bool:
        return self.is_element_displayed(self.PESAN_SUKSES_REGISTRASI, timeout=5)
