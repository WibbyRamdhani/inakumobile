import pytest
import allure
import time
from page.login_pages import LoginPage

@allure.feature("Login")
class TestLogin:
    
    @allure.story("Login dengan kredensial valid")
    @allure.title("LOGIN-01: Login dengan kredensial valid")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_kredensial_valid(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("admin@portal.dev", "Admin123!")
        for _ in range(20):
            if not login_page.is_element_displayed(login_page.LOGIN_PAGE_INDICATOR, timeout=0.5):
                break
            time.sleep(0.5)
        login_page.go_to_beranda()
        is_home = login_page.is_element_displayed(login_page.HOME_INDICATOR, timeout=5)
        assert is_home, "Setelah login sukses dan kembali ke beranda, elemen Benefit harus tampil."

    @allure.story("Login dengan kredensial tidak valid")
    @allure.title("LOGIN-02: Login dengan password salah")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_password_salah(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("admin@portal.dev", "budidor3mi!")
        is_home = login_page.is_home_screen_displayed()
        assert not is_home, "Seharusnya tidak berhasil login dengan password yang salah."

    @allure.story("Login dengan kredensial tidak valid")
    @allure.title("LOGIN-03: Login dengan username/email tidak terdaftar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_username_tidak_terdaftar(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("user_tidak_ada@portal.dev", "Admin123!")
        is_home = login_page.is_home_screen_displayed()
        assert not is_home, "Seharusnya tidak berhasil login dengan email yang tidak terdaftar."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-04: Login dengan field kosong (keduanya)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_field_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("", "")
        assert login_page.is_empty_fields_error_displayed(), "Pesan error field kosong harus muncul."
        is_home = login_page.is_home_screen_displayed(timeout=1)
        assert not is_home, "Seharusnya tidak berhasil login dengan field kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-05: Login dengan username kosong, password terisi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_dengan_username_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("", "Admin123!")
        is_home = login_page.is_home_screen_displayed()
        assert not is_home, "Seharusnya tidak berhasil login dengan username kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-06: Login dengan password kosong, username terisi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_dengan_password_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("admin@portal.dev", "")
        is_home = login_page.is_home_screen_displayed()
        assert not is_home, "Seharusnya tidak berhasil login dengan password kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-07: Format email tidak valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_format_email_tidak_valid(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("adminportal.dev", "Admin123!")
        is_home = login_page.is_home_screen_displayed()
        assert not is_home, "Seharusnya tidak berhasil login dengan format email tidak valid."

    @allure.story("UI Interaction")
    @allure.title("LOGIN-08: Tombol show/hide password")
    @allure.severity(allure.severity_level.MINOR)
    def test_tombol_show_hide_password(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.enter_password("Admin123!")
        login_page.tap_toggle_password()

    # @allure.story("Kondisi Jaringan")
    # @allure.title("LOGIN-10: Tanpa koneksi internet")
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_tanpa_koneksi_internet(self, driver, login_page):
    #     login_page.navigate_to_login()
    #     driver.set_network_connection(0)
    #     try:
    #         login_page.login("admin@portal.dev", "Admin123!")
    #         is_home = login_page.is_home_screen_displayed(timeout=3)
    #         assert not is_home, "Seharusnya muncul pesan error koneksi, bukan berhasil login."
    #         assert login_page.is_no_internet_error_displayed(), "Pesan error koneksi internet harus muncul."
    #     finally:
    #         driver.set_network_connection(6)

    # @allure.story("Session Management")
    # @allure.title("LOGIN-11: Session tetap login setelah app ditutup-buka lagi")
    # @allure.severity(allure.severity_level.MINOR)
    # def test_session_tetap_login(self, driver, login_page):
    #     login_page.navigate_to_login()
    #     login_page.login("admin@portal.dev", "Admin123!")
    #     for _ in range(20):
    #         if not login_page.is_element_displayed(login_page.LOGIN_PAGE_INDICATOR, timeout=0.5):
    #             break
    #         time.sleep(0.5)
    #     login_page.go_to_beranda()
    #     assert login_page.is_element_displayed(login_page.HOME_INDICATOR, timeout=5), "Harus berhasil login dulu"
    #     app_package = driver.capabilities.get('appPackage')
    #     if app_package:
    #         driver.terminate_app(app_package)
    #         driver.activate_app(app_package)
    #         assert login_page.is_element_displayed(login_page.HOME_INDICATOR, timeout=3), "Session harus tersimpan setelah aplikasi ditutup dan dibuka lagi"

    # @allure.story("Session Management")
    # @allure.title("LOGIN-12: Logout lalu coba akses halaman yang butuh login")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_logout_akses_halaman_login(self, driver, login_page):
    #     login_page.navigate_to_login()
    #     login_page.login("admin@portal.dev", "Admin123!")
    #     for _ in range(20):
    #         if not login_page.is_element_displayed(login_page.LOGIN_PAGE_INDICATOR, timeout=0.5):
    #             break
    #         time.sleep(0.5)
    #     login_page.go_to_beranda()
    #     assert login_page.is_element_displayed(login_page.HOME_INDICATOR, timeout=5), "Harus berhasil login dulu"
    #     login_page.logout()
    #     assert login_page.is_element_displayed(login_page.LOGIN_PAGE_INDICATOR, timeout=3), "Harus kembali ke halaman login setelah logout"

    # @allure.story("Keamanan")
    # @allure.title("LOGIN-13: Brute force / rate limiting")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_brute_force_rate_limiting(self, driver, login_page):
    #     login_page.navigate_to_login()
    #     for _ in range(5):
    #         login_page.login("admin@portal.dev", "PasswordSalah123!")
    #         time.sleep(1)
    #     is_home = login_page.is_home_screen_displayed()
    #     assert not is_home, "Seharusnya akun di-lock atau muncul rate limiting"
