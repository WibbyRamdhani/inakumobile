import pytest
import allure
import time
from page.beranda_page import BerandaPage
from page.search_page import SearchPage
from page.layanan_page import LayananPage
from page.detail_layanan_page import DetailLayananPage


@allure.feature("Layanan")
class TestLayanan:

    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_beranda):
        """Kembali ke Beranda sebelum tiap test."""
        class_beranda.go_to_beranda()

    @pytest.fixture
    def detail_sosial(self, class_driver, class_beranda):
        """Buka halaman detail layanan pertama langsung dari tab Layanan."""
        layanan_page = LayananPage(class_driver)
        class_beranda.go_to_layanan()
        class_beranda.tap_pencarian()
        layanan_page.search_layanan("sosial")
        layanan_page.buka_detail_layanan_pertama()
        yield DetailLayananPage(class_driver)

    # ─── LAYANAN-01 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-01")
    @allure.title("LAYANAN-01: Navigasi Filter Layanan (Sort → Kategori → Filter)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_01_filter_kategori(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        layanan_page = LayananPage(class_driver)
        class_beranda.go_to_layanan()
        class_beranda.tap_pencarian()
        layanan_page.search_layanan("sosial")
        search_page.tap_sort_az()
        layanan_page.pilih_kategori_bantuan_sosial()
        search_page.tap_filter()

    # ─── LAYANAN-02 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-02")
    @allure.title("LAYANAN-02: Tombol Bagikan")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_02_bagikan(self, class_driver, class_beranda):
        layanan_page = LayananPage(class_driver)
        detail_page = DetailLayananPage(class_driver)
        class_beranda.go_to_layanan()
        class_beranda.tap_pencarian()
        layanan_page.search_layanan("sosial")
        layanan_page.buka_detail_layanan_pertama()
        detail_page.tap_bagikan()

    # ─── LAYANAN-03 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-03")
    @allure.title("LAYANAN-03: Navigasi Tab Informasi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_03_navigasi_tab(self, detail_sosial):
        detail_sosial.navigasi_tab("Persyaratan")
        detail_sosial.navigasi_tab("Cara Mengakses")
        detail_sosial.navigasi_tab("Informasi Tambahan")

    # ─── LAYANAN-04 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-04")
    @allure.title("LAYANAN-04: Akses ke Layanan (Eksternal)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_04_akses_kemensos(self, detail_sosial):
        detail_sosial.tap_akses_kemensos()
        detail_sosial.press_back()

    # ─── LAYANAN-05 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-05")
    @allure.title("LAYANAN-05: QnA (Tanya Jawab)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_05_qna(self, detail_sosial):
        detail_sosial.tap_qna_teratas()

    # ─── LAYANAN-06 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-06")
    @allure.title("LAYANAN-06: Tidak Menemukan Jawaban")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_06_tidak_menemukan_jawaban(self, detail_sosial):
        detail_sosial.tap_tidak_menemukan_jawaban()

    # ─── LAYANAN-07 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-07")
    @allure.title("LAYANAN-07: Layanan Terkait")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_07_layanan_terkait(self, detail_sosial):
        detail_sosial.tap_layanan_terkait_teratas()

    # ─── LAYANAN-08 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-08")
    @allure.title("LAYANAN-08: Rating & Ulasan (Rich Text)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur rating rich text belum selesai diimplementasikan")
    def test_layanan_08_rating_rich_text(self, detail_sosial):
        detail_sosial.buka_form_ulasan()
        detail_sosial.format_rich_text()
        detail_sosial.ketik_ulasan("Masih minim informasi")
        detail_sosial.kirim_ulasan()

    # ─── LAYANAN-09 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-09")
    @allure.title("LAYANAN-09: Pengaduan Kemensos")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_09_pengaduan_kemensos(self, detail_sosial):
        detail_sosial.tap_pengaduan_kemensos()

    # ─── LAYANAN-10 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-10")
    @allure.title("LAYANAN-10: Pengaduan Lapor")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_10_pengaduan_lapor(self, detail_sosial):
        detail_sosial.tap_pengaduan_lapor()

    # ─── LAYANAN-11 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-11")
    @allure.title("LAYANAN-11: Unduh Playstore")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_11_unduh_playstore(self, detail_sosial):
        detail_sosial.tap_unduh_playstore()
        detail_sosial.press_back()

    # ─── LAYANAN-12 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-12")
    @allure.title("LAYANAN-12: Verifikasi Konten Utama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_12_verifikasi_konten_utama(self, detail_sosial):
        assert detail_sosial.is_judul_layanan_displayed(), \
            "Judul layanan tidak ditemukan di layar utama!"
