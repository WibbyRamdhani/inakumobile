import pytest
import allure
import time
from appium import webdriver
from page.beranda_page import BerandaPage
from page.footer_component import FooterComponent

class TestFooter:
    @pytest.fixture(autouse=True)
    def reset_to_beranda(self, class_beranda):
        class_beranda.go_to_beranda()

    @allure.story("FOOTER")
    @allure.title("FOOTER-01: FAQ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_footer_faq(self, class_driver):
        footer_page = FooterComponent(class_driver)
        BerandaPage(class_driver).scroll_ke_bawah()
        footer_page.tap_lihat_pertanyaan_umum()

    @allure.story("FOOTER")
    @allure.title("FOOTER-02: Media Sosial")
    @allure.severity(allure.severity_level.NORMAL)
    def test_footer_medsos(self, class_driver):
        footer_page = FooterComponent(class_driver)
        BerandaPage(class_driver).scroll_ke_bawah()
        footer_page.tap_sosmed("ig")

    @allure.story("FOOTER")
    @allure.title("FOOTER-03: Toggle")
    @allure.severity(allure.severity_level.NORMAL)
    def test_footer_toggle(self, class_driver):
        footer_page = FooterComponent(class_driver)
        BerandaPage(class_driver).scroll_ke_bawah()
        footer_page.tap_toggle_layanan_publik()
        footer_page.tap_toggle_bantuan()
           