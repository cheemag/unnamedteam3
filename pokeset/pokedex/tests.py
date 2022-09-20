from django.test import TestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class AccessViewTestCase(TestCase):
    """
    Set of test cases that test access to the webpages of the website
    """

    def test_login_access(self):
        response = self.client.get('/pokedex/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_access(self):
        response = self.client.get('/pokedex/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_without_login_path_access(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class AccessViewTestCaseWithSelenium(StaticLiveServerTestCase):
    """
    Set of test cases that test access to the webpages from other
    webpages using Selenium
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.selenium.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        return super().tearDownClass()

    def test_register_access_from_login_page(self):
        url = self.live_server_url
        self.selenium.get(url + '/pokedex/login')
        self.selenium.find_element(By.CLASS_NAME, 'link_button').click()
        self.assertEqual(self.selenium.current_url, url + '/pokedex/register/')


class CorrectTemplateTestCase(TestCase):
    """
    Set of test cases that test if the right template was used
    """

    def test_login_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')

    def test_register_template(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'register.html')

    def test_login_without_login_path_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'login.html')

