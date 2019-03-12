from selenium import webdriver 
import unittest

class NewVisitorTest(unittest.TestCase): 
    def setUp(self):
        self.browser = webdriver.Chrome() 
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
            # She is invited to enter a to-do item straight away

if __name__ == '__main__':
    unittest.main(warnings='ignore')