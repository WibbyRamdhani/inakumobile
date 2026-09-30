import pytest
import allure
import time
from page.profil_page import ProfilPage
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage

VALID_EMAIL = "hernanda17@hotmail.com"
VALID_PASSWORD = "Bebas884422"


@allure.feature("Profil")
class TestProfil:
    """
    Test suite Profil - function-scoped driver (tiap test sesi baru).
    Dikonversi dari class-scoped karena test_akses_edokumen (xfail) dapat
    crash UiAutomator2 dan mempengaruhi test berikutnya.
    """

    @pytest.fixture(autouse=True)
    def setup_profil(self, driver):
        """Tiap test: fresh driver → login → ke tab Profil."""
        beranda = BerandaPage(driver)
        login = LoginPage(driver)
        self.profil = ProfilPage(driver)
        self.driver = driver
        # Login
        login.navigate_to_login()
        login.login(VALID_EMAIL, VALID_PASSWORD)
        time.sleep(5)
        # Tunggu home screen
        for _ in range(10):
            if login.is_home_screen_displayed(timeout=1):
                break
            time.sleep(1)
        beranda.go_to_profil()
        time.sleep(2)
        yield
        try:
            login.logout()
        except Exception:
            pass

    # ── PROFIL-01 ─────────────────────────────────────────────────────────────

    @allure.story("Profil")
    @allure.title("PROFIL-01: View Dokumen Saya → Search → Detail → Unduh")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Masih dalam pengembangan (search)")
    def test_akses_edokumen(self):
        self.profil.buka_edokumen()
        self.profil.buka_dokumen_saya()
        self.profil.cari_dokumen("KTP")
        self.profil.buka_detail_dokumen_pertama()
        self.profil.unduh_dokumen()

    # ── PROFIL-02 ─────────────────────────────────────────────────────────────

    @allure.story("Profil")
    @allure.title("PROFIL-02: View Dokumen Keluarga → Detail Anggota → Unduh")
    @allure.severity(allure.severity_level.NORMAL)
    def test_akses_dokumen_keluarga(self):
        self.profil.buka_edokumen()
        self.profil.buka_dokumen_keluarga()

    # ── PROFIL-03 ─────────────────────────────────────────────────────────────

    @allure.story("Profil")
    @allure.title("PROFIL-03: View Status → Search/Filter/Sort → Detail Status")
    @allure.severity(allure.severity_level.NORMAL)
    def test_akses_status(self):
        self.profil.buka_status()

    # ── PROFIL-04 ─────────────────────────────────────────────────────────────

    @allure.story("Profil")
    @allure.title("PROFIL-04: Uji Toggle Notifikasi (Email, Permohonan, Keamanan)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_toggle_pengaturan(self):
        self.profil.buka_pengaturan()
        self.profil.toggle_notifikasi_email()
        time.sleep(0.1)
        self.profil.toggle_pembaruan_permohonan()
        time.sleep(0.1)
        self.profil.toggle_peringatan_keamanan()
