import os
import bethesda
import unittest

class BethesdaTestCase(unittest.TestCase):

    def setUp(self):
        bethesda.app.testing = True
        self.app = bethesda.app.test_client()


    def tearDown(self):
        pass

    def test_home_page_returns_correct_html(self):
        self.app.get('/')
        self.assertTemplateUsed(response, 'home.html')


if __name__=="__main__":
    unittest.main()
