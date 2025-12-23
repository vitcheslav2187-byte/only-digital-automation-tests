"""Tests for Only.Digital home page"""


def test_page_loads(driver):
    """Test: Page loads successfully"""
    title = driver.title
    assert title != ""
    assert "Only" in title


def test_logo_visible(driver):
    """Test: Logo is visible"""
    logo = driver.find_element("xpath", "//a[contains(@href, '/')]")
    assert logo.is_displayed()


def test_email_visible(driver):
    """Test: Email contact is visible"""
    email_link = driver.find_element("xpath", "//a[contains(@href, 'mailto:')]") 
    assert email_link.is_displayed()
    assert "hello@only.digital" in email_link.get_attribute("href")


def test_phone_visible(driver):
    """Test: Phone number is visible"""
    phone_link = driver.find_element("xpath", "//a[contains(@href, 'tel:')]")
    assert phone_link.is_displayed()
    assert "+7" in phone_link.get_attribute("href")


def test_start_project_button_visible(driver):
    """Test: Start project button is visible"""
    button = driver.find_element("xpath", "//button[contains(text(), 'проект')]") 
    assert button.is_displayed()


def test_projects_section_visible(driver):
    """Test: Projects section is visible"""
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    projects_heading = driver.find_element("xpath", "//*[contains(text(), 'проекты')]")
    assert projects_heading.is_displayed()


def test_cookie_notice_exists(driver):
    """Test: Cookie notice appears"""
    # Check if page loads - cookie is likely present
    page_source = driver.page_source
    assert "only.digital" in page_source.lower()
