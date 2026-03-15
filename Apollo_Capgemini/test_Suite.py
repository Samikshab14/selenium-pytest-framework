import time
import unittest
import argparse
import HtmlTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from Apollo_Capgemini.Scripts.POM_Pages.LoginPage import LoginPage
from Apollo_Capgemini.Scripts.Utilities.excel_utility import read_excel_data
from Apollo_Capgemini.Scripts.POM_Pages.Homepage import HomePage
from Apollo_Capgemini.Scripts.POM_Pages.BlogHomePage import BlogPage
from Apollo_Capgemini.Scripts.POM_Pages.DiabetesManagement import DiabetesManagement
from Apollo_Capgemini.Scripts.POM_Pages.BuyMedicinePage import BuyMedicinePage
from Apollo_Capgemini.Scripts.POM_Pages.SymptomHistory import GenerateReport


parser = argparse.ArgumentParser()
parser.add_argument("--browser", default="chrome", help="Browser name: chrome/firefox/edge")
args, unknown = parser.parse_known_args()


class ApolloTestSuite(unittest.TestCase):
    data=read_excel_data(r'C:\Users\Samiksha Bandgar\PycharmProjects\Apollo_Capgemini\Apollo_Capgemini\test_data\details.xls',"Data")
    def setUp(self):

        browser = args.browser.lower()

        if browser == "chrome":
            opts = ChromeOptions()
            opts.add_experimental_option("detach", True)
            opts.add_argument("--disable-notifications")
            self.driver = Chrome(opts)

        elif browser == "firefox":
            options = FirefoxOptions()
            options.set_preference("dom.webnotifications.enabled", False)
            self.driver = Firefox(options=options)

        elif browser == "edge":
            self.driver = Edge()

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver.get("https://www.apollo247.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        print("Exiting the Suite")

    def test_Login(self):
        homepage = HomePage(self.driver)
        homepage.click_login()
        loginpage = LoginPage(self.driver)
        loginpage.login(self.data["phonenumber"])


    def test_Blog_AutoSuggestion(self):
        home = HomePage(self.driver)
        blog = BlogPage(self.driver)

        home.click_blog_link()
        blog.switch_to_blog_window()
        blog.validate_autosuggestions(self.data["valid_data"])

    def test_Invalid_Article_Search(self):
        home = HomePage(self.driver)
        blog = BlogPage(self.driver)
        home.click_blog_link()
        blog.switch_to_blog_window()
        blog.search_invalid_article(self.data["Invalid_data"])

    def test_Category_Selection(self):
        home = HomePage(self.driver)
        blog = BlogPage(self.driver)
        home.click_blog_link()
        blog.switch_to_blog_window()
        blog.select_category()

    def test_Add_To_Cart_From_Blog(self):
        home = HomePage(self.driver)
        blog = BlogPage(self.driver)
        diabetes = DiabetesManagement(self.driver)
        medicine = BuyMedicinePage(self.driver)
        home.click_blog_link()
        blog.switch_to_blog_window()
        blog.add_to_cart_flow()
        diabetes.add_product_to_cart_and_proceed()
        medicine.add_product_to_cart_and_proceed()

    def test_Generate_report(self):
        home = HomePage(self.driver)
        home.click_blog_link()
        blog = BlogPage(self.driver)
        blog.switch_to_blog_window()
        symptom = GenerateReport(self.driver)
        symptom.start_symptom_checker(self.data["age"])

    @unittest.skip("skip this test temporary")
    def test_Invalid_login(self):
        homepage = HomePage(self.driver)
        homepage.click_login()
        loginpage = LoginPage(self.driver)
        loginpage.login(self.data["phonenumber"])
        loginpage.verify_unsuccessful_login(self.data["message"])


def TestSuite_Apollo():
    suite = unittest.TestSuite()
    suite.addTest(ApolloTestSuite("test_Blog_AutoSuggestion"))
    suite.addTest(ApolloTestSuite("test_Invalid_Article_Search"))
    suite.addTest(ApolloTestSuite("test_Category_Selection"))
    suite.addTest(ApolloTestSuite("test_Add_To_Cart_From_Blog"))
    suite.addTest(ApolloTestSuite("test_Generate_report"))
    suite.addTest(ApolloTestSuite("test_Invalid_login"))
    return suite



if __name__ == "__main__":
    runner = HtmlTestRunner.HTMLTestRunner(

        output="Apollo_Test_Reports",
        report_title="Apollo 24/7 Automation Test Suite Report",
        descriptions="End-to-End Tests for Apollo Blog and Product Modules"
    )
    runner.run(TestSuite_Apollo())
