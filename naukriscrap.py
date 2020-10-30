# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:58:51 2020

@author: U6067583
"""


import csv
import time
from selenium import webdriver
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import math
import urllib 
import numpy as np
from urllib.request import Request, urlopen
import requests
from time import sleep
from random import randint
from selenium.common.exceptions import *
import datetime


#driver = "C:\Program Files (x86)\chromedriver.exe"

driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
jobs={"roles":[],
     "companies":[],
     "locations":[],
     "experience":[],
     "skills":[],
     "salary":[],}

    
for i in range(1):
    driver.get("https://www.naukri.com/machine-learning-jobs-{}".format(i))
    time.sleep(3)
    lst=driver.find_elements_by_css_selector(".jobTuple.bgWhite.br4.mb-8")
    
    # scrape the data from website
    for job in lst:
        driver.implicitly_wait(10)
        role=job.find_element_by_css_selector("a.title.fw500.ellipsis").text
        company=job.find_element_by_css_selector("a.subTitle.ellipsis.fleft").text
        location=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.location").text
        salaries=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.salary").text
        exp=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.experience").text
        skills=job.find_element_by_css_selector(".tags.has-description").text
        jobs["roles"].append(role)
        jobs["companies"].append(company)
        jobs["locations"].append(location)
        jobs["experience"].append(exp)
        jobs["salary"].append(salaries)
        jobs["skills"].append(skills)
        
df=pd.DataFrame.from_dict(jobs)
df.head(10)
