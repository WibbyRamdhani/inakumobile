
import pytest
import allure
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage
import time

@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Beranda")
class TestBerandaLogin:
    
    @pytest.fixture(scope="class", autouse=True)
    @classmethod
    def setup_login_class(cls, class_driver, class_beranda, class_login):
        """Setup dijalankan 1x per class: hapus app data, restart, lalu login."""
        class_beranda.tap_masuk_header()
        class_login.login("admin@portal.dev", "Admin123!")
        for _ in range(20):
            if not class_beranda.is_element_displayed(class_login.LOGIN_PAGE_INDICATOR, timeout=0.5):
                break
            time.sleep(0.5)
        class_beranda.go_to_beranda()
        assert class_beranda.is_element_displayed(class_beranda.SECTION_BENEFIT, timeout=15), "Benefit tidak ditemukan, berarti gagal kembali ke Beranda (atau login gagal)"
        
    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_beranda):
        """Dijalankan sebelum tiap test untuk memastikan aplikasi berada di Beranda tanpa perlu clearApp."""
        class_beranda.go_to_beranda()

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-01: Menampilkan section lengkap termasuk Benefit & E-Dokumen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_tampilan_lengkap(self, class_driver, class_beranda):
        assert class_beranda.is_benefit_section_displayed(), "Section Benefit harusnya muncul setelah login."
        assert class_beranda.is_edokumen_section_displayed(), "Section E-Dokumen harusnya muncul setelah login."

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-02: Pencarian dari halaman beranda saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_search(self, class_driver, class_beranda):
        class_beranda.tap_pencarian_dummy() 
        class_beranda.input_pencarian("Kesehatan")
        class_beranda.tap_hasil_pencarian()

    @allure.story("Benefit User")
    @allure.title("BERANDA-03: Carousel Benefit dan klik item pertama")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_benefit_carousel(self, class_driver, class_beranda):
        class_beranda.scroll_carousel_benefit()
        class_beranda.tap_item_benefit()

    @allure.story("Benefit User")
    @allure.title("BERANDA-04: Validasi pagination pada halaman Lihat Semua Benefit")
    @allure.severity(allure.severity_level.NORMAL)
    def test_pagination_benefit(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_benefit()
        class_beranda.scroll_ke_bawah()
        class_beranda.tap_pagination_benefit("next")
        class_beranda.tap_pagination_benefit("prev")
        class_beranda.tap_pagination_benefit("last")
        class_beranda.tap_pagination_benefit("first")

    @allure.story("Benefit User")
    @allure.title("BERANDA-05: Pencarian pada halaman Lihat Semua Benefit")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_benefit_all(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_benefit()
        class_beranda.input_pencarian("keluarga")
        class_beranda.tap_item_benefit()
        class_beranda.safe_tap_back()

    @allure.story("Benefit User")
    @allure.title("BERANDA-06: Filter dan Sort pada halaman Lihat Semua Benefit")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur belum selesai")
    def test_beranda_benefit_all_filter_sort(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_benefit()
        class_beranda.tap_filter_benefit()
        class_beranda.tap_sort_benefit()
        time.sleep(2)
        

    @allure.story("Pencarian User")
    @allure.title("BERANDA-07: Pemilihan Kategori pada halaman Lihat Semua Benefit")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_benefit_all_kategori(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_benefit()
        
        class_beranda.pilih_kategori_benefit("semua")
        class_beranda.pilih_kategori_benefit("bantuan sosial")
        class_beranda.pilih_kategori_benefit("pendidikan")

    @allure.story("E-Dokumen User")
    @allure.title("BERANDA-08: Interaksi Carousel E-Dokumen dan Lihat/Unduh Dokumen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_edokumen(self, class_driver, class_beranda):
        class_beranda.tap_item_edokumen()
        class_beranda.tap_lihat_dokumen() 
        class_beranda.tap_unduh_dokumen()

    @allure.story("E-Dokumen User")
    @allure.title("BERANDA-09: Direct ke halaman Profil E-Dokumen")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_edokumen_all(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_edokumen()
        class_beranda.is_profil_edokumen_displayed()

    @allure.story("Layanan Populer (Login)")
    @allure.title("BERANDA-10: Interaksi Layanan Populer saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_layanan_populer(self, class_driver, class_beranda):
        class_beranda.tap_item_layanan_populer()
        class_beranda.safe_tap_back()
        class_beranda.tap_lihat_semua_layanan_populer()
        class_beranda.tap_item_layanan_populer()

    @allure.story("Topik Populer (Login)")
    @allure.title("BERANDA-11: Interaksi Topik Populer saat login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur belum jadi")
    def test_beranda_topik_populer(self, class_driver, class_beranda):
        class_beranda.tap_item_topik_populer()
        assert not class_beranda.is_element_displayed(class_beranda.TAB_BERANDA, timeout=3), "Topik Populer gagal membuka halaman baru (fitur belum jadi)"

    @allure.story("Jelajahi Layanan (Login)")
    @allure.title("BERANDA-12: Jelajahi Layanan Kategori Kesehatan saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_jelajahi_layanan(self, class_driver, class_beranda):
        class_beranda.tap_kategori_kesehatan()
        class_beranda.go_to_beranda()
        class_beranda.tap_lihat_semua_jelajahi_layanan()
        class_beranda.pilih_kategori_benefit("bantuan sosial") 