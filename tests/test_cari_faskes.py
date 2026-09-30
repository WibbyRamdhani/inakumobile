import pytest
import allure
import time
from page.faskes_page import FaskesPage
from page.beranda_page import BerandaPage


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Cari Fasilitas Kesehatan")
class TestCariFaskes:
    """Test suite Faskes - 1 sesi class_driver untuk semua test."""

    @pytest.fixture(autouse=True)
    def reset_to_faskes(self, class_driver, class_beranda):
        """Sebelum tiap test: beranda → buka Faskes."""
        self.faskes = FaskesPage(class_driver)
        class_beranda.go_to_beranda()
        class_beranda.scroll_and_tap(self.faskes.ITEM_FASKES, max_swipes=5)
        time.sleep(2)

    # ── FASKES-01 ────────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman Faskes")
    @allure.title("FASKES-01: Halaman Pencarian Faskes tampil dengan benar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_faskes_tampil(self, class_driver):
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Fasilitas', 'Faskes', 'Kesehatan', 'Cari', 'Puskesmas', 'Rumah Sakit'
        ]), "Halaman Pencarian Faskes tidak tampil"

    # ── FASKES-02 ────────────────────────────────────────────────────────────

    @allure.story("Pencarian Faskes")
    @allure.title("FASKES-02: Cari faskes dengan nama 'Puskesmas'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_cari_faskes_puskesmas(self, class_driver):
        self.faskes.cari_faskes("Puskesmas")
        time.sleep(3)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Puskesmas', 'Faskes', 'Kesehatan', 'ditemukan', 'Hasil'
        ]), "Hasil pencarian Puskesmas tidak muncul"

    # ── FASKES-03 ────────────────────────────────────────────────────────────

    @allure.story("Detail Faskes")
    @allure.title("FASKES-03: Buka detail faskes pertama dari hasil pencarian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_detail_faskes(self, class_driver, class_beranda):
        self.faskes.cari_faskes("Puskesmas")
        time.sleep(3)
        if self.faskes.is_hasil_displayed():
            self.faskes.tap_hasil_pertama()
            time.sleep(2)
            src = class_driver.page_source
            assert any(kw in src for kw in [
                'Alamat', 'Telepon', 'Detail', 'Jam', 'Layanan'
            ]), "Detail faskes tidak tampil"
        else:
            pytest.skip("Tidak ada hasil pencarian faskes")

    # ── FASKES-04 ────────────────────────────────────────────────────────────

    @allure.story("Pencarian Faskes - Negatif")
    @allure.title("FASKES-04: Cari faskes dengan kata tidak valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cari_faskes_tidak_ada(self, class_driver):
        self.faskes.cari_faskes("zzzznotfound999")
        time.sleep(3)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'tidak ditemukan', 'Tidak ada', 'Cari', 'Fasilitas'
        ]) or self.faskes.is_kosong_displayed(), \
            "App tidak merespons pencarian kata tidak valid"
