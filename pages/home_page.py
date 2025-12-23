"""Page Object Model for Only.Digital home page with Locators"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OnlyDigitalHomePageLocators:
    """Locators for Only.Digital home page"""
    
    # Navigation & Header
    LOGO = (By.XPATH, "//a[@href='/']") 
    MENU_BUTTON = (By.CSS_SELECTOR, "button[aria-label*='menu']")
    
    # Contact Information
    EMAIL_LINK = (By.XPATH, "//a[contains(@href, 'mailto:hello@only.digital')]")
    PHONE_LINK = (By.XPATH, "//a[contains(@href, 'tel:+7')]") 
    TELEGRAM_LINK = (By.XPATH, "//a[contains(@href, 't.me')]") 
    TELEGRAM_TEXT = (By.XPATH, "//*[contains(text(), '@onlydigitalagency')]")
    
    # Main Call-to-Action Button
    START_PROJECT_BTN = (By.XPATH, "//button[contains(text(), 'проект')]")
    
    # Sections Headers
    PROJECTS_HEADING = (By.XPATH, "//*[contains(text(), 'проекты')]")
    CLIENTS_HEADING = (By.XPATH, "//*[contains(text(), 'клиенты')]")
    DIRECTIONS_HEADING = (By.XPATH, "//*[contains(text(), 'направления')]")
    AWARDS_HEADING = (By.XPATH, "//*[contains(text(), 'награды')]")
    
    # Projects Section
    PROJECT_CARDS = (By.CSS_SELECTOR, "[class*='project'], [data-test*='project']")
    PROJECT_NAME = (By.CSS_SELECTOR, "h3, [class*='title']")
    
    # Clients Section
    CLIENT_LOGOS = (By.CSS_SELECTOR, "[class*='client'], [data-test*='client']")
    INDUSTRY_FILTERS = (By.XPATH, "//a[contains(@href, '/projects/industry/')]")
    
    # Awards Section
    AWARD_ITEMS = (By.CSS_SELECTOR, "[class*='award'], [data-test*='award']")
    AWARD_COUNT = (By.CSS_SELECTOR, "[class*='count']")
    
    # Footer
    FOOTER = (By.TAG_NAME, "footer")
    SOCIAL_LINKS = (By.XPATH, "//a[contains(@href, 'behance') or contains(@href, 'vk.com') or contains(@href, 't.me')]")
    PRIVACY_LINK = (By.XPATH, "//a[contains(@href, 'privacy') or contains(text(), 'Политика')]")
    
    # Carousel/Slider
    NEXT_SLIDE_BTN = (By.XPATH, "//button[contains(text(), 'следующий')]")
    PREV_SLIDE_BTN = (By.XPATH, "//button[contains(text(), 'предыдущий')]")


class OnlyDigitalHomePage:
    """Page Object for Only.Digital home page"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.locators = OnlyDigitalHomePageLocators()
    
    # ===== VISIBILITY CHECKS =====
    
    def is_logo_visible(self) -> bool:
        """Check if logo is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.LOGO))
            return True
        except:
            return False
    
    def is_email_visible(self) -> bool:
        """Check if email link is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.EMAIL_LINK))
            return True
        except:
            return False
    
    def is_phone_visible(self) -> bool:
        """Check if phone link is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.PHONE_LINK))
            return True
        except:
            return False
    
    def is_start_project_btn_visible(self) -> bool:
        """Check if start project button is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.START_PROJECT_BTN))
            return True
        except:
            return False
    
    def is_projects_section_visible(self) -> bool:
        """Check if projects section is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.PROJECTS_HEADING))
            return True
        except:
            return False
    
    def is_footer_visible(self) -> bool:
        """Check if footer is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.locators.FOOTER))
            return True
        except:
            return False
    
    # ===== ELEMENT RETRIEVAL =====
    
    def get_email(self) -> str:
        """Get email from link"""
        element = self.driver.find_element(*self.locators.EMAIL_LINK)
        return element.get_attribute('href')
    
    def get_phone(self) -> str:
        """Get phone from link"""
        element = self.driver.find_element(*self.locators.PHONE_LINK)
        return element.get_attribute('href')
    
    def get_telegram_url(self) -> str:
        """Get Telegram URL"""
        element = self.driver.find_element(*self.locators.TELEGRAM_LINK)
        return element.get_attribute('href')
    
    def get_project_cards_count(self) -> int:
        """Get number of project cards"""
        return len(self.driver.find_elements(*self.locators.PROJECT_CARDS))
    
    def get_client_logos_count(self) -> int:
        """Get number of client logos"""
        return len(self.driver.find_elements(*self.locators.CLIENT_LOGOS))
    
    # ===== ACTIONS =====
    
    def click_start_project_button(self):
        """Click start project button"""
        element = self.wait.until(EC.element_to_be_clickable(self.locators.START_PROJECT_BTN))
        element.click()
    
    def click_email_link(self):
        """Click email link"""
        element = self.wait.until(EC.element_to_be_clickable(self.locators.EMAIL_LINK))
        element.click()
    
    def click_next_slide(self):
        """Click next slide button"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.locators.NEXT_SLIDE_BTN))
            element.click()
            return True
        except:
            return False
    
    # ===== PAGE PROPERTIES =====
    
    def get_page_title(self) -> str:
        """Get page title"""
        return self.driver.title
    
    def get_current_url(self) -> str:
        """Get current URL"""
        return self.driver.current_url
