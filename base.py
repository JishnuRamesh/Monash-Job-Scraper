from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from page import page
from timecheck import Find_Time
import timecheck,logging
import time
from ConfigParser import ConfigParser
import Readconfig_file


"""
==============================================================================================================================
 This is the base page on which testing is done. All the base pages are meant to be inherited from 'page.py' which contains all 
 methods common for all modules
==============================================================================================================================

"""""

#setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

page_url = "https://www.gmail.com"


"""This part reads the configuration file and sets this values into the corresponding dictionary. Range and indexes are depended 
on the number of sections that are to be imported """

locators = {}
Credentials = {}
Emails = {}
dic = [ {} for _ in range(3)]

for i in range(3):
    dic[i] = Readconfig_file.get_values_from_configfile(i)
locators = dic[0]
Credentials = dic[1]
Emails = dic[2]
logger.info("created all dictionaries for locators, credentials and emails")

    

#base page on which testing is done
#For the time being all execution are put inside search mail. This will be modified in later commits
class Login_page(page):
    

        
    def search_mail(self):
        self.Get_Search_Input = Find_Time()
        input_text = self.Get_Search_Input.Get_Search_Days()
        self.enter_text(locators['search'],input_text)
        self.click_button(locators['advanced_search'])
        self.wait_for_element(locators['from_text_box'])
        self.enter_text(locators['from_text_box'],Emails['from_email'])
        self.click_button(locators['search_icon'])
        self.wait_for_element(locators['forward']) # new code instead of sleep (15) 
        self.wait_for_mail(locators['forward'])
        self.click_button(locators['forward'])
        self.switch_to_desired_window()
        self.Accept_alert()
        self.enter_text(locators['receiver'],Emails['to_email'])
        self.click_button(locators['send'])
        self.confirm_mail_sent()
        logger.debug("mail is sent")
        
    
            
    def open(self):
        self.driver.get(page_url)
        logger.info("opening page " + str(page_url))
        self.driver.maximize_window()
        if self.wait_for_element (locators['login_email']):
            return self
        else :
            logger.exception ("test failed")
            exit
    
    def login(self):
        self.enter_text(locators['login_email'],Credentials['login'])
        self.click_button(locators['email_next'])
        self.wait_for_element(locators['login_password'])
        self.enter_text(locators['login_password'],Credentials['password'])
        self.click_button(locators['sign_in'])
        logger.info("Logged into gmail")
        time.sleep(20)
        
   
            
            
            
        
        
