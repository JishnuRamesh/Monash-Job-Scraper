from driver import Webdriver
import unittest,time,logging
from base import Login_page

"""
==============================================================================================================================
 This is the main test case script. All test cases are added as test cases in unittest and executed accordingly 
==============================================================================================================================

"""""

#Setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

desired_capabilities = { 'browserName' : 'chrome' }
command_executor = "http://127.0.0.1:4444/wd/hub"



#Unittest code 
class testing_first_code(unittest.TestCase):
    def setUp (self):
        self.driver = Webdriver(desired_capabilities=desired_capabilities, command_executor=command_executor)
        logger.info("setup done" )
        #self.current_setUp_name =  setUp.__name__

    def tearDown (self):
        self.driver.close()
        self.driver.quit()
        logger.info("tear down done, closed driver")
    
    #Test case for logging in and sending mail    
    def test_enter_login_cred(self):
        logger.info("starting first test--> opening url")
        gmail = Login_page(self.driver).open()
        gmail.login()
        """login.enter_login_data()
        login.press_login_button()
        login.search_mail()
        logger.info("Finishing test")"""
        
if __name__ == "__main__":
    unittest.main()
    