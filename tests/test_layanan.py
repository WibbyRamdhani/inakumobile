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
        """Buka halaman detail layanan 'Mengecek Bantuan Sosial' — dipakai oleh banyak test."""
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
    def test_layanan_02_bagikan(self, detail_sosial):
        detail_sosial.tap_bagikan()

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

    # ─── LAYANAN-08 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-08")
    @allure.title("LAYANAN-08: Tidak Menemukan Jawaban")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_08_tidak_menemukan_jawaban(self, detail_sosial):
        detail_sosial.tap_tidak_menemukan_jawaban()

    # ─── LAYANAN-09 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-09")
    @allure.title("LAYANAN-09: Layanan Terkait")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_09_layanan_terkait(self, detail_sosial):
        detail_sosial.tap_layanan_terkait_teratas()

    # ─── LAYANAN-11 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-11")
    @allure.title("LAYANAN-11: Rating & Ulasan (Rich Text)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur rating rich text belum selesai diimplementasikan")
    def test_layanan_11_rating_rich_text(self, detail_sosial):
        detail_sosial.buka_form_ulasan()
        detail_sosial.format_rich_text()
        detail_sosial.ketik_ulasan("Masih minim informasi")
        detail_sosial.kirim_ulasan()

    # ─── LAYANAN-12 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-12")
    @allure.title("LAYANAN-12: Pengaduan Kemensos")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_12_pengaduan_kemensos(self, detail_sosial):
        detail_sosial.tap_pengaduan_kemensos()

    # ─── LAYANAN-13 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-13")
    @allure.title("LAYANAN-13: Pengaduan Lapor")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_13_pengaduan_lapor(self, detail_sosial):
        detail_sosial.tap_pengaduan_lapor()

    # ─── LAYANAN-14 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-14")
    @allure.title("LAYANAN-14: Unduh Playstore")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_14_unduh_playstore(self, detail_sosial):
        detail_sosial.tap_unduh_playstore()
        detail_sosial.press_back()

    # ─── LAYANAN-15 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-15")
    @allure.title("LAYANAN-15: Verifikasi Konten Utama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_15_verifikasi_konten_utama(self, detail_sosial):
        assert detail_sosial.is_judul_layanan_displayed(), \
            "Judul layanan tidak ditemukan di layar utama!"

    # ─── LAYANAN-16 ──────────────────────────────────────────────────────────
    @allure.story("LAYANAN-16")
    @allure.title("LAYANAN-16: Tombol Back")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan_16_tombol_back(self, class_driver, class_beranda):
        layanan_page = LayananPage(class_driver)
        class_beranda.go_to_layanan()
        class_beranda.tap_pencarian()
        layanan_page.search_layanan("sosial")
        layanan_page.buka_detail_layanan_pertama()
        DetailLayananPage(class_driver).press_back()
        assert layanan_page.is_element_displayed(layanan_page.SEARCH_FIELD), \
            "Gagal kembali ke halaman pencarian!"
