from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage

class LoginPage(BasePage):
    TOMBOL_MASUK_BERANDA = (AppiumBy.ACCESSIBILITY_ID, "Masuk")
    EMAIL_FIELD = (AppiumBy.XPATH, "(//android.widget.EditText)[1]")
    PASSWORD_FIELD = (AppiumBy.XPATH, "(//android.widget.EditText)[2]")
    TOMBOL_MASUK = (AppiumBy.ACCESSIBILITY_ID, "Masuk ke akun IKD")
    HOME_INDICATOR = (AppiumBy.ACCESSIBILITY_ID, "Benefit Anda")
    LOGIN_PAGE_INDICATOR = (AppiumBy.ACCESSIBILITY_ID, "Masuk ke akun Anda")
    ERROR_NO_INTERNET = (AppiumBy.ACCESSIBILITY_ID, "No internet connection. Please check your network.")
    ERROR_EMPTY_FIELDS = (AppiumBy.ACCESSIBILITY_ID, "Username/NIK dan PIN wajib diisi.")
    TOGGLE_PASSWORD = (AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.EditText[2]/android.widget.Button")

    def __init__(self, driver):
        super().__init__(driver)
    
    def navigate_to_login(self):
        try:
            self.tap(self.TOMBOL_MASUK_BERANDA, timeout=3)
        except:
            pass
        self.find_element(self.LOGIN_PAGE_INDICATOR, timeout=3)

    def enter_email(self, email: str):
        self.type_text(self.EMAIL_FIELD, email)

    def enter_password(self, password:str):
        self.type_text(self.PASSWORD_FIELD, password)

    def tap_login_button(self):
        self.tap(self.TOMBOL_MASUK)

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        try:
            self.driver.hide_keyboard()
        except:
            pass
        self.tap_login_button()

    def is_home_screen_displayed(self, timeout=5):
        return self.is_element_displayed(self.HOME_INDICATOR, timeout=timeout)
        
    def is_no_internet_error_displayed(self):
        return self.is_element_displayed(self.ERROR_NO_INTERNET, timeout=5)
        
    def is_empty_fields_error_displayed(self):
        return self.is_element_displayed(self.ERROR_EMPTY_FIELDS, timeout=5)
        
    def tap_toggle_password(self):
        self.tap(self.TOGGLE_PASSWORD)

    def logout(self):
        self.go_to_profil()
        import time
        time.sleep(1)
        locator = (AppiumBy.ACCESSIBILITY_ID, "Keluar")
        if not self.is_element_displayed(locator, timeout=3):
            for _ in range(10):
                window_size = self.driver.get_window_size()
                # Swipe kecil agar tidak kejauhan
                self.driver.swipe(
                    window_size['width'] * 0.5,
                    window_size['height'] * 0.60,
                    window_size['width'] * 0.5,
                    window_size['height'] * 0.45,
                    600
                )
                time.sleep(0.5)
                if self.is_element_displayed(locator, timeout=1):
                    break
        self.tap(locator)

