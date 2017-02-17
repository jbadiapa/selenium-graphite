import unittest
from selenium import webdriver
# from selenium.webdriver.common.by import By
from time import sleep


class GraphiteSelenium(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.ip = '192.168.33.51'
        self.port = '8080'
        self.url = 'http://{ip}:{port}/'.format(
            ip=self.ip,
            port=self.port
        )

    def _url_load(self, url):
        driver = self.driver
        driver.get(url)
        sleep(2)
        return driver

    def _url_test(self, url, text):
        driver = self._url_load(url)
        assert text in driver.title
        return driver

    def test_graphite(self):
        return self._url_test(self.url, 'Graphite Browser')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
