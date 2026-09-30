import pytest
import allure
import time
from page.cari_dokter_page import CariDokterPage
from page.beranda_page import BerandaPage


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Cari Dokter")
class TestCariDokter:
    """Test suite Cari Dokter - 1 sesi class_driver. Status: 🔵 In Progress."""

    @pytest.fixture(autouse=True)
    def reset_to_dokter(self, class_driver, class_beranda):
        """Sebelum tiap test: beranda → health category → Cari Dokter."""
        self.dokter = CariDokterPage(class_driver)
        class_beranda.go_to_beranda()
        # Coba langsung scroll dari beranda dulu
        try:
            class_beranda.scroll_and_tap(self.dokter.ITEM_CARI_DOKTER, max_swipes=8)
        except Exception:
            # Fallback: via kategori kesehatan
            try:
                class_beranda.tap_kategori_kesehatan()
                time.sleep(1)
                class_beranda.scroll_and_tap(self.dokter.ITEM_CARI_DOKTER, max_swipes=5)
            except Exception:
                pass  # Let test handle missing navigation
        time.sleep(2)


    # ── DOKTER-01 ────────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman")
    @allure.title("DOKTER-01: Halaman Pencarian Dokter tampil")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_cari_dokter_tampil(self, class_driver):
        assert self.dokter.is_halaman_displayed(), \
            "Halaman Pencarian Dokter tidak tampil"

    # ── DOKTER-02 ────────────────────────────────────────────────────────────

    @allure.story("Pencarian Dokter")
    @allure.title("DOKTER-02: Cari dokter berdasarkan spesialisasi")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.xfail(reason="Fitur Pencarian Dokter masih dalam pengembangan")
    def test_cari_dokter_spesialisasi(self, class_driver):
        self.dokter.cari_dokter("Umum")
        time.sleep(3)
        assert self.dokter.is_hasil_displayed(), \
            "Hasil pencarian dokter tidak tampil"

    # ── DOKTER-03 ────────────────────────────────────────────────────────────

    @allure.story("Detail Dokter")
    @allure.title("DOKTER-03: Buka detail dokter dari hasil pencarian")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur Pencarian Dokter masih dalam pengembangan")
    def test_detail_dokter(self, class_driver, class_beranda):
        self.dokter.cari_dokter("Umum")
        time.sleep(3)
        if self.dokter.is_hasil_displayed():
            self.dokter.tap_hasil_pertama()
            time.sleep(2)
            src = class_driver.page_source
            assert any(kw in src for kw in [
                'Dokter', 'Spesialis', 'Jadwal', 'Rumah Sakit'
            ]), "Detail dokter tidak tampil"
        else:
            pytest.skip("Tidak ada hasil pencarian dokter")
