import unittest
from flask import Flask
from flask_testing import TestCase
from bethesda import app

class BethesdaTestCase(TestCase):

    def create_app(self):
        return app


    def test_home_page_returns_correct_html(self):
        self.client.get('/')
        self.assert_template_used('home.html')

    def test_info_page_returns_correct_html(self):
        self.client.get('/info')
        self.assert_template_used('info.html')


if __name__=="__main__":
    unittest.main()
