from backports import configparser
import logging
from baselogging import *

"""
==============================================================================================================================
 This file reads the concerned config file and inputs it into a dictionary which is then returned to base page
==============================================================================================================================



#setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('Selenium.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
""""" 

def get_values_from_configfile(index):
    cfg = configparser.ConfigParser()
    cfg.read('config_file.ini')
    log.info("Reading configuration file into configparser")

    dic = {}
    sec = cfg.sections()

    for items in cfg[sec[index]]:
        key = items
        log.info("imported  key  " + str(key) + "  to dictionary")
        value = cfg[sec[index]][items]
        value = value.split("'")[1]
        log.info("imported value  " + str(value) + "  to dictionary")
        dic[key] = value
    log.info ("returning the created dictionary of config file values to base file")
    return dic
