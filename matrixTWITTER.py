#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:29:08 2017

@author: angela
"""

import numpy
import csv

def get_data_twitter():
    
    f = open('films_TWITTER.csv')
    lines_twitter = csv.reader(f, delimiter=',')

    matrix = numpy.zeros((298,10))
    y = numpy.zeros((298,1))
    i = 0
    
    for line_twitter in lines_twitter:
        film_twitter = line_twitter[0].split("'")[1]
        total_tweets = line_twitter[1]
        total_retweets = line_twitter[2]
        total_favorites = line_twitter[3]
        
        f = open('films_IMDB.csv')
        lines_IMDB = csv.reader(f, delimiter=',')
    
        for line_IMDB in lines_IMDB:
            film_IMDB = line_IMDB[0].split("'")[1]
            rating = line_IMDB[1]
            votes = line_IMDB[2]
            
            if film_twitter == film_IMDB:
                f = open('films2.csv')
                lines_total = csv.reader(f, delimiter=',')
            
                for line in lines_total:
                    film_id = line[0].split("'")[3]
                    data_1 = line[1]
                    data_2 = line[2]
                    
                    if film_id == film_IMDB:
                        rank_1 = data_1.split(" ")[5]
                        euros_1 = data_1.split(" ")[7]
                        cinemas_1 = data_1.split(" ")[9]
                        screens_1 = data_1.split(" ")[10]
                        spect_1 = data_1.split(" ")[11]
                            
                        euros_acum = data_2.split(" ")[7]
                        
                        matrix[i][0] = rank_1
                        matrix[i][1] = euros_1
                        matrix[i][2] = cinemas_1
                        matrix[i][3] = screens_1
                        matrix[i][4] = spect_1
                        matrix[i][5] = rating
                        matrix[i][6] = votes
                        matrix[i][7] = total_tweets
                        matrix[i][8] = total_retweets
                        matrix[i][9] = total_favorites
                        y[i][0] = euros_acum
                                   
                        i = i + 1
                        
    return matrix,y