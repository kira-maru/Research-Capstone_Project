from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from functions import input_data, find_and_click
from research_brain import ResearchBrain
import time

# Setting driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class SheetMaker:
    """Automated sheet maker with google forms"""
    def __init__(self, form_website):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(form_website)
        self.wait = WebDriverWait(self.driver, 10)
        self.rb = ResearchBrain()

    def form_fill(self):
        """Automated filling form function"""
        for i in range(len(self.rb.prices)):

            inputs = self.driver.find_elements(By.CSS_SELECTOR, ".whsOnd.zHQkBf")
            inputs_list = [box_q for box_q in inputs]

            time.sleep(2)

            input_data(wait=self.wait, ec=EC, element=inputs_list[0], data=self.rb.addresses[i])
            input_data(wait=self.wait, ec=EC, element=inputs_list[1], data=self.rb.prices[i])
            input_data(wait=self.wait, ec=EC, element=inputs_list[2], data=self.rb.links[i])

            time.sleep(2)

            find_and_click(wait=self.wait, ec=EC, by=By.CSS_SELECTOR, value="div[role='button']")
            find_and_click(wait=self.wait, ec=EC, by=By.CSS_SELECTOR, value="a[href]")

            time.sleep(2)

        self.driver.quit()

    def create_sheet(self, resp_website, s_name=None):
        """Creates sheet from provided google's form URL with responses.
        Optional argument to name the sheet - if not used, then sheet's name will be 'Sheet1'"""
        if not s_name:
            s_name = "Sheet1"
        else:
            pass

        self.driver.get(resp_website)
        time.sleep(2)

        find_and_click(self.wait, EC, By.CSS_SELECTOR, "div[role='button'].uArJ5e")
        time.sleep(2)

        sheet_name = self.driver.find_element(By.CSS_SELECTOR, "div input .whsOnd")
        sheet_name.clear()
        time.sleep(1)
        input_data(self.wait, EC, By.CSS_SELECTOR, "div input .whsOnd", s_name)
        find_and_click(self.wait, EC, By.CSS_SELECTOR, "div[role='button'].HvOprf")

    def download_csv(self, resp_website):
        """Downloads csv with responses from provided google's sheet URL"""
        self.driver.get(resp_website)

        find_and_click(self.wait, EC, By.CLASS_NAME, "JfdRKe")
        find_and_click(self.wait, EC, By.CSS_SELECTOR, ".uyYuVb.oJeWuf")











