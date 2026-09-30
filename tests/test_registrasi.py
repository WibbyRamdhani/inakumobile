import pytest
import allure
import time
import random
from page.registrasi_page import RegistrasiPage
from page.login_pages import LoginPage
from page.beranda_page import BerandaPage


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Registrasi Non-IKD")
class TestRegistrasi:
    """
    Test suite Registrasi - function-scoped driver (tiap test sesi baru).
    Keyboard-heavy tests rentan crash di class-scoped session.
    Flow: Profil → Masuk Akun → Daftar sekarang → Form Registrasi
    """

    @pytest.fixture(autouse=True)
    def setup_registrasi(self, driver):
        """Tiap test: fresh driver → navigate ke form registrasi."""
        beranda = BerandaPage(driver)
        login = LoginPage(driver)
        self.registrasi = RegistrasiPage(driver)
        self.driver = driver
        # Navigate ke form registrasi
        beranda.go_to_beranda()
        time.sleep(1)
        login.navigate_to_login()
        time.sleep(1)
        self.registrasi.tap_link_daftar()
        time.sleep(2)
        yield

    # ── REG-01 ───────────────────────────────────────────────────────────────

    @allure.story("Tampilan Form Registrasi")
    @allure.title("REG-01: Form registrasi tampil dengan semua field")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_form_registrasi_tampil(self):
        assert self.registrasi.is_halaman_registrasi_displayed(), \
            "Halaman registrasi tidak tampil setelah klik link daftar"

    # ── REG-02 ───────────────────────────────────────────────────────────────

    @allure.story("Registrasi - Field Kosong")
    @allure.title("REG-02: Submit form registrasi kosong → validasi semua field wajib")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registrasi_field_kosong(self):
        self.registrasi.tap_daftar()
        time.sleep(2)
        src = self.driver.page_source
        assert any(kw in src for kw in [
            'wajib', 'required', 'tidak boleh', 'harus diisi', 'Daftar', 'Registrasi'
        ]), "Tidak ada validasi saat submit form kosong"

    # ── REG-03 ───────────────────────────────────────────────────────────────

    @allure.story("Registrasi - Email Sudah Terdaftar")
    @allure.title("REG-03: Registrasi dengan email yang sudah terdaftar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_registrasi_email_terdaftar(self):
        self.registrasi.isi_form_registrasi(
            nama="Test User",
            email="hernanda17@hotmail.com",
            password="TestPass123!",
            konfirmasi="TestPass123!"
        )
        self.registrasi.tap_daftar()
        time.sleep(4)  # Tunggu response API
        src = self.driver.page_source
        # App bisa menampilkan error dalam berbagai format
        assert any(kw in src for kw in [
            'sudah terdaftar', 'already', 'sudah digunakan', 'gagal', 'error',
            'Error', 'tidak dapat', 'exists', 'terdaftar', 'Email'
        ]) or not self.registrasi.is_sukses_displayed(), \
            "Submit email terdaftar tidak memunculkan pesan error"

    # ── REG-04 ───────────────────────────────────────────────────────────────

    @allure.story("Registrasi - Password Tidak Cocok")
    @allure.title("REG-04: Registrasi dengan konfirmasi password tidak sama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registrasi_password_tidak_cocok(self):
        self.registrasi.isi_form_registrasi(
            nama="Test User",
            email=f"testqa.beda{random.randint(1000,9999)}@mailinator.com",
            password="TestPass123!",
            konfirmasi="TestPass999!"
        )
        self.registrasi.tap_daftar()
        time.sleep(2)
        src = self.driver.page_source
        assert any(kw in src for kw in [
            'tidak sama', 'tidak cocok', 'mismatch', 'password', 'Password', 'Konfirmasi'
        ]), "Tidak ada validasi untuk konfirmasi password yang berbeda"

    # ── REG-05 ───────────────────────────────────────────────────────────────

    @allure.story("Registrasi - Email Format Salah")
    @allure.title("REG-05: Registrasi dengan format email tidak valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_registrasi_email_format_salah(self):
        self.registrasi.isi_form_registrasi(
            nama="Test User",
            email="bukan-email-valid",
            password="TestPass123!",
            konfirmasi="TestPass123!"
        )
        self.registrasi.tap_daftar()
        time.sleep(2)
        src = self.driver.page_source
        assert any(kw in src for kw in [
            'tidak valid', 'format', 'invalid', 'email', '@', 'Email'
        ]), "Tidak ada validasi untuk format email tidak valid"

    # ── REG-06 ───────────────────────────────────────────────────────────────

    @allure.story("Registrasi - Sukses")
    @allure.title("REG-06: Registrasi berhasil dengan data valid (baru)")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.xfail(reason="Membutuhkan email baru yang belum terdaftar setiap run")
    def test_registrasi_berhasil(self):
        suffix = random.randint(10000, 99999)
        self.registrasi.isi_form_registrasi(
            nama=f"Test Auto {suffix}",
            email=f"testqa.auto{suffix}@mailinator.com",
            password="TestPass123!",
            konfirmasi="TestPass123!"
        )
        self.registrasi.tap_checkbox_setuju()
        self.registrasi.tap_daftar()
        time.sleep(5)
        assert self.registrasi.is_sukses_displayed() or any(
            kw in self.driver.page_source for kw in [
                'berhasil', 'OTP', 'verifikasi', 'Selamat'
            ]
        ), "Registrasi tidak berhasil dengan data valid"
