from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Wrapper:
    def __init__(self,driver):
        self.driver=driver

    def click_item(self,locator):
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self,locator,*,value):
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(value)

    def select_option(self,locator,*,value):
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.visibility_of_element_located(locator))
        select=Select(element)
        select.select_by_visible_text(value)

    def mouse_hover(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        action=ActionChains(self.driver)
        action.move_to_element(element).perform()

    def get_text(self,locator):
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def visibilty_element_(self, locator):
            wait = WebDriverWait(self.driver, 20)
            wait.until(
                EC.visibility_of_element_located(locator))

    def scroll_to_element(self,locator):
        element=self.driver.find_element(*locator)
        action=ActionChains(self.driver)
        action.scroll_to_element(element).perform()

    def is_element_visible(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def take_screenshot(self):
        self.driver.save_screenshot(r"C:\Users\Samiksha Bandgar\PycharmProjects\Apollo_Capgemini\screenshots\home.png")