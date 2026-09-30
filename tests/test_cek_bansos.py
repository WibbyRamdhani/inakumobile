import pytest
import allure
import time
from page.cek_bansos_page import CekBansosPage
from page.beranda_page import BerandaPage

NIK_VALID = "1902015511940006"


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Cek Bantuan Sosial")
class TestCekBansos:
    """
    Test suite Bansos - 1 sesi class_driver.
    Status: ⚙️ API belum terintegrasi — mayoritas test di-skip.
    """

    @pytest.fixture(autouse=True)
    def reset_to_bansos(self, class_driver, class_beranda):
        """Sebelum tiap test: beranda → buka Bansos."""
        self.bansos = CekBansosPage(class_driver)
        class_beranda.go_to_beranda()
        class_beranda.scroll_and_tap(self.bansos.ITEM_BANSOS, max_swipes=5)
        time.sleep(2)

    # ── BANSOS-01 ────────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman")
    @allure.title("BANSOS-01: Halaman Cek Bansos tampil")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_bansos_tampil(self, class_driver):
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Bansos', 'Bantuan', 'Sosial', 'PKH', 'NIK'
        ]), "Halaman Cek Bansos tidak tampil"

    # ── BANSOS-02 ────────────────────────────────────────────────────────────

    @allure.story("Cek Bansos")
    @allure.title("BANSOS-02: Cek bansos dengan NIK valid")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip(reason="API Cek Bansos belum terintegrasi")
    def test_cek_bansos_nik_valid(self, class_driver):
        self.bansos.cek_bansos(NIK_VALID)
        time.sleep(5)
        assert self.bansos.is_hasil_displayed() or any(
            kw in class_driver.page_source for kw in ['PKH', 'BPNT', 'Penerima']
        ), f"Hasil cek bansos untuk NIK {NIK_VALID} tidak tampil"

    # ── BANSOS-03 ────────────────────────────────────────────────────────────

    @allure.story("Cek Bansos - Tidak Terdaftar")
    @allure.title("BANSOS-03: Cek bansos dengan NIK tidak terdaftar")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="API Cek Bansos belum terintegrasi")
    def test_cek_bansos_tidak_terdaftar(self, class_driver):
        self.bansos.cek_bansos("0000000000000000")
        time.sleep(5)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'tidak terdaftar', 'tidak menerima', 'Tidak ditemukan'
        ]), "Tidak ada pesan untuk NIK yang tidak terdaftar bansos"

    # ── BANSOS-04 ────────────────────────────────────────────────────────────

    @allure.story("Validasi Input")
    @allure.title("BANSOS-04: Cek bansos dengan NIK kosong")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="API Cek Bansos belum terintegrasi")
    def test_cek_bansos_nik_kosong(self, class_driver):
        self.bansos.cek_bansos("")
        time.sleep(2)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'wajib', 'required', 'NIK', 'isi'
        ]), "Tidak ada validasi untuk NIK kosong"
