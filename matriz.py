#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:11:52 2017

@author: angela
"""

import numpy
import csv

def get_data():
    matrix = numpy.zeros((1527,5))
    y = numpy.zeros((1527,1))
        
    f = open('films2.csv')
    lines = csv.reader(f, delimiter=',')
        
    First_line = True
    i = 0
    for line in lines:
        if First_line == False:
                try:
                    data_1 = line[1]
                    
                    rank_1 = data_1.split(" ")[5]
                    euros_1 = data_1.split(" ")[7]
                    cinemas_1 = data_1.split(" ")[9]
                    screens_1 = data_1.split(" ")[10]
                    spect_1 = data_1.split(" ")[11]
                    
                    data_2 = line[2]
                    
                    euros_acum = data_2.split(" ")[7]              
                    
                    
                    matrix[i][0] = rank_1
                    matrix[i][1] = euros_1
                    matrix[i][2] = cinemas_1
                    matrix[i][3] = screens_1
                    matrix[i][4] = spect_1
                    y[i][0] = euros_acum
                          
                    i = i + 1
    
                except:
                    continue
        else:
            First_line = False

    return matrix,y
