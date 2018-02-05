import time
from selenium.common.exceptions import NoAlertPresentException 
from Exceptions import NoElementAvailableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from baselogging import *
from time import sleep

"""
==============================================================================================================================
 This is the basic page which contains common modules for all pages. base page inherets from this page
==============================================================================================================================

"""""

class page (object):
    timeout_seconds = 20
    
    def __init__(self,driver):
        self.driver = driver
        log.info("driver intialized")
        
    def find_element_by_locator(self,locator):
        return self.driver.find_element_by_locator(locator)
    
    def find_elements_by_locator(self,locator):
        return self.driver.find_elements_by_locator(locator)
    
    def enter_text(self,locator,text):
        element = self.driver.find_element_by_locator(locator)
        element.send_keys(text)
        
    def click_button(self,locator):
        if self.wait_for_element(locator):
            self.find_element_by_locator(locator).click()
        
    def Send_Enter(self,locator):
        self.find_element_by_locator(locator).send_keys(Keys.ENTER)
        
    #wait for element waits until the element is present on the screen or till time out is reached    
    def wait_for_element(self,locator):
        for i in range (self.timeout_seconds):
            log.info("inside the for loop for wait method in page module")
            if self.driver.is_element_present(locator):
                break
            time.sleep(.5)
        else:
               raise  NoElementAvailableException () 
               log.exception("Wait for element " + str(locator)+" timed out")
               return False 
        return True
    
    #wait for element waits until the element for mail is present on the screen or till time out is reached  
    def wait_for_mail(self,locator):
        log.info("executing to find if mail is available")
        for i in range (self.timeout_seconds):
            if self.driver.is_element_available(locator):
                log.info("mail is found")
                break
            log.info("sleeping to find the mail identified by locator =  " + str(locator))
            time.sleep(.5)
        else:
               raise  NoElementAvailableException () 
               log.exception("NO Build Today... Exiting")
               return False
        return True
    
    #wait for the hidden element to be present on the screen    
    def wait_for_hidden(self,locator):
        for i in range (self.timeout_seconds):
            if self.driver.is_element_present(locator):
                log.info("sleeping to find the element identified by locator = " + str(locator))
                time.sleep(.5)
            else:
                break
            
        else :
            raise NoElementAvailableException ()
            log.exception("Wait for the hidden element timed out")
        return True
    
    def Accept_alert(self):
        for i in range (self.timeout_seconds):
            log.debug("before_try_")
            try:
                log.debug("Inside try wait alert")
                jalert = self.driver.switch_to.alert
                log.info("switched to alert")
                jalert.accept()
                log.info("alert accepted")
                return 
            except NoAlertPresentException as nape:
                log.warning("alert not seen , sleeping till alert is shown")
            time.sleep(.5)
        else:
            log.debug("inside else")
            raise NoAlertPresentException ()
        log.exception("no alert observed , returing")
        return True
    
    #used to navigate from the current window to newly created window.Not used in this example
    def switch_to_desired_window(self):
        window_handle_names = self.driver.window_handles
        if len(window_handle_names) == 1 :
            return
        else:
            self.driver.switch_to_window(window_handle_names[1])
            self.driver.current_window_handle
            return
        
    #Once mail is sent the new pop up window closes, this part confirms the closure of the window.Not used in this example
    def confirm_mail_sent(self):
        window_handles_names = []
        for i in range(self.timeout_seconds):
            window_handles_names[:] = []
            window_handles_names = self.driver.window_handles
            if len(window_handles_names) == 1:
                self.driver.switch_to_window(window_handles_names[0])
                log.info("mail sent confirmed")
                return 
            else:
                log.info("waiting for mail to be sent")
                time.sleep(.5)
                
    def maximize_browser_window(self):
        self.driver.maximize_window()
        
    def click_subelement(self,locator_value_0,locator_value_1):
        element_to_find_0 = self.find_element_by_locator(locator_value_0)
        element_to_find_1 = self.find_element_by_locator(locator_value_1)
        if self.driver.is_element_available(locator_value_1):
            ActionChains(self.driver).move_by_offset(958, 317).click_and_hold(element_to_find_1).perform()
            sleep(1)
            ActionChains(self.driver).release(element_to_find_1)
        #ActionChains(self.driver).move_to_element(element_to_find_0).move_to_element(element_to_find_1).click(element_to_find_1).perform()
            ActionChains(self.driver).move_to_element(element_to_find_1).send_keys(Keys.SPACE)
        else:
            print('issue found')
            
            
    def select_list_element(self,list_header,list_selection):
        list_header_element = self.driver.find_element_by_locator(list_header)
        ActionChains(self.driver).move_to_element(list_header_element)
        list_selection_elements = list_header_element.find_elements_by_tag_name("li")    
        for items in list_selection_elements:
            print(str(items))
            
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        log.info("scrolled page to bottom")
        
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        log.info("scrolled to the top page")
            
                