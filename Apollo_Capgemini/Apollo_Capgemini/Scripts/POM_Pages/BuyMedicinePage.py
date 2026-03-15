import time
from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper

class BuyMedicinePage(HomePage):
    kwikpen_product = ('xpath', '//span[@aria-label="Kwikpen"]')
    add_to_cart = ('xpath', '//span[text()="Add to Cart"]')
    view_cart = ('xpath', '//span[text()="View Cart"]')




    def add_product_to_cart_and_proceed(self):
        wrapper = Wrapper(self.driver)

        wrapper.click_item(self.kwikpen_product)
        time.sleep(2)

        wrapper.scroll_to_element(self.add_to_cart)
        wrapper.click_item(self.add_to_cart)
        time.sleep(2)

        wrapper.click_item(self.view_cart)
        time.sleep(3)


        print(" Product added to cart and proceeded successfully")
