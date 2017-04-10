from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from selenium.common.exceptions import NoSuchElementException
from baselogging import *
"""
==============================================================================================================================
 Subclassing Webelement for the better implementation
==============================================================================================================================
"""""

class WebElement(SeleniumWebElement):
	def __init__(self,element):
		super(WebElement,self).__init__(element.parent,element.id)
		
	def find_element_by_locator(self,locator):
		locator_type,locator_value = locator.split('=')
		
		if locator_type == 'class':
			return WebElement(self.find_element_by_class_name(locator_value))
		elif locator_type == 'css':
			return WebElement(self.find_element_by_css_selector(locator_value))
		elif locator_type == 'id':
			return WebElement(self.find_element_by_id(locator_value))
		elif locator_type == 'link':
			return WebElement(self.find_element_by_link_text(locator_value))
		elif locator_type == 'plink':
			return WebElement(self.find_element_by_partial_link_tetx(locator_value))
		elif locator_type == 'tag':
			return WebElement(self.find_element_by_tag_name(locator_value))
		elif locator_type == 'xpath':
			return WebElement(self.find_element_by_xpath(locator_value))
		elif locator_type == ' name':
			return WebElement(self.find_element_by_name(locator_value))
		else:
			raise NoSuchElementException ("Invalid Selector")
			log.exception("wrong locator :" +str(locator_value) + " given and an element couldn't be found with this locator")


	def find_elements_by_locator(self,locator):
		locator_type,locator_value = locator.split('=')
		
		if locator_type == 'class':
			element = self.find_elements_by_class_name(locator_value)
		if locator_type == 'css':
			element = self.find_elements_by_css_selector(locator_value)
		if locator_type == 'name':
			element = self.find_elements_by_name(locator_value)
		if locator_type == 'link':
			element = self.find_elements_by_partial_link(locator_value)
		if locator_type == 'plink':
			element = self.find_elements_by_partial_link(locator_value)
		if locator_type == 'tag':
			element = self.find_elements_by_tag(locator_value)
		if locator_type == 'xpath':
			element = self.find_elements_by_xpath(locator_value)
		if locator_type == 'id':
			element = self.find_elements_by_id(locator_value)
		else:
			raise Exception ("Invalid Selector")
			log.exception("wrong locator:  " + str(locator_value) + " given and an element couldn't be found with this locator")
		
		return [Webelement(e) for e in element]
	
	
			