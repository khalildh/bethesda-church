from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Bethesda Church', header_text)


        # THe sees a button that sends Learn More about our upcoming events
        link = self.browser.find_element_by_id('link-for-info')
        self.assertEqual(
            link.text,
            'Learn more about our upcoming events'
        )
        link.click()
        time.sleep(1)


        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()
