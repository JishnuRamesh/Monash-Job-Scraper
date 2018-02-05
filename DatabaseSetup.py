import sqlite3
from baselogging import *

conn = sqlite3.connect('Database/jobs.db')

c = conn.cursor()

c. execute("""CREATE TABLE casual (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table casual")


c. execute("""CREATE TABLE fy_recruitment (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table FY_recruitment")

c. execute("""CREATE TABLE graduate_recruitment (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table Graduate_Recruitment")


c. execute("""CREATE TABLE professional (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table professional")

c. execute("""CREATE TABLE vacation (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table vacation")



c. execute("""CREATE TABLE intern (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table intern")

c. execute("""CREATE TABLE on_campus (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table on_campus")

c. execute("""CREATE TABLE independent (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table independent")

c. execute("""CREATE TABLE vacation_employment (
           c_jobName text, 
              c_jobOrg  text,
              c_jobSummary text,
              c_jobDate    text,
              c_jobLocation text,
              c_link text,
              PRIMARY KEY(c_jobName,c_jobOrg,c_jobDate))
                """)
log.info("Created table vacation_employment")




conn.commit()

c.close()