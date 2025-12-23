"""Tests for Only.Digital using Page Object Model with Locators"""
from pages.home_page import OnlyDigitalHomePage, OnlyDigitalHomePageLocators


class TestOnlyDigitalLocators:
    """Tests using locators for Only.Digital"""
    
    def test_page_loads_with_logo(self, driver):
        """Test: Page loads and logo is visible"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_logo_visible()
    
    def test_email_contact_visible(self, driver):
        """Test: Email contact link is visible"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_email_visible()
        assert "hello@only.digital" in home.get_email()
    
    def test_phone_contact_visible(self, driver):
        """Test: Phone contact link is visible"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_phone_visible()
        assert "+7" in home.get_phone()
    
    def test_telegram_link_visible(self, driver):
        """Test: Telegram link is visible"""
        home = OnlyDigitalHomePage(driver)
        telegram_url = home.get_telegram_url()
        assert "t.me" in telegram_url
    
    def test_start_project_button_clickable(self, driver):
        """Test: Start project button is visible and clickable"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_start_project_btn_visible()
    
    def test_projects_section_visible(self, driver):
        """Test: Projects section is visible"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_projects_section_visible()
    
    def test_project_cards_exist(self, driver):
        """Test: Multiple project cards are present"""
        home = OnlyDigitalHomePage(driver)
        project_count = home.get_project_cards_count()
        assert project_count > 0
    
    def test_footer_visible(self, driver):
        """Test: Footer section is visible"""
        home = OnlyDigitalHomePage(driver)
        assert home.is_footer_visible()
    
    def test_locator_email_link(self, driver):
        """Test: Locator for email link works"""
        email_element = driver.find_element(*OnlyDigitalHomePageLocators.EMAIL_LINK)
        assert email_element.is_displayed()
    
    def test_locator_phone_link(self, driver):
        """Test: Locator for phone link works"""
        phone_element = driver.find_element(*OnlyDigitalHomePageLocators.PHONE_LINK)
        assert phone_element.is_displayed()
    
    def test_locator_start_button(self, driver):
        """Test: Locator for start project button works"""
        button = driver.find_element(*OnlyDigitalHomePageLocators.START_PROJECT_BTN)
        assert button.is_displayed()
    
    def test_locator_projects_heading(self, driver):
        """Test: Locator for projects heading works"""
        heading = driver.find_element(*OnlyDigitalHomePageLocators.PROJECTS_HEADING)
        assert heading.is_displayed()
