import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CHROMEDRIVER_PATH, TARGET_URL, SCREENSHOT_PATH

class KurtosysTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_navigation_and_form_submission(self):
        driver = self.driver
        driver.get(TARGET_URL)

        # Hover over INSIGHTS to reveal the dropdown
        menu_item_xpath = '//*[@id="kurtosys-menu-item-75710"]/a/div/div/span'
        menu_item = driver.find_element(By.XPATH, menu_item_xpath)
        actions = ActionChains(driver)
        actions.move_to_element(menu_item).perform()

        # Locate and click White Papers & eBooks
        dropdown_item_xpath = '//*[@id="kurtosys-menu-item-75710"]/div/div/div/div/section/div/div/div/div/div/div/div/ul/li[3]/a/span'
        dropdown_item = driver.find_element(By.XPATH, dropdown_item_xpath)
        dropdown_item.click()

        # Verify the page title reads "White Papers"
        title_xpath = '/html/body/div[2]/div/section[1]/div/div/div/div/div/div[2]/div/h2'
        title_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, title_xpath)))
        expected_title = "White Papers"
        actual_title = title_element.text
        self.assertEqual(expected_title, actual_title, f"Title should be '{expected_title}' but was '{actual_title}'")

        # Click on "UCITS Whitepaper"
        ucits_whitepaper_xpath = '/html/body/div[2]/div/section[2]/div/div/div/div/div/div/div/div[1]/article[7]/div/div[1]/p/a'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ucits_whitepaper_xpath)))
        ucits_whitepaper = driver.find_element(By.XPATH, ucits_whitepaper_xpath)
        ucits_whitepaper.click()

        self.enter_text_by_id("18882_231669pi_18882_231669", "Fungai")  # First Name
        self.enter_text_by_id("18882_231671pi_18882_231671", "Bobo")    # Last Name
        self.enter_text_by_id("18882_231675pi_18882_231675", "Kurtosys") # Company
        self.enter_text_by_id("18882_231677pi_18882_231677", "FinTech")  # Industry

        # Click "Send me a copy" button
        send_me_a_copy_xpath = '/html/body/form/p[2]'
        driver.find_element(By.XPATH, send_me_a_copy_xpath).click()


        # Add screenshot of the error messages
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hs-error-msg")))
        driver.save_screenshot(SCREENSHOT_PATH)
        print(f"Screenshot saved to {SCREENSHOT_PATH}")

        # Validate all error messages
        error_messages = driver.find_elements(By.CLASS_NAME, "hs-error-msg")
        for error_message in error_messages:
            self.assertTrue(error_message.is_displayed(), "Error message should be displayed")

    def enter_text_by_id(self, element_id, text):
        element = self.driver.find_element(By.ID, element_id)
        element.clear()
        element.send_keys(text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
