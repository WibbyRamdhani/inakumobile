import pytest
import allure
from page.sidebar_component import SidebarComponent
from page.base_page import BasePage

class TestSidebar:

    @allure.story("Sidebar")
    @allure.title("Beranda")
    @allure.severity(allure.severity_level.NORMAL)
    def test_beranda(self, driver):
        sidebar = SidebarComponent(driver)
        sidebar.tap_burger()
        sidebar.tap_beranda()

    @allure.story("Sidebar")
    @allure.title("Layanan Publik")
    @allure.severity(allure.severity_level.NORMAL)
    def test_layanan(self, driver):
        sidebar = SidebarComponent(driver)
        sidebar.tap_burger()
        sidebar.tap_layanan_publik()

    @allure.story("Sidebar")
    @allure.title("Informasi Layanan")
    @allure.severity(allure.severity_level.NORMAL)
    def test_informasi(self, driver):
        sidebar = SidebarComponent(driver)
        sidebar.tap_burger()
        sidebar.tap_informasi_layanan()

    @allure.story("Sidebar")
    @allure.title("Aduan dan Bantuan")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason="Belum implementasi")
    def test_aduan_bantuan(self, driver):
        sidebar = SidebarComponent(driver)
        sidebar.tap_burger()
        sidebar.tap_aduan_bantuan()

