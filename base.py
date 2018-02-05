from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from page import page
from timecheck import Find_Time
import timecheck
import time
import Readconfig_file
from baselogging import *
from selenium.webdriver.remote.webelement import WebElement
from symbol import argument
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Parser import parser


"""
==============================================================================================================================
 This is the base page on which testing is done. All the base pages are meant to be inherited from 'page.py' which contains all 
 methods common for all modules
==============================================================================================================================

"""
page_url = "https://careergateway.monash.edu.au/students/login?ReturnUrl=%2f"


"""This part reads the configuration file and sets this values into the corresponding dictionary. Range and indexes are depended 
on the number of sections that are to be imported """

locators = {}
Credentials = {}
Email_data = {}
# creates a dictionary of dictionary
dic = [ {} for _ in range(3)]

#Populates the dictionary using the read values from config file
for i in range(3):
    dic[i] = Readconfig_file.get_values_from_configfile(i)
locators = dic[0]
Credentials = dic[1]
Email_data = dic[2]
log.info("created all dictionaries for locators, credentials and emails")

    

#base page on which testing is done
#For the time being all execution are put inside search mail. This will be modified in later commits
class Login_page(page):
                
    def open(self):
        self.driver.get(page_url)
        log.info("opening page " + str(page_url))
        if self.wait_for_element (locators['current_student']):
            return self
        else :
            log.exception ("test failed")
    
    def login(self):
        self.click_button(locators['current_student'])
        self.enter_text(locators['login_email'],Credentials['login'])
        self.enter_text(locators['login_password'],Credentials['password'])
        self.driver.find_element_by_locator(locators['sign_in']).submit()
        self.wait_for_element(locators['image'])
        log.info("login completed")
        
        
    def get_vacation_programme(self):
        self.wait_for_element(locators['job_option'])
        select = Select(self.find_element_by_locator(locators['job_option']))
        select.select_by_visible_text("Vacation Employment Programme")
        self.find_element_by_locator(locators['image']).send_keys(Keys.ENTER)
        self.wait_for_element(locators['caret'])
        time.sleep(10)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_button(locators['caret'])
        self.wait_for_element(locators['list_all'])
        self.click_button(locators['list_all'])
        log.info("listed the vacation programme")
        
    def get_jobs(self,job_type):
        for item in job_type:
            self.scroll_to_top()
            self.wait_for_element(locators['job_option'])
            select = Select(self.find_element_by_locator(locators['job_option']))
            select.select_by_visible_text(item)
            try:
                self.find_element_by_locator(locators['image']).send_keys(Keys.ENTER)
            except:
                self.find_element_by_locator(locators['image1']).send_keys(Keys.ENTER)
            try:
                self.wait_for_element(locators['caret'])
                self.scroll_to_bottom()
                self.click_button(locators['caret'])
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Used a loop to list all items of the job listing
                for i in range(1,1000):
                    try:
                        self.wait_for_element("xpath=//*[@id=\"ng-app\"]/div[2]/div/div[3]/div[1]/div[2]/div/div/ul/li["+str(i)+"]/a")
                    except:
                        i=i-1
                        log.info("Not Found_element_SHOW_ALL"+ str(i))
                        self.scroll_to_bottom()
                        self.click_button("xpath=//*[@id=\"ng-app\"]/div[2]/div/div[3]/div[1]/div[2]/div/div/ul/li["+(str(i))+"]/a")
                        break
            except:
                log.info("no caret element for " + str(job_type))
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.scroll_to_bottom()
            self.wait_for_element(locators['job_option'])
            html = self.driver.page_source.encode("utf-8")
            page_parser = parser(html)
            page_parser.scrape_jobs(item)
        
    
     
        
  
        
            
                                                       
        
        
   
            
            
            
        
        
