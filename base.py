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
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

page_url = "https://www.gmail.com"


"""This part reads the configuration file and sets this values into the corresponding dictionary. Range and indexes are depended 
on the number of sections that are to be imported """

locators = {}
Credentials = {}
Email_data = {}
dic = [ {} for _ in range(3)]

for i in range(3):
    dic[i] = Readconfig_file.get_values_from_configfile(i)
locators = dic[0]
Credentials = dic[1]
Email_data = dic[2]
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
        logger.info("need to search for " + locators['compose'])
        self.wait_for_element(locators['compose'])
        logger.info("Logged into gmail")
        
        
    def send_mail(self):
        self.click_button(locators['compose'])
        self.enter_text(locators['to'],Email_data['to_mail'])
        self.enter_text(locators['subject'],Email_data['subject'])
        #self.click_button(locators['body'])
        #self.enter_text(locators['body'],Email_data['body'])
        element = self.find_element_by_locator(locators['body'])
        self.driver.execute_script("arguments[0].innerHTML = arguments[1];", element, "testing");
        self.click_button(locators['send'])
        logger.info("send mail")
        
   
            
            
            
        
        
