from driver import Webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest,time
from base import Login_page
from baselogging import *
from selenium.webdriver.common import desired_capabilities
from ServerManager import server_manager

"""
==============================================================================================================================
 This is the main test case script. All test cases are added as test cases in unittest and executed accordingly 
==============================================================================================================================
"""

#Unittest code 
class testing_first_code(unittest.TestCase):
    def setUp (self):
        self.selenium_server = server_manager()
        self.selenium_server.start_server()
        #enter the name of the browser that you need to test here supported chrome/firefox
        self.driver = Webdriver(browser = 'chrome')
        log.info("setup done" )
        self.monash_career = Login_page(self.driver).open()
        
        #self.current_setUp_name =  setUp.__name__

    def tearDown (self):
        self.driver.close()
        self.driver.quit()
        log.info("tear down done, closed driver")
    
    #Test case for logging in and sending mail    
    def test_enter_login_cred(self):
        log.info("starting first test--> opening url")
        self.monash_career.login()
        self.monash_career.get_jobs(["Casual/ Part-time Employment", "Graduate Employment/ Final Year Recruiting" , "Graduate Recruitment Programme",
                                     "Professional Employment/ Experienced Graduate", "Vacation Employment", "Internship/ Industry Based Learning/ Scholarship",
                                     "Jobs on campus", "Independent contractor", "Vacation Employment Programme"])
        
        
        
if __name__ == "__main__":
    try:
        unittest.main()
    except Exception as e:
        log.info("error occured",e)
    