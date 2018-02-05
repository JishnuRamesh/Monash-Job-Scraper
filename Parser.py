from baselogging import *
from bs4 import BeautifulSoup
from DatabaseInteraction import databaseInteraction
import re 


class parser():
    
    def __init__(self,html):
        self.soup = BeautifulSoup(html,'lxml',from_encoding="utf-8")
        log.info("initialized parser")
        self.database_manager = databaseInteraction()
        
        
    def scrape_jobs(self,text):
        log.info("scraping for new + str(text) + jobs")
        job_class_list = self.soup.find_all('div', class_='list-group-item')
        job_location_list = self.soup.find_all('div',class_='job-list-location')
        job_date_list = self.soup.find_all('div',class_='job-list-close')
        job_summary_list = self.soup.find_all('p',class_='job-list-summary') 
        job_link_list = self.soup.find_all()
        new_jobs = []
        job_detail = [0]*6
        i = -1
        for job in job_class_list:
            i+=1
            job_string = job.div.div.h4.text
            if "(new)" in job_string:
                job_detail[0] = job.div.div.h4.a.text.strip()
                #print(job_detail[0])
                job_detail[1]  = job.div.div.h5.text.strip()
                #print(job_detail[1])
                location  = job_location_list[i]
                job_detail[2] = location.div.text.strip()
                #print(job_detail[2])
                date  = job_date_list[i]
                job_detail[3] = date.text.strip()
                #print(job_detail[3])
                summary = job_summary_list[i]
                job_detail[4] = summary.text.strip()
                #print(job_detail[4])
                job_detail[5] = job.div.div.h4.a
                job_detail[5] = str(job_detail[5]).split('\\n')[0]
                job_link = job_detail[5].split('=')
                #print(job_link)
                #job_detail[5] = re.sub('[<>]',"",job_detail[5])
                job_link[1] = job_link[1].split(('"'))[1]
                job_detail[5] = job_link[0] + '="https://careergateway.monash.edu.au' + job_link[1]+'"'
                #print(job_detail[5])
                job_detail = self.remove_characters(job_detail)
        
                job = { 'job_name': job_detail[0] , 
                       'job_org' : job_detail[1],
                       'job_location' : job_detail[2],
                       'closing_date' : job_detail[3],
                       'job_summary':  job_detail[4],
                       'job_link' : job_detail[5]}
                
                new_jobs.append(job)
                
    
    
        if text == "Casual/ Part-time Employment":
            self.database_manager.add_rows_casual(new_jobs)
        elif text == "Graduate Employment/ Final Year Recruiting":
            self.database_manager.add_rows_fy_recruitment(new_jobs)
        elif text == "Graduate Recruitment Programme":
            self.database_manager.add_rows_graduate_recruitment(new_jobs)
        elif text == "Professional Employment/ Experienced Graduate":
            self.database_manager.add_rows_professional(new_jobs)
        elif text == "Vacation Employment":
            self.database_manager.add_rows_vacation(new_jobs)
        elif text == "Internship/ Industry Based Learning/ Scholarship":
            self.database_manager.add_rows_intern(new_jobs)
        elif text == "Jobs on campus":
            self.database_manager.add_rows_on_campus(new_jobs)
        elif text == "Independent contractor":
            self.database_manager.add_rows_independent(new_jobs)
        elif text == "Vacation Employment Programme":
            self.database_manager.add_rows_vacation_employment(new_jobs)
        else:
            log.info("no specific job set found... something is wrong")
        
        
        
    def remove_characters(self,job_list):
        new_job_list = []
        for item in job_list:
            new_item= re.sub(r'[\\][nt]',"",item)
            final_text=re.sub(r'[\s]{2,}',"",new_item)
            log.info("removed all unwated characters " + str(final_text))
            new_job_list.append(final_text)
        return (new_job_list)
            
        
                
                
            
            
            
def main():
    file = open('casual.html',"r")
    page_parser = parser(file)
    page_parser.scrape_jobs('casual')
        
        
        
if __name__ == "__main__":
    main()

        
    