import time

from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper

class DiabetesManagement(HomePage):

    service_option = ('xpath', '//span[@class="articledetail_serviceImg__7CgpQ"]')


    def add_product_to_cart_and_proceed(self):
        wrapper = Wrapper(self.driver)

        wrapper.click_item(self.service_option)
        time.sleep(2)

