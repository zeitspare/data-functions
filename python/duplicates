#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:29:17 2022

@author: Sureshkumar Ramachandran
@Type: DATA CLEANSING
@Function: 
0. duplicate_all --> show all other duplicate values (Whole Data Frame)
1. duplicate ---> default - leave the first value and show all other duplicate values (Whole Data Frame)
2. duplicate_last ---> leave the last value and show all other duplicate values (Whole Data Frame)
3. duplicate_column ---> leave the last value and show all other duplicate values (based on column in Data Frame)
4. duplicate_columns ---> leave the last value and show all other duplicate values (based on Multiple column in Data Frame)
6. remove_duplicates ---> remove all the duplicates in the wholedataframe
7. remove_duplicates_max  ---> remove all the duplicates in the wholedataframe leaving max values
"""


import pandas as pd

data = [["james smith","james","","smith",30,"M",60000], 
        ["michael ","michael","rose","",50,"M",70000], 
        ["robert williams","robert","","williams",42,"",400000], 
        ["robert williams","robert","","williams",42,"",500000], 
        ["maria jones","maria","Anne","jones",38,"F",500000],
        ["maria jones","maria","Anne","jones",38,"F",500000],
        ["maria jones","maria","Anne","jones",38,"F",600000],
        ["jen brown","jen","Mary","brown",45,None,0]] 
columns=["Name",'First Name','Middle Name','Last Name','Age','Gender','Salary']

df = pd.DataFrame(data=data,columns=columns)

def duplicate_all(df):
    duplicate = df[df.duplicated(keep=False)]
    return duplicate

def duplicate(df):
    duplicate = df[df.duplicated()]
    return duplicate

def duplicate_last(df):
    duplicate = df[df.duplicated(keep = 'last')]
    return duplicate

def duplicate_column(df):
    duplicate = df[df.duplicated('Name', keep = 'last')]
    return duplicate

def duplicate_columns(df):
    duplicate = df[df.duplicated(['Name', 'First Name'], keep = 'last')]
    return duplicate

def remove_duplicates(df):
    length1 = len(df)
    print(length1)
    duplicate = df.drop_duplicates()
    length2 = len(duplicate)
    print(length2)
    return duplicate

def remove_duplicates_max(df):
    length1 = len(df)
    print(length1)
    duplicate = df.groupby('Name').apply(lambda x: x.loc[x.Salary.idxmax()])
    length2 = len(duplicate)
    print(length2)
    return duplicate



if __name__ == "__main__":
    duplicate_all_df = duplicate_all(df)
    duplicate_df = duplicate(df)
    duplicate_last_df = duplicate_last(df)
    duplicate_column_df = duplicate_column(df)
    duplicate_columns_df = duplicate_columns(df)
    remove_duplicates_df = remove_duplicates(df)
    remove_duplicates_max_df = remove_duplicates_max(df) 
