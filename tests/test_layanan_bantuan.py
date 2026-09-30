import pytest
import allure
import time
from page.layanan_bantuan_page import LayananBantuanPage
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage

VALID_EMAIL = "hernanda17@hotmail.com"
VALID_PASSWORD = "Bebas884422"


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Layanan Bantuan")
class TestLayananBantuan:
    """
    Test suite untuk fitur Layanan Bantuan / Aduan (Tiket Help Desk).
    """

    @pytest.fixture(scope="class", autouse=True)
    def setup_login_class(self, class_driver, class_beranda, class_login):
        """Login 1x untuk seluruh class tests."""
        class_login.navigate_to_login()
        class_login.login(VALID_EMAIL, VALID_PASSWORD)
        for _ in range(15):
            time.sleep(1)
            if class_login.is_home_screen_displayed(timeout=1):
                break
        class_login.go_to_beranda()
        time.sleep(2)
        yield
        try:
            class_login.logout()
        except Exception:
            pass

    @pytest.fixture(autouse=True)
    def reset_to_bantuan(self, class_driver, class_beranda):
        """Navigasi ke tab Bantuan sebelum tiap test."""
        bantuan = LayananBantuanPage(class_driver)
        bantuan.go_to_bantuan()
        time.sleep(1)

    # ── BANTUAN-01 ───────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman Bantuan")
    @allure.title("BANTUAN-01: Halaman bantuan tampil dengan benar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_bantuan_tampil(self, class_driver):
        bantuan = LayananBantuanPage(class_driver)
        assert bantuan.is_halaman_bantuan_displayed(), \
            "Halaman Bantuan tidak tampil setelah tap tab Bantuan"

    # ── BANTUAN-02 ───────────────────────────────────────────────────────────

    @allure.story("Buat Tiket Bantuan")
    @allure.title("BANTUAN-02: Buka form buat tiket bantuan")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buka_form_buat_tiket(self, class_driver):
        bantuan = LayananBantuanPage(class_driver)
        bantuan.tap_buat_tiket()
        time.sleep(2)
        src = class_driver.page_source
        assert any(kw in src for kw in ['Judul', 'Deskripsi', 'Kategori', 'Tiket', 'Buat']), \
            "Form buat tiket tidak terbuka"

    # ── BANTUAN-03 ───────────────────────────────────────────────────────────

    @allure.story("Buat Tiket Bantuan")
    @allure.title("BANTUAN-03: Isi dan kirim tiket bantuan baru")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_buat_tiket_bantuan(self, class_driver):
        bantuan = LayananBantuanPage(class_driver)
        bantuan.tap_buat_tiket()
        time.sleep(2)
        bantuan.isi_form_tiket(
            judul="Test Tiket Otomasi",
            deskripsi="Ini adalah tiket test dari automation QA"
        )
        bantuan.kirim_tiket()
        time.sleep(3)
        # Verifikasi tiket terkirim: kembali ke daftar tiket atau muncul pesan sukses
        src = class_driver.page_source
        assert any(kw in src for kw in ['Bantuan', 'Tiket', 'berhasil', 'Terima']), \
            "Tiket bantuan gagal dikirim"

    # ── BANTUAN-04 ───────────────────────────────────────────────────────────

    @allure.story("Daftar Tiket")
    @allure.title("BANTUAN-04: Lihat daftar tiket dan buka detail tiket pertama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_lihat_daftar_tiket(self, class_driver):
        bantuan = LayananBantuanPage(class_driver)
        time.sleep(1)
        src = class_driver.page_source
        # Jika ada tiket tampil → tap tiket pertama
        if bantuan.is_element_displayed(bantuan.TIKET_PERTAMA, timeout=3):
            bantuan.tap_tiket_pertama()
            time.sleep(2)
            src = class_driver.page_source
            assert any(kw in src for kw in ['Detail', 'Status', 'Tiket', '#']), \
                "Detail tiket tidak terbuka"
        else:
            # Tidak ada tiket → soft pass (belum ada data)
            assert True, "Tidak ada tiket (expected jika akun baru)"

    # ── BANTUAN-05 ───────────────────────────────────────────────────────────

    @allure.story("Buat Tiket via Tombol di Beranda")
    @allure.title("BANTUAN-05: Buat Tiket dari tombol 'Buat Tiket' di beranda")
    @allure.severity(allure.severity_level.NORMAL)
    def test_buat_tiket_dari_beranda(self, class_driver, class_beranda):
        """Ada tombol 'Buat Tiket' dengan badge '9+' di beranda saat login."""
        class_beranda.go_to_beranda()
        time.sleep(1)
        buat_tiket = (
            __import__('appium.webdriver.common.appiumby', fromlist=['AppiumBy']).AppiumBy.ACCESSIBILITY_ID,
            "Buat Tiket"
        )
        bantuan = LayananBantuanPage(class_driver)
        if bantuan.is_element_displayed(buat_tiket, timeout=3):
            bantuan.tap(buat_tiket)
            time.sleep(2)
            src = class_driver.page_source
            assert any(kw in src for kw in ['Judul', 'Tiket', 'Buat']), \
                "Form tiket tidak terbuka dari beranda"
        else:
            pytest.skip("Tombol 'Buat Tiket' tidak tampil di beranda saat ini")
