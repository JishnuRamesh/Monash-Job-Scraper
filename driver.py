from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from Exceptions import NoElementAvailableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webelement import WebElement
import logging

"""
==============================================================================================================================
 Subclassing Webdriver for better implementation. We don't use the the driver methods to find elements directly in any of the 
 page objects , instead uses find_element_by_locator() method
==============================================================================================================================

"""""

#setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



class Webdriver (WebDriver):
    def __init__(self,**kwargs):
        logger.info("webdriver is getting executed")
        super(Webdriver,self).__init__(**kwargs)
    
    def find_element_by_locator(self,locator):
        locator_type,locator_value = locator.split('=',1)
        logger.info("inside locator method in driver")
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
            logger.exception("no element found with the given locator: " + str(locator_value))
        
    
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
            logger.exception("no element found with the given locator: " + str(locator_value))
        
        return [ WebElement(e) for e in elements ]
    
    def is_element_present(self,locator):
        try :
            logger.info("checking whether element " + str(locator) + " is available on screen")
            self.find_element_by_locator(locator)
        except NoSuchElementException:
            logger.warning("No element is present in the screen with the locator " + str(locator))
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
        
   
    