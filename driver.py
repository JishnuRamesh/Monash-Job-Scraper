from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from Exceptions import NoElementAvailableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webelement import WebElement
from baselogging import *
from selenium.webdriver.common import desired_capabilities

"""
==============================================================================================================================
 Subclassing Webdriver for better implementation. We don't use the the driver methods to find elements directly in any of the 
 page objects , instead uses find_element_by_locator() method
==============================================================================================================================

"""


class Webdriver (WebDriver):
    def __init__(self,browser):
        if browser == 'chrome':
            log.info("Setting capabilities for chrome")
            desired_capabilities = {'browserName' : 'chrome'}
        
        if browser == 'firefox':
            log.info("Setting capabilities for chrome")
            desired_capabilities = {'browserName' : 'firefox' , 'marionette' : True , 'binary' : 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe' , 'profile' : 'C:/Users/Jishnu/AppData/Local/Mozilla/Firefox/Profiles/oio7zluy.Automation'}
            
        command_executor = "http://127.0.0.1:4444/wd/hub"    
        log.info("webdriver is getting executed")
        super(Webdriver,self).__init__(command_executor,desired_capabilities )
    
    def find_element_by_locator(self,locator):
        locator_type,locator_value = locator.split('=',1)
        log.info("inside locator method in driver")
        if locator_type == 'class':
            return WebElement(self.find_element_by_class_name(locator_value))
        if locator_type == 'css':
            return WebElement(self.find_element_by_css_selector(locator_value))
        if locator_type == 'id':
            return WebElement (self.find_element_by_id(locator_value))
        if locator_type == 'link':
            return WebElement(self.find_element_by_link_text(locator_value))
        if locator_type == 'plink':
            return WebElement(self.find_element_by_partial_link_text(locator_type))
        if locator_type == 'xpath':
            return WebElement(self.find_element_by_xpath(locator_value))
        if locator_type == 'name':
            return WebElement(self.find_element_by_name(locator_value))
        if locator_type == 'tag':
            return WebElement(self.find_element_by_tag_name(locator_value))
        else :
            raise Exception()
            log.exception("no element found with the given locator: " + str(locator_value))
        
    
    def find_elements_by_locator(self,locator):
        locator_type,locator_value = locator.split('=')
        
        if locator_type == 'class':
            elements = self.find_elements_by_class_name(locator_value)
        if locator_type == 'css':
            elements = self.find_elements_by_css_selector(locator_value)
        if locator_type == 'link':
            elements = self.find_elements_by_link_text(locator_value)
        if locator_type == 'plink':
            elements = self.find_elements_by_partial_link_text(locator_value)
        if locator_type == 'xpath':
            elements = self.find_elements_by_xpath(locator_value)
        if locator_type == 'tag':
            elements = self.find_elements_by_tag_name(locator_value)
        if locator_type == 'id':
            elements = self.find_elements_by_id(locator_value)
        if locator_type == 'name':
            elements = self.find_elements_by_name(locator_value)
        else:
            raise Exception ()
            log.exception("no element found with the given locator: " + str(locator_value))
        
        return [ WebElement(e) for e in elements ]
    
    def is_element_present(self,locator):
        try :
            log.info("checking whether element " + str(locator) + " is available on screen")
            self.find_element_by_locator(locator)
        except NoSuchElementException:
            log.warning("No element is present in the screen with the locator " + str(locator))
            return False
        return True
    def is_element_visible(self,locator):
        if self.find_element_by_locator(locator).is_displayed():
            return True
        else:
            return False
        
    def is_element_available (self,locator):
        if self.is_element_present(locator):
            if self.is_element_visible(locator):
                return True
            
        else:
            return False
        
   
    