from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper


class HomePage(Wrapper):
    login_link=("xpath",'//span[@class="HeaderNew_loginCTATxt__nYlvD"]')
    blog_link = ('xpath', '//a[text()="Blogs"]')

    def __init__(self,driver):
        super().__init__(driver)

    def click_login(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_item(self.login_link)

    def click_blog_link(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_item(self.blog_link)