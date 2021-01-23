# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 04:49:04 2021

@author: U6067583
"""


import numpy as np
import pandas as pd
#from flask import Flask, render_template, request
# libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from IPython.display import HTML 

def create_sim():
    data = pd.read_csv("C:\\Users\\u6067583\\Downloads\\Project2\\Recom1.csv")
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['text'])
    # creating a similarity score matrix
    sim = cosine_similarity(count_matrix)
    return data,sim

def rcmd(m):
    #m = m.lower()
    # check if data and sim are already assigned
    try:
        data.head()
        sim.shape
    except:
        data, sim = create_sim()
    # check if the role is in our database or not
    if m not in data['Job_Roles'].unique():
        return('This job_roles is not in our database.\nPlease check if you spelled it correct.')
    else:
        # getting the index of the role in the dataframe
        i = data.loc[data['Job_Roles']==m].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- role scores
        # not taking the first index since it is the same role
        lst = lst[1:11]

        # making an empty list that will containg all 10 role recommendations
        l = []
        L=[]
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['skills'][a])
            L.append(data['Job_Roles'][a])
            jobs={'Roles':L,'TEXT':l}
            recommendation = pd.DataFrame(jobs)
            result = recommendation.to_html()
            
            html = recommendation.to_html()
            # write html to file 
            text_file = open("index.html", "w") 
            text_file.write(html) 
            text_file.close() 
            table=HTML(recommendation.to_html(classes='table table-striped'))
  

        return table

rcmd('Machine Learning Engineer')
result = recommendation.to_html() 
print(result)

data = pd.read_csv("C:\\Users\\u6067583\\Downloads\\Project2\\Recom1.csv")
data