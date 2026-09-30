
import pytest
import allure
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage
import time

VALID_EMAIL = "hernanda17@hotmail.com"
VALID_PASSWORD = "Bebas884422"

@allure.epic("Portal Layanan Publik Mobile")
@allure.feature("Beranda")
class TestBerandaLogin:

    @pytest.fixture(scope="class", autouse=True)
    def setup_login_class(self, class_driver, class_beranda, class_login):
        """Login 1x per class, teardown logout."""
        class_login.navigate_to_login()
        class_login.login(VALID_EMAIL, VALID_PASSWORD)
        # Tunggu login selesai — indikator: notifikasi '9+' atau header berubah
        for _ in range(15):
            time.sleep(1)
            src = class_driver.page_source
            if '9+' in src or 'Akun Saya' in src:
                break
        class_login.go_to_beranda()
        time.sleep(2)

        yield

        try:
            class_login.logout()
        except Exception:
            pass

    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_driver, class_beranda):
        """Sebelum tiap test: pop nav stack, kembali ke beranda."""
        for _ in range(5):
            try:
                class_driver.press_keycode(4)  # Android Back
            except Exception:
                pass
            time.sleep(0.2)
        time.sleep(0.5)
        class_beranda.go_to_beranda()
        time.sleep(1)


    # ── BERANDA-01 ───────────────────────────────────────────────────────────

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-01: Header berubah setelah login (notifikasi / akun)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_beranda_header_login(self, class_driver, class_beranda):
        """Setelah login, header beranda menampilkan notifikasi (9+) atau menu akun."""
        src = class_driver.page_source
        assert ('9+' in src or 'Akun Saya' in src), \
            "Header beranda tidak berubah setelah login — state masih non-login."

    # ── BERANDA-02 ───────────────────────────────────────────────────────────

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-02: Layanan Populer tampil dan bisa diklik saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_layanan_populer(self, class_driver, class_beranda):
        class_beranda.tap_item_layanan_populer()
        class_beranda.safe_tap_back()

    # ── BERANDA-03 ───────────────────────────────────────────────────────────

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-03: Lihat semua Layanan Populer saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_lihat_semua_layanan_populer(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_layanan_populer()
        time.sleep(2)
        # Verifikasi halaman baru terbuka (ada item layanan / konten)
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Pengurusan', 'Pencarian', 'Layanan', 'Informasi', 'Kepesertaan'
        ]), "Halaman Lihat Semua Layanan tidak terbuka."
        class_beranda.safe_tap_back()

    # ── BERANDA-04 ───────────────────────────────────────────────────────────

    @allure.story("Beranda (Setelah Login)")
    @allure.title("BERANDA-04: Topik Populer tampil saat login")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Fitur Topik Populer belum jadi")
    def test_beranda_topik_populer(self, class_driver, class_beranda):
        class_beranda.tap_item_topik_populer()
        assert not class_beranda.is_element_displayed(class_beranda.TAB_BERANDA, timeout=3), \
            "Topik Populer gagal membuka halaman baru"

    # ── BERANDA-05 ───────────────────────────────────────────────────────────

    @allure.story("Jelajahi Layanan (Login)")
    @allure.title("BERANDA-05: Jelajahi Layanan Kategori Kesehatan saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_jelajahi_layanan_kesehatan(self, class_driver, class_beranda):
        class_beranda.tap_kategori_kesehatan()
        class_beranda.safe_tap_back()

    # ── BERANDA-06 ───────────────────────────────────────────────────────────

    @allure.story("Jelajahi Layanan (Login)")
    @allure.title("BERANDA-06: Lihat Semua Jelajahi Layanan saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_lihat_semua_jelajahi_layanan(self, class_driver, class_beranda):
        class_beranda.tap_lihat_semua_jelajahi_layanan()
        time.sleep(2)
        # Verifikasi halaman kategori terbuka
        src = class_driver.page_source
        assert any(kw in src for kw in [
            'Bantuan', 'Kesehatan', 'Pendidikan', 'Pemerintahan', 'Layanan'
        ]), "Halaman Jelajahi Layanan tidak terbuka."
        class_beranda.safe_tap_back()

    # ── BERANDA-07 ───────────────────────────────────────────────────────────

    @allure.story("Info Layanan (Login)")
    @allure.title("BERANDA-07: Info Layanan Terbaru tampil dan bisa diklik saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_info_layanan(self, class_driver, class_beranda):
        class_beranda.tap_item_info_layanan()
        class_beranda.safe_tap_back()

    # ── BERANDA-08 ───────────────────────────────────────────────────────────

    @allure.story("Pencarian (Login)")
    @allure.title("BERANDA-08: Pencarian dari beranda saat login")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda_pencarian(self, class_driver, class_beranda):
        class_beranda.go_to_cari()
        time.sleep(1)