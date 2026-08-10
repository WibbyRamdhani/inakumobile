import pytest
import allure
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage
import time

@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Beranda")
class TestBerandaNonLogin:
    
    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_beranda):
        """Dijalankan sebelum tiap test untuk memastikan aplikasi berada di Beranda."""
        class_beranda.go_to_beranda()

    @allure.story("Beranda (Non-Login)")
    @allure.title("BERANDA-01: Menampilkan section standar (tanpa Benefit/E-Dokumen)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_tampilan_benar(self, class_beranda):
        assert class_beranda.is_beranda_standar_displayed(), "Section standar beranda gagal dimuat."
        assert not class_beranda.is_benefit_section_displayed(), "Section Benefit seharusnya TIDAK muncul saat belum login."
        assert not class_beranda.is_edokumen_section_displayed(), "Section E-Dokumen seharusnya TIDAK muncul saat belum login."

    @allure.story("Beranda (Non-Login)")
    @allure.title("BERANDA-02: Pencarian dari halaman beranda saat belum login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_search(self, class_beranda):
        class_beranda.tap_pencarian()
        time.sleep(2)
        class_beranda.input_pencarian("Nasional")
        class_beranda.tap_hasil_pencarian()

    @allure.story("Beranda (Non-Login)")
    @allure.title("BERANDA-03: Interaksi Layanan Populer saat belum login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_layanan_populer(self, class_beranda):
        class_beranda.tap_item_layanan_populer()
        class_beranda.safe_tap_back()
        class_beranda.tap_lihat_semua_layanan_populer()
        class_beranda.safe_tap_back()

    @allure.story("Beranda (Non-Login)")
    @allure.title("BERANDA-04: Jelajahi Layanan Kategori Kesehatan")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_jelajahi_layanan(self, class_beranda):
        class_beranda.tap_kategori_kesehatan()
        class_beranda.tap_pencarian_dokter()
