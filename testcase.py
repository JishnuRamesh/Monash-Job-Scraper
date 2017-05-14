from driver import Webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest,time
from base import Login_page
from baselogging import *
from selenium.webdriver.common import desired_capabilities

"""
==============================================================================================================================
 This is the main test case script. All test cases are added as test cases in unittest and executed accordingly 
==============================================================================================================================
"""

#Unittest code 
class testing_first_code(unittest.TestCase):
    def setUp (self):
        #enter the name of the browser that you need to test here supported chrome/firefox
        self.driver = Webdriver(browser = '')
        log.info("setup done" )
        #self.current_setUp_name =  setUp.__name__

    def tearDown (self):
        self.driver.close()
        self.driver.quit()
        log.info("tear down done, closed driver")
    
    #Test case for logging in and sending mail    
    def test_enter_login_cred(self):
        log.info("starting first test--> opening url")
        gmail = Login_page(self.driver).open()
        gmail.login()
        gmail.send_mail()
        
        
if __name__ == "__main__":
    unittest.main()
    