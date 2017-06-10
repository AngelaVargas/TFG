#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 17:11:52 2017

@author: angela

Estructure of the matrix:
    [year month day ]
    ['date_1', 'rank_1', 'first_week','acum_euros_1', 
   'euros_1', 'cines_1', 'screens_1', 'acum_espect_1', 'espect₁']
"""
import numpy
import csv

def get_data():
    matrix = numpy.zeros((1527,8))
    y = numpy.zeros((1527,1))
    
    
    f = open('films2.csv')
    lines = csv.reader(f, delimiter=',')
    
    First_line = True
    i = 0
    for line in lines:
        if First_line == False:
                try:
                    data_1 = line[1]
                    
                    #Date
                    film_date = data_1.split(",")
                    wrong_date = film_date[0] + "("
                    year = wrong_date.split("(")[1]
                    month_space = film_date[1]
                    month = month_space.split(" ")[1]
                    day_space = film_date[2]
                    day = day_space.split(" ")[1]
                    
                    rank_1 = data_1.split(" ")[5]
                    euros_1 = data_1.split(" ")[7]
                    cinemas_1 = data_1.split(" ")[9]
                    screens_1 = data_1.split(" ")[10]
                    spect_1 = data_1.split(" ")[11]
                    
                    data_2 = line[2]
                    
                    rank_2 = data_2.split(" ")[5]
                    weeks = data_2.split(" ")[6]
                    euros_acum = data_2.split(" ")[7]
                    euros_2 = data_2.split(" ")[8]
                    cinemas_2 = data_2.split(" ")[9]
                    screens_2 = data_2.split(" ")[10]
                    spect_acum = data_2.split(" ")[11]
                    spect_2 = data_2.split(" ")[12]
                    spect_2 = spect_2.split("]")[0]
                    
                    
                    matrix[i][0]= year
                    matrix[i][1]= month
                    matrix[i][2] = day
                    matrix[i][3] = rank_1
                    matrix[i][4] = euros_1
                    matrix[i][5] = cinemas_1
                    matrix[i][6] = screens_1
                    matrix[i][7] = spect_1
                    y[i][0] = euros_acum
                          
                    i = i + 1
    
                except:
                    continue
        else:
            First_line = False

    return matrix,y