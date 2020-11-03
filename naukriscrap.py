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

driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
jobs={"roles":[],
     "companies":[],
     "locations":[],
     "experience":[],
     "skills":[],
     "Dates":[],
     "PresentDate":[],
     "salary":[],}

MAX_PAGE_NUM = 500
MAX_PAGE_DIG = 3
driver=webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

for i in range(1, MAX_PAGE_NUM+1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url="https://www.naukri.com/data-scientist-jobs-"+page_num+"?k=data%20scientist"
    driver.get(url)
    time.sleep(3)
    lst=driver.find_elements_by_css_selector(".jobTuple.bgWhite.br4.mb-8")
    
    for job in lst:
        driver.implicitly_wait(10)
        try:
            role=job.find_element_by_css_selector("a.title.fw500.ellipsis").text
            company=job.find_element_by_css_selector("a.subTitle.ellipsis.fleft").text
            location=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.location").text
            salaries=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.salary").text
            exp=job.find_element_by_css_selector(".fleft.grey-text.br2.placeHolderLi.experience").text
            date=job.find_element_by_css_selector(".type.br2.fleft.grey").text
            skills=job.find_element_by_css_selector(".tags.has-description").text 
        except NoSuchElementException:
             pass
        today=datetime.datetime.today().strftime('%Y-%m-%d')
        jobs["roles"].append(role)
        jobs["companies"].append(company)
        jobs["locations"].append(location)
        jobs["experience"].append(exp)
        jobs["salary"].append(salaries)
        jobs["Dates"].append(date)
        jobs["PresentDate"].append(today)
        jobs["skills"].append(skills)
                    
        
df=pd.DataFrame.from_dict(jobs)
