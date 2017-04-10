import time
from datetime import date, timedelta
from baselogging import *

"""
==============================================================================================================================
 This is module produces output as <yesterday's date> .. <todays's date> which is used for searching and filtering the mails
 received from yesterday through today
=============================================================================================================================
"""""
#not used in the current example. Used to get out the specific time for filtering emails. 
class Find_Time():
    def Get_Search_Days(self):
        Current_Day = time.strftime("%B %d")
        Yesterday = date.today()-timedelta(1)
        #print Current_Day
        Yester_Day = Yesterday.strftime("%B %d")
        #print Yester_Day
        search_input = str(Yester_Day)+ " .. " + str(Current_Day)
        log.info("returning the search to be inputted as " + str(search_input))
        return search_input