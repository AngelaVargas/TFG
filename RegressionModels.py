#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 16:23:01 2017

@author: angela
"""


from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matriz import get_data
from sklearn import preprocessing
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
import numpy as np

X, y = get_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = preprocessing.StandardScaler().fit(X_train)
X_test_scaled = scaler.transform(X_test)

"""
Linear Regression Model
"""

# Create linear regression model
my_lr = linear_model.LinearRegression()
my_lr.fit(X_test_scaled,y_test)
y_pred = my_lr.predict(X_test_scaled)

#select the metric
r2_lr = r2_score(y_test,y_pred)
print "R2 linear regression model:", r2_lr
mse_lr = mean_squared_error(y_test, y_pred)
print "MSE linear regression model:", mse_lr

"""
SVR Model
"""

tuned_parameters = {'gamma': np.logspace(-4,1,25),'C': np.logspace(1,4,25)}
svr = SVR(kernel = 'rbf')
grid = GridSearchCV(svr, param_grid=tuned_parameters, cv=5 ,n_jobs = -1) #10-fold cross-validatio
grid.fit(X_test_scaled, y_test)
svr_my_model = grid.best_estimator_

#the result contains the cross-validation results and the best
y_pred_svr = svr_my_model.predict(X_test_scaled)

r2_svr = r2_score(y_test,y_pred_svr)
print "R2 SVR model:", r2_svr
mse_svr = mean_squared_error(y_test, y_pred)
print "MSE SVR model:", mse_svr