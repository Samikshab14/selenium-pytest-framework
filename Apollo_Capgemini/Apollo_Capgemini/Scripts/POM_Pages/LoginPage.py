import time
from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper


class LoginPage(HomePage):
    mobile_no = ("name", "mobileNumber")
    continue_button = ('xpath', '//button[text()="Continue"]')
    verify_otp = ('xpath', '//input[@type="tel"]')
    verify_button = ('xpath', '//button[text()="Verify"]')
    login_error_msg = ("xpath", '''//div[contains(text()," Incorrect OTP")]''')

    def login(self, mobile):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.mobile_no, value=mobile)
        wrapper.click_item(self.continue_button)
        wrapper.visibilty_element_(self.verify_otp)
        time.sleep(15)
        wrapper.click_item(self.verify_button)

    def verify_unsuccessful_login(self,message):
        wrapper=Wrapper(self.driver)
        msg=wrapper.get_text(self.login_error_msg)
        assert msg == message