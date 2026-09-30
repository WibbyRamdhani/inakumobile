import pytest
import allure
import time
from page.login_pages import LoginPage

# Credentials yang valid untuk testing
VALID_EMAIL = "hernanda17@hotmail.com"
VALID_PASSWORD = "Bebas884422"


@allure.feature("Login")
class TestLogin:

    # ─── NEGATIVE TESTS (jalankan duluan, tidak mengubah login state) ───

    @allure.story("Login dengan kredensial tidak valid")
    @allure.title("LOGIN-01: Login dengan password salah")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_password_salah(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login(VALID_EMAIL, "PasswordSalah123!")
        time.sleep(3)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan password yang salah."

    @allure.story("Login dengan kredensial tidak valid")
    @allure.title("LOGIN-02: Login dengan email tidak terdaftar")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_email_tidak_terdaftar(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("user_tidak_ada@example.com", VALID_PASSWORD)
        time.sleep(3)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan email yang tidak terdaftar."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-03: Login dengan field kosong (keduanya)")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_field_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.tap_login_button()
        time.sleep(2)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan field kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-04: Login dengan email kosong, password terisi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_dengan_email_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("", VALID_PASSWORD)
        time.sleep(2)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan email kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-05: Login dengan password kosong, email terisi")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_dengan_password_kosong(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.enter_email(VALID_EMAIL)
        try:
            login_page.driver.hide_keyboard()
        except Exception:
            pass
        login_page.tap_login_button()
        time.sleep(2)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan password kosong."

    @allure.story("Validasi Field Login")
    @allure.title("LOGIN-06: Format email tidak valid")
    @allure.severity(allure.severity_level.NORMAL)
    def test_format_email_tidak_valid(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login("bukan-email-valid", VALID_PASSWORD)
        time.sleep(2)
        assert login_page.is_still_on_login_page(), \
            "Seharusnya tetap di halaman login dengan format email tidak valid."

    @allure.story("UI Interaction")
    @allure.title("LOGIN-07: Tombol show/hide password")
    @allure.severity(allure.severity_level.MINOR)
    def test_tombol_show_hide_password(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.enter_password("TestPassword123!")
        login_page.tap_toggle_password()
        time.sleep(1)

    # ─── POSITIVE TEST (terakhir, karena akan login & mengubah app state) ───

    @allure.story("Login dengan kredensial valid")
    @allure.title("LOGIN-08: Login dengan kredensial valid")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_dengan_kredensial_valid(self, driver, login_page):
        login_page.navigate_to_login()
        login_page.login(VALID_EMAIL, VALID_PASSWORD)
        time.sleep(5)
        # Setelah login, seharusnya kembali ke beranda
        login_page.go_to_beranda()
        is_home = login_page.is_home_screen_displayed(timeout=8)
        assert is_home, "Setelah login sukses, beranda harus tampil."
        # Logout supaya tidak ganggu test berikutnya
        login_page.logout()
        time.sleep(2)
