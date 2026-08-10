import pytest
import allure
import time
from page.search_page import SearchPage
from page.beranda_page import BerandaPage

@allure.feature("Search")
class TestSearch:
    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_beranda):
        class_beranda.go_to_beranda()

    @allure.story("Pencarian Valid")
    @allure.title("SEARCH-01: Cari Layanan dan Lihat Detail")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pencarian_layanan_detail(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("Nasional")
        search_page.tap_hasil_pencarian_pertama()

    @allure.story("Filter & Kategori")
    @allure.title("SEARCH-02: Filter dengan Kategori Layanan & Informasi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_kategori_pencarian(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("Nasional")
        search_page.tap_kategori_layanan()
        search_page.tap_kategori_informasi()

    @allure.story("Filter & Sort")
    @allure.title("SEARCH-03: Buka dan Aplikasikan Filter")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_pencarian(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("Nasional")
        search_page.tap_filter()
        class_beranda.press_back()

    @allure.story("Filter & Sort")
    @allure.title("SEARCH-04: Sort Hasil Pencarian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_pencarian(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("Nasional")
        search_page.tap_sort_az()

    @allure.story("Pencarian Invalid")
    @allure.title("SEARCH-05: Pencarian Tanpa Hasil (Negative)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_pencarian_tanpa_hasil(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("xyzabc123999")
        assert search_page.is_empty_state_displayed(), "Empty state 'tidak ada hasil' tidak muncul."

    @allure.story("UI Interaction")
    @allure.title("SEARCH-06: Tombol Clear Search")
    @allure.severity(allure.severity_level.MINOR)
    def test_clear_search(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("Nasional")
        search_page.clear_search()
        text = search_page.get_search_field_text()
        assert "Nasional" not in text, "Teks pencarian gagal dihapus."

    @allure.story("Pencarian Valid")
    @allure.title("SEARCH-07: Case Insensitivity")
    @allure.severity(allure.severity_level.MINOR)
    def test_case_insensitivity(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("nAsIoNal")
        search_page.tap_hasil_pencarian_pertama()
        assert search_page.is_detail_layanan_displayed(), "Pencarian bersifat case sensitive (harusnya insensitive)."

    @allure.story("Pencarian Invalid")
    @allure.title("SEARCH-08: Pencarian Karakter Spesial")
    @allure.severity(allure.severity_level.MINOR)
    def test_pencarian_karakter_spesial(self, class_driver, class_beranda):
        search_page = SearchPage(class_driver)
        class_beranda.go_to_cari()
        search_page.search_keyword("@#$%^&*()")
        is_empty = search_page.is_empty_state_displayed(timeout=2)
        is_result_shown = search_page.is_element_displayed(search_page.HASIL_PENCARIAN_PERTAMA, timeout=1)
        search_field_present = search_page.is_element_displayed(search_page.SEARCH_FIELD, timeout=1)
        assert is_empty or is_result_shown or search_field_present, "Aplikasi crash atau tidak merespon saat input karakter spesial."
