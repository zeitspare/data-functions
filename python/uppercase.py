#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:29:17 2022

@author: Sureshkumar Ramachandran
@Type: DATA PROCESSING
@Function: 
1. convertCase ---> First letter of the column names to be in capital  
2. upperCase ---> Name column to be Full in Capital Letters  
"""


import pandas as pd

data = [["james smith","james","","smith",30,"M",60000], 
        ["michael ","michael","rose","",50,"M",70000], 
        ["robert williams","robert","","williams",42,"",400000], 
        ["maria jones","maria","Anne","jones",38,"F",500000],
        ["maria jones","maria","Anne","jones",38,"F",500000],
        ["jen brown","jen","Mary","brown",45,None,0]] 
columns=["Name",'First Name','Middle Name','Last Name','Age','Gender','Salary']

df = pd.DataFrame(data=data,columns=columns)

#first letter of the column to be in capital letter
def convertCase(Name):
    resStr=""
    arr = Name.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr 

def upperCase(Name):
    return Name.upper() 

if __name__ == "__main__":
    df['CName'] = df['Name'].apply(convertCase)
    df['UName'] = df['Name'].apply(upperCase)
