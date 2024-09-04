import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CHROMEDRIVER_PATH, TARGET_URL

class TangentTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test_navigation_and_form_submission(self):
        driver = self.driver
        driver.get(TARGET_URL)

        # Wait for the main heading to be present
        main_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="lead"]/div/div/h3/a'))
        )
        main_heading_text = main_heading.text
        
        # Click on the main heading
        main_heading.click()

        # Switch to the new window
        driver.switch_to.window(driver.window_handles[-1])

        # Wait for the popup heading to be present
        popup_heading = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="overview"]/div[2]/div/div/div[2]/div/div[1]/h1/a'))
        )
        popup_heading_text = popup_heading.text

        # Compare the texts
        self.assertEqual(main_heading_text, popup_heading_text, "The headings do not match. Test failed.")
      
    def tearDown(self):
        # Keep the browser open for a while before quitting (for debugging purposes)
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
