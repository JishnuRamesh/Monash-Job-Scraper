from datetime import datetime
import schedule
import unittest

class testing_first_code(unittest.TestCase):
        
    
    #Test case for logging in and sending mail    
    def test_enter_login_cred(self):
        print("test",str(datetime.now()))
        
        
        
if __name__ == "__main__":
    def job():
        try:
            unittest.main()
        except Exception as e:
            log.info("error occured",e)
            
    schedule.every(5).seconds.do(job)
            
    
            