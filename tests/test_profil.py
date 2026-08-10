import pytest
import allure
import time
from page.profil_page import ProfilPage
from page.beranda_page import BerandaPage
from page.login_pages import LoginPage

@allure.feature("Profil")
class TestProfil:
    @pytest.fixture(scope="class", autouse=True)
    @classmethod
    def setup_login_class(cls, class_beranda, class_login):
        try:
            class_beranda.tap_masuk_header()
        except:
            pass
        class_login.login("admin@portal.dev", "Admin123!")
        for _ in range(20):
            if not class_beranda.is_element_displayed(class_login.LOGIN_PAGE_INDICATOR, timeout=0.5):
                break
            time.sleep(0.2)

    @pytest.fixture(autouse=True)
    def reset_to_profil(self, class_beranda):
        class_beranda.go_to_profil()

    @allure.story("Profil")
    @allure.title("PROFIL-01: View Dokumen Saya -> Search -> Detail -> Unduh")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Masih dalam pengembangan (search)")
    def test_akses_edokumen(self, class_profil):
        class_profil.buka_edokumen()
        class_profil.buka_dokumen_saya()
        class_profil.cari_dokumen("KTP")
        class_profil.buka_detail_dokumen_pertama()
        class_profil.unduh_dokumen()

    @allure.story("Profil")
    @allure.title("PROFIL-02: View Dokumen Keluarga -> Detail Anggota -> Unduh")
    @allure.severity(allure.severity_level.NORMAL)
    def test_akses_dokumen_keluarga(self, class_profil):
        class_profil.buka_edokumen()
        class_profil.buka_dokumen_keluarga()
        # lanjut aksi

    @allure.story("Profil")
    @allure.title("PROFIL-03: View Status -> Search/Filter/Sort -> Detail Status")
    @allure.severity(allure.severity_level.NORMAL)
    def test_akses_status(self, class_profil):
        class_profil.buka_status()
        # lanjut aksi

    @allure.story("Profil")
    @allure.title("PROFIL-04: Uji Toggle Notifikasi (Notifikasi Email, Pembaruan Permohonan, Peringatan Keamanan)")
    @allure.severity(allure.severity_level.NORMAL)
    def test_toggle_pengaturan(self, class_profil):
        class_profil.buka_pengaturan()
        class_profil.toggle_notifikasi_email()
        time.sleep(0.1)
        class_profil.toggle_pembaruan_permohonan()
        time.sleep(0.1)
        class_profil.toggle_peringatan_keamanan()
