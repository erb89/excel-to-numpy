#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 20:17:54 2017

@author: emilyburnside
"""
#organise your values in spreadsheet columns, save as csv, then...
import numpy as np



import csv

with open('yourfile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    a = []
    b = []
    for row in readCSV:  
        a.append(float(row [0])) #where row 0 is excel column A
        b.append(float(row [1])) #where row 1 is excel column B etc

print (a, b)