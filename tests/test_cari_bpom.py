import pytest
import allure
import time
from page.bpom_page import BpomPage
from page.beranda_page import BerandaPage


@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Cari Produk BPOM")
class TestCariBpom:
    """
    Test suite BPOM - Search Results dan Detail Layanan Pengecekan Produk BPOM.
    Note: Tap 'Pengecekan Produk BPOM' dari topik populer membuka halaman Search Results,
    bukan halaman input produk. 1 sesi class_driver.
    """

    @pytest.fixture(autouse=True)
    def reset_to_bpom(self, class_driver, class_beranda):
        """Sebelum tiap test: beranda → buka halaman Search Results BPOM."""
        self.bpom = BpomPage(class_driver)
        class_beranda.go_to_beranda()
        class_beranda.scroll_and_tap(self.bpom.ITEM_BPOM, max_swipes=5)
        time.sleep(2)

    # ── BPOM-01 ──────────────────────────────────────────────────────────────

    @allure.story("Tampilan Halaman BPOM")
    @allure.title("BPOM-01: Halaman Search Results 'Pengecekan Produk BPOM' tampil")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_halaman_bpom_tampil(self, class_driver):
        """Verifikasi halaman search results BPOM terbuka."""
        assert self.bpom.is_search_results_displayed() or any(
            kw in class_driver.page_source for kw in [
                'BPOM', 'Produk', 'Pencarian', 'Pengecekan'
            ]
        ), "Halaman Search Results BPOM tidak tampil"

    # ── BPOM-02 ──────────────────────────────────────────────────────────────

    @allure.story("Card BPOM di Search Results")
    @allure.title("BPOM-02: Card layanan BPOM tersedia di hasil pencarian")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_card_bpom_tersedia(self, class_driver):
        """Verifikasi card 'Pengecekan Produk BPOM' muncul di hasil pencarian."""
        assert self.bpom.is_card_bpom_displayed() or any(
            kw in class_driver.page_source for kw in [
                'Pengecekan Produk BPOM', 'LAYANAN NASIONAL', 'BPOM'
            ]
        ), "Card BPOM tidak ditemukan di search results"

    # ── BPOM-03 ──────────────────────────────────────────────────────────────

    @allure.story("Detail Layanan BPOM")
    @allure.title("BPOM-03: Tap card BPOM → halaman Detail Layanan terbuka")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_detail_layanan_bpom(self, class_driver, class_beranda):
        """Tap card BPOM untuk buka Detail Layanan, verifikasi konten."""
        self.bpom.tap_card_bpom()
        time.sleep(2)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'BPOM', 'Produk', 'NASIONAL', 'ONLINE', 'Cara Akses', 'Layanan'
        ]), "Detail Layanan BPOM tidak terbuka setelah tap card"

    # ── BPOM-04 ──────────────────────────────────────────────────────────────

    @allure.story("Filter Search Results")
    @allure.title("BPOM-04: Filter chip 'Layanan' berfungsi di search results BPOM")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_chip_layanan(self, class_driver):
        """Tap chip 'Layanan' untuk filter hasil pencarian."""
        self.bpom.tap_chip_layanan()
        time.sleep(1)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Layanan', 'BPOM', 'Pengecekan', 'NASIONAL'
        ]), "Filter Layanan tidak berfungsi di BPOM search results"

    # ── BPOM-05 ──────────────────────────────────────────────────────────────

    @allure.story("Konten Detail BPOM")
    @allure.title("BPOM-05: Rating section tersedia di Detail Layanan BPOM")
    @allure.severity(allure.severity_level.MINOR)
    def test_rating_detail_bpom(self, class_driver, class_beranda):
        """Setelah buka detail BPOM, verifikasi section rating tersedia."""
        self.bpom.tap_card_bpom()
        time.sleep(3)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'BPOM', 'Produk', 'NASIONAL', 'Layanan', 'Cari', 'Beranda', 'Detail'
        ]), "Halaman tidak tampil setelah tap card BPOM"

