from appium.webdriver.common.appiumby import AppiumBy
from page.base_page import BasePage

class SidebarComponent(BasePage):
    TOMBOL_BURGER = (AppiumBy.XPATH, "(//android.widget.Button)[1]")
    BERANDA = (AppiumBy.ACCESSIBILITY_ID, "Beranda")
    LAYANAN_PUBLIK = (AppiumBy.ACCESSIBILITY_ID, "Layanan Publik")
    INFORMASI_LAYANAN = (AppiumBy.ACCESSIBILITY_ID, "Informasi Layanan")
    ADUAN_BANTUAN = (AppiumBy.ACCESSIBILITY_ID, "Aduan & Bantuan")
    KATEGORI_LAYANAN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Maritim")')

    def tap_burger(self):
        self.tap(self.TOMBOL_BURGER)

    def tap_beranda(self):
        self.tap(self.BERANDA)

    def tap_layanan_publik(self):
        self.tap(self.LAYANAN_PUBLIK)
        self.tap(self.KATEGORI_LAYANAN)

    def tap_informasi_layanan(self):
        self.tap(self.INFORMASI_LAYANAN)

    def tap_aduan_bantuan(self):
        self.tap(self.ADUAN_BANTUAN) 