from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_get_a_landing_page_with_an_image(self):
        # John hears about a site about a local church convention.
        # He goes to the homepage.
        self.browser.get('http:localhost:5000')

        # On the page they notice the page title
        self.assertIn('Bethesda Church', self.browser.title)

if __name__ == '__main__':
    unittest.main()
