import pytest
import allure
import time
from page.search_page import SearchPage
from page.beranda_page import BerandaPage


@allure.feature("Search")
class TestSearch:
    """
    Search tests: masing-masing test pakai function-scoped driver (sesi fresh).
    Ini mencegah cascading failure jika UiAutomator2 crash di satu test.
    """

    @pytest.fixture(autouse=True)
    def setup_search(self, driver):
        """Tiap test: fresh driver → go to beranda → siap."""
        self.beranda = BerandaPage(driver)
        self.search = SearchPage(driver)
        self.beranda.go_to_beranda()
        yield

    # ── SEARCH-01 ───────────────────────────────────────────────────────────

    @allure.story("Pencarian Valid")
    @allure.title("SEARCH-01: Cari Layanan dan Lihat Detail")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pencarian_layanan_detail(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.clear_search()
        time.sleep(0.5)
        self.search.search_keyword("Nasional")
        self.search.tap_hasil_pencarian_pertama()
        try:
            self.beranda.press_back()
        except Exception:
            pass

    # ── SEARCH-02 ───────────────────────────────────────────────────────────

    @allure.story("Filter & Kategori")
    @allure.title("SEARCH-02: Filter dengan Kategori Layanan & Informasi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_kategori_pencarian(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.clear_search()
        time.sleep(0.5)
        self.search.search_keyword("Nasional")
        self.search.tap_kategori_layanan()
        self.search.tap_kategori_informasi()

    # ── SEARCH-03 ───────────────────────────────────────────────────────────

    @allure.story("Filter & Sort")
    @allure.title("SEARCH-03: Buka dan Aplikasikan Filter")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_pencarian(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.clear_search()
        time.sleep(0.5)
        self.search.search_keyword("Nasional")
        self.search.tap_filter()
        self.beranda.press_back()

    # ── SEARCH-04 ───────────────────────────────────────────────────────────

    @allure.story("Filter & Sort")
    @allure.title("SEARCH-04: Sort Hasil Pencarian")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_pencarian(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.clear_search()
        time.sleep(0.5)
        self.search.search_keyword("Nasional")
        self.search.tap_sort_az()

    # ── SEARCH-05 ───────────────────────────────────────────────────────────

    @allure.story("Pencarian Invalid")
    @allure.title("SEARCH-05: Pencarian Tanpa Hasil (Negative)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_pencarian_tanpa_hasil(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.clear_search()
        time.sleep(0.5)
        self.search.search_keyword("zzzznotexist9999")
        time.sleep(3)
        # Soft-assert: app tidak crash, search field masih ada
        search_field_present = self.search.is_element_displayed(
            self.search.SEARCH_FIELD, timeout=3)
        assert search_field_present, \
            "App crash atau search field hilang setelah pencarian tanpa hasil."

    # ── SEARCH-06 ───────────────────────────────────────────────────────────

    @allure.story("UI Interaction")
    @allure.title("SEARCH-06: Tombol Clear Search")
    @allure.severity(allure.severity_level.MINOR)
    def test_clear_search(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.search_keyword("Nasional")
        self.search.clear_search()
        text = self.search.get_search_field_text()
        assert "Nasional" not in text, "Teks pencarian gagal dihapus."

    # ── SEARCH-07 ───────────────────────────────────────────────────────────

    @allure.story("Pencarian Valid")
    @allure.title("SEARCH-07: Case Insensitivity")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail(reason="UiAutomator2 instrumentation crash pada mixed-case input")
    def test_case_insensitivity(self, driver):
        self.beranda.go_to_cari()
        self.search.search_keyword("nAsIoNal")
        self.search.tap_hasil_pencarian_pertama()
        assert self.search.is_detail_layanan_displayed(), \
            "Pencarian bersifat case sensitive (harusnya insensitive)."

    # ── SEARCH-08 ───────────────────────────────────────────────────────────

    @allure.story("Pencarian Invalid")
    @allure.title("SEARCH-08: Pencarian Karakter Spesial")
    @allure.severity(allure.severity_level.MINOR)
    def test_pencarian_karakter_spesial(self, driver):
        self.beranda.go_to_cari()
        time.sleep(1)
        self.search.search_keyword("@#$%&*()")
        is_empty = self.search.is_empty_state_displayed(timeout=2)
        is_result = self.search.is_element_displayed(
            self.search.HASIL_PENCARIAN_PERTAMA, timeout=1)
        field_ok = self.search.is_element_displayed(
            self.search.SEARCH_FIELD, timeout=1)
        assert is_empty or is_result or field_ok, \
            "Aplikasi crash atau tidak merespon saat input karakter spesial."
