#!/usr/bin/env python2
"""
Created on Mon Jun 19 09:05:22 2017

@author: angela
"""

import numpy
import csv


def get_data():
    
    f = open('films_IMDB.csv')
    lines_IMDB = csv.reader(f, delimiter=',')

    matrix = numpy.zeros((620,7))
    i = 0
    
    for line_IMDB in lines_IMDB:
        film_IMDB = line_IMDB[0].split("'")[1]
        rating = line_IMDB[1]
        votes = line_IMDB[2]
        
        f = open('films2.csv')
        lines_total = csv.reader(f, delimiter=',')
        for line in lines_total:
                film_id = line[0].split("'")[3]
                data_1 = line[1]
                
                if film_id == film_IMDB:
                        
                        rank_1 = data_1.split(" ")[5]
                        euros_1 = data_1.split(" ")[7]
                        cinemas_1 = data_1.split(" ")[9]
                        screens_1 = data_1.split(" ")[10]
                        spect_1 = data_1.split(" ")[11]
                         
                        matrix[i][0] = rank_1
                        matrix[i][1] = euros_1
                        matrix[i][2] = cinemas_1
                        matrix[i][3] = screens_1
                        matrix[i][4] = spect_1
                        matrix[i][5] = rating
                        matrix[i][6] = votes
                              
                        i = i + 1

