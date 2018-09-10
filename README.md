
# DEPRECATED

Since Monash moved into OKTA login provider this service no longer works. Hence been deprecated





# Monash Job Scraper
This script runs through the Monash career gateway website and scrapes the job information. These data are then saved into a sqlite3 database. When a new job listing is encountered an email is send out to the concerened user.

How to run the script

## STEP 1

Download following dependencies and softwares
Selenium Standalone Server 3.4.0
Python 3.6
Python-Selenium 3.4
Beautiful Soup 4
lxml
backports
Configparser

## STEP 2

Update the location of the downloaded selenium standalone server 3.4.0 in the script ServerManager.py on line 12

## STEP 3

Update the location of the downloaded script in the DabatbaseInteraction.py on line 10

## STEP 4

Run DatabaseSetup.py first. This sets up the database for the script

## STEP 5

Update the from and to email address in the script EmailSender.py from lines 10 to 12

## STEP 6

Run testcase,py to run the script to scrape for new jobs.
