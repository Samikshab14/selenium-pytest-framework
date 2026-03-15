import time

from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.Utilities.Gen_Utility import Wrapper

class BlogPage(HomePage):
    search_bar = ('xpath', '//input[@placeholder="Search Articles"]')
    auto_suggestions = ('xpath', '//div[contains(@class,"ArticleSearch_searchResultsWrap")]/section/ul/li/a')
    no_results_msg = ('xpath', '//h3[contains(@class,"ArticleSearch_notFound")]')
    diabetes_category = ('xpath', '//p[text()="Diabetes Management"]')
    first_article=('xpath','''//h2[text()="Guide for Mounjaro Dosage: How to Use Mounjaro for Diabetes and Weight Loss?"]''')


    def switch_to_blog_window(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if "blog" in self.driver.current_url:
                break

    def validate_autosuggestions(self, text):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.search_bar, value=text)
        time.sleep(2)
        suggestions = self.driver.find_elements(*self.auto_suggestions)
        assert len(suggestions) > 0, "No auto-suggestions displayed"
        print("Auto-suggestions are visible in Blog search")

    def search_invalid_article(self, text):
        wrapper = Wrapper(self.driver)
        try:
            wrapper.enter_text(self.search_bar, value=text)

            self.driver.find_element(*self.search_bar).send_keys("\n")

            assert wrapper.is_element_visible(self.no_results_msg), "No results message not displayed"
            print("No results found message displayed")
        except :
            print("Article related to search ")

    def select_category(self):
        wrapper = Wrapper(self.driver)
        wrapper.scroll_to_element(self.diabetes_category)
        wrapper.click_item(self.diabetes_category)
        time.sleep(2)
        wrapper.take_screenshot()
        assert "diabetes-management" in self.driver.current_url, "URL validation failed!"
        print("Diabetes Management category opened successfully")

    def add_to_cart_flow(self):
        wrapper = Wrapper(self.driver)
        wrapper.scroll_to_element(self.first_article)
        wrapper.click_item(self.first_article)
        time.sleep(2)




