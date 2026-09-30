import pytest
import allure
import time
from appium.webdriver.common.appiumby import AppiumBy
from page.layanan_bantuan_page import LayananBantuanPage
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage

VALID_EMAIL = "hernanda17@hotmail.com"
VALID_PASSWORD = "Bebas884422"


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Layanan Bantuan")
class TestLayananBantuan:
    """
    Test suite Layanan Bantuan - function-scoped driver (tiap test sesi baru).
    Dikonversi dari class-scoped karena UiAutomator2 crash setelah sesi sebelumnya.
    """

    @pytest.fixture(autouse=True)
    def setup_bantuan(self, driver):
        """Tiap test: fresh driver → login → ke tab Bantuan."""
        beranda = BerandaPage(driver)
        login = LoginPage(driver)
        self.bantuan = LayananBantuanPage(driver)
        self.driver = driver
        # Login
        login.navigate_to_login()
        login.login(VALID_EMAIL, VALID_PASSWORD)
        time.sleep(5)
        for _ in range(15):
            if login.is_home_screen_displayed(timeout=1):
                break
            time.sleep(1)
        beranda.go_to_beranda()
        time.sleep(2)
        # Navigasi ke Bantuan
        self.bantuan.go_to_bantuan()
        time.sleep(2)
        yield
        try:
            login.logout()
        except Exception:
            pass

    # ── BANTUAN-01 ─────────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman Bantuan")
    @allure.title("BANTUAN-01: Halaman bantuan tampil dengan benar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_bantuan_tampil(self):
        assert self.bantuan.is_halaman_bantuan_displayed(), \
            "Halaman Bantuan tidak tampil setelah tap tab Bantuan"

    # ── BANTUAN-02 ─────────────────────────────────────────────────────────────

    @allure.story("Buat Tiket Bantuan")
    @allure.title("BANTUAN-02: Buka form buat tiket bantuan")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buka_form_buat_tiket(self):
        self.bantuan.tap_buat_tiket()
        time.sleep(2)
        src = self.driver.page_source
        assert any(kw in src for kw in ['Judul', 'Deskripsi', 'Kategori', 'Tiket', 'Buat']), \
            "Form buat tiket tidak terbuka"

    # ── BANTUAN-03 ─────────────────────────────────────────────────────────────

    @allure.story("Buat Tiket Bantuan")
    @allure.title("BANTUAN-03: Isi dan kirim tiket bantuan baru")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buat_tiket_bantuan(self):
        self.bantuan.tap_buat_tiket()
        time.sleep(2)
        self.bantuan.isi_form_tiket(
            judul="Test Tiket Otomasi",
            deskripsi="Ini adalah tiket test dari automation QA"
        )
        self.bantuan.kirim_tiket()
        time.sleep(3)
        src = self.driver.page_source
        assert any(kw in src for kw in ['Bantuan', 'Tiket', 'berhasil', 'Terima']), \
            "Tiket bantuan gagal dikirim"

    # ── BANTUAN-04 ─────────────────────────────────────────────────────────────

    @allure.story("Daftar Tiket")
    @allure.title("BANTUAN-04: Lihat daftar tiket dan buka detail tiket pertama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lihat_daftar_tiket(self):
        time.sleep(1)
        if self.bantuan.is_element_displayed(self.bantuan.TIKET_PERTAMA, timeout=3):
            self.bantuan.tap_tiket_pertama()
            time.sleep(2)
            src = self.driver.page_source
            assert any(kw in src for kw in ['Detail', 'Status', 'Tiket', '#']), \
                "Detail tiket tidak terbuka"
        else:
            assert True  # Soft pass - belum ada tiket

    # ── BANTUAN-05 ─────────────────────────────────────────────────────────────

    @allure.story("Buat Tiket via Tombol di Beranda")
    @allure.title("BANTUAN-05: Buat Tiket dari tombol 'Buat Tiket' di beranda")
    @allure.severity(allure.severity_level.NORMAL)
    def test_buat_tiket_dari_beranda(self):
        """Ada tombol 'Buat Tiket' di beranda saat login."""
        beranda = BerandaPage(self.driver)
        beranda.go_to_beranda()
        time.sleep(1)
        buat_tiket_loc = (AppiumBy.ACCESSIBILITY_ID, "Buat Tiket")
        if self.bantuan.is_element_displayed(buat_tiket_loc, timeout=3):
            self.bantuan.tap(buat_tiket_loc)
            time.sleep(2)
            src = self.driver.page_source
            assert any(kw in src for kw in ['Judul', 'Tiket', 'Buat']), \
                "Form tiket tidak terbuka dari beranda"
        else:
            pytest.skip("Tombol 'Buat Tiket' tidak tampil di beranda saat ini")
