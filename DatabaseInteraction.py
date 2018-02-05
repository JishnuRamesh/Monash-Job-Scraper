import sqlite3
import sys,os
from baselogging import *
from EmailSender import email_sender


class databaseInteraction():
    
    def __init__(self):
        os.chdir(r'C:\Users\Jishnu\Documents\Coding github clones\Monash_webscraper')
        self.conn = sqlite3.connect('Database/jobs.db')
        self.c     = self.conn.cursor()
        self.emailManager = email_sender()
        
    
    def add_rows_casual(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] + dic_item['job_link'])
                    self.c.execute("INSERT INTO casual VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert casual jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New Casual Jobs')
        else:
            log.info("No new casual jobs")
                    
                    
    def add_rows_fy_recruitment(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO fy_recruitment VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link']})
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert final year recruitment jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New final year recruitment  jobs')
        else:
            log.info("No new final year recruitment jobs")
        
        
    def add_rows_graduate_recruitment(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO graduate_recruitment VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert graduate recruitment jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New graduate recruitment  jobs')
        else:
            log.info("no new graduate recruitement jobs")
        
    def add_rows_professional(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO professional VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert professional jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New professional jobs')
        else:
            log.info("no new professional jobs")
        
    def add_rows_vacation(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO vacation VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert vacation jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New vacation jobs')
        else:
            log.info("No new vacation jobs")
        
    def add_rows_intern(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO intern VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert intern jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New intern jobs')
        else:
            log.info("no new intern jobs")
        
    def add_rows_on_campus(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO on_campus VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert on campus jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New on campus jobs')
        else:
            log.info("no new on campus jobs")
        
    def add_rows_independent(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO independent VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert on independent jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New independent jobs')
        else:
            log.info("no new independent jobs")
        
    def add_rows_vacation_employment(self,job_list):
        email_list = [] 
        for dic_item in job_list:
                try:
                    log.info(dic_item['job_name']+ dic_item['job_org']+ 
                                    dic_item['job_location']+ dic_item['closing_date']+ 
                                    dic_item['job_summary'] )
                    self.c.execute("INSERT INTO vacation_employment VALUES (:jobName, :jobOrg, :jobLocation, :jobDate, :jobSummary, :jobLink)",
                                   {'jobName': dic_item['job_name'],'jobOrg' : dic_item['job_org'],'jobLocation' : 
                                    dic_item['job_location'],'jobDate' : dic_item['closing_date'], 'jobSummary' : 
                                    dic_item['job_summary'], 'jobLink' : dic_item['job_link'] })
                    self.conn.commit()
                    email_list.append(dic_item)
                    
                except:
                    log.info(sys.exc_info())
                    log.info("already in db")
        log.info("done with db insert on vacation_employment jobs ")
        self.conn.close()
        if len(email_list) != 0:
            self.emailManager.send_email(email_list,'New vacation_employment jobs')
        else:
            log.info("no new vaction employment")
        
        
                    
def main():
    db = databaseInteraction()
    list_a = [{"job_org" : "Kaiser Trading Group",
"job_summary" : "We are looking for an enthusiastic and intellectually curious intern to support senior development staff on a casual basis for a minimum of six months",
"job_location" : "Melbourne",
"closing_date" : "Closes - 2 Jan, 2018",
"job_name" : "Hedge Fund Intern ֠Junior Developer" } ]
    db.add_rows_casual(list_a)
    
if __name__ == "__main__":
    main()
    
            