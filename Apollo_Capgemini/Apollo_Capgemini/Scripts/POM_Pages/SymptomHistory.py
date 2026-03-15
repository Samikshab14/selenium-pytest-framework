import time

from selenium.common import StaleElementReferenceException

from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper


class GenerateReport(HomePage):
    blog_link = ('xpath', '//a[text()="Blogs"]')
    view_more = ('xpath', '//h2[text()="Guide for Mounjaro Dosage: How to Use Mounjaro for Diabetes and Weight Loss?"]')
    second_blog = ('xpath', '(//span[@class="blog_editorImg__nKfce"])[2]')
    symptom_check = ('xpath', '(//p[text()="Check Your Symptoms Here"])[2]')
    start_symptom = ('xpath', '//p[@class="SymptomChecker_txt__HoIFk"]')
    continue_btn = ('xpath', '(//span[text()="Continue"])[1]')
    female_option = ('xpath', '//p[text()="Female"]')
    age_input = ('xpath', '//input[@placeholder="Enter age between 0-99"]')
    cough_option = ('xpath', '//span[text()="Cough"]')
    none_option = ('xpath', '//p[text()="None"]')
    no_option = ('xpath', '//p[text()="No"]')
    dry_cough = ('xpath', '//li[text()="Dry cough"]')
    suddenly_option = ('xpath', '//li[text()="Suddenly"]')
    moderate_option = ('xpath', '//div[text()="Moderate"]')
    allergy_option = ('xpath', '//li[text()="Allergy"]')
    radio_yes = ('xpath', '(//input[@type="radio"])[2]')
    stuffy_nose = ('xpath', '//li[text()="Stuffy nose"]')
    result_text = ('xpath', '//h2[contains(text(),"Results")]')

    def start_symptom_checker(self,age):
        wrapper = Wrapper(self.driver)
        time.sleep(2)

        # wrapper.scroll_to_element(self.view_more)
        wrapper.click_item(self.second_blog)
        time.sleep(1)

        wrapper.click_item(self.symptom_check)
        wrapper.click_item(self.start_symptom)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.female_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.enter_text(self.age_input, value=age)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.cough_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.none_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.no_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.dry_cough)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.suddenly_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.moderate_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.allergy_option)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.radio_yes)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.radio_yes)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        wrapper.click_item(self.stuffy_nose)
        time.sleep(1)
        wrapper.click_item(self.continue_btn)

        time.sleep(1)
        print("Symptom checker completed successfully.")


