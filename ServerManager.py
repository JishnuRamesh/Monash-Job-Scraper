import subprocess
import os
import time
import sys
from baselogging import *


class server_manager():
    
    def start_server(self):
        try:
            os.chdir('C:\AutomationSetup\Selenium')
            proc = subprocess.Popen("java -jar selenium-server-standalone-3.8.0.jar",shell=True)
            print("check")
            time.sleep(20)
            proc.terminate()
            log.info("server initiliazed")
        except Exception as e:
            log.info(sys.exc_info())
            log.info("exception occured", e)
        


if __name__ == "__main__":
    selenium_server = server_manager()
    selenium_server.start_server()
