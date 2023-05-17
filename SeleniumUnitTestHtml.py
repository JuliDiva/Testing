import time
import unittest

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
       cls.driver = webdriver.Chrome("/Users/Juli Diva/PycharmProjects/Testing/drivers/chromedriver")
       cls.driver.implicitly_wait(10)
       cls.driver.maximize_window()

   def test_search(self):
       self.driver.set_page_load_timeout(10)
       self.driver.get("https://www.google.com/")
       self.driver.find_element(By.NAME, "q").send_keys("Automation step by step")
       self.driver.find_element(By.NAME, "btnK").click()
       x = self.driver.title
       print(x)
       self.assertEqual(x, "Automation step by step - Google Search")

   @classmethod
   def tearDownClass(cls):
       cls.driver.close()
       cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                  '/Users/Juli Diva/PycharmProjects/Testing/html_reports'))

#run your test file from Terminal like:python3 SeleniumUnitTestHtml.py or py3 SeleniumUnitTestHtml.py


