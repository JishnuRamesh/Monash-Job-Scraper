import logging,inspect

class BaseLogging ():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s:%(mod_name)s,%(levelname)s:%(message)s')
        self.file_handler = logging.FileHandler('Selenium1.log') 
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        
    def debug(self,msg):
        module_stack = inspect.stack()[1][1]
        mod_name = inspect.getmodulename(module_stack) 
        d = { 'mod_name' : mod_name }
        self.logger.debug(msg, extra = d)
        
    def info(self,msg):
        module_stack = inspect.stack()[1][1]
        mod_name = inspect.getmodulename(module_stack) 
        d = { 'mod_name' : mod_name }
        self.logger.info(msg, extra = d)
        
    def warning(self,msg):
        module_stack = inspect.stack()[1][1]
        mod_name = inspect.getmodulename(module_stack) 
        d = { 'mod_name' : mod_name }
        self.logger.warning(msg, extra = d)
        
    def critical(self,msg):
        module_stack = inspect.stack()[1][1]
        mod_name = inspect.getmodulename(module_stack) 
        d = { 'mod_name' : mod_name }
        self.logger.critical(msg, extra = d)
    
    def exception(self,msg):
        module_stack = inspect.stack()[1][1]
        mod_name = inspect.getmodulename(module_stack) 
        d = { 'mod_name' : mod_name }
        self.logger.exception(msg, extra = d) 
        
class Log_Object():
    log = BaseLogging()
    
        
        
        
        