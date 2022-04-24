#!/usr/bin/env python
# -*- coding: utf-8 -*-
import roslib
import rospy
#import maths
import sys
import cv2
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
import matplotlib.pyplot as plt
import cv_bridge
import time
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
import os
from timeit import timeit
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray,Float64
from std_msgs.msg import MultiArrayDimension
from math import pi
from time import sleep
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from math import e
from datetime import datetime
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score
import statistics
import guardar_info as gdi   
def abs_lista(lista):
    lista_new = []
    for i in lista:
       lista_new.append(abs(i))
    return(lista_new)

def segmentacion(r , dr, alf, dr_pred):  
    r_tot = []
    dr_tot = []
    alf_tot = []
    for i in range(len(r)):
       if dr_pred[i] >= dr[i]:
          r_tot.append(r[i])
          dr_tot.append(dr[i])
          alf_tot.append(alf[i])
    return(r_tot,dr_tot,alf_tot)
    
def segmentacion_xy(r , dr, dr_pred):  
    r_tot = []
    dr_tot = []
    for i in range(len(r)):
       if dr_pred[i] >= dr[i]:
          r_tot.append(r[i])
          dr_tot.append(dr[i])
    return(r_tot,dr_tot)
    
def regresion_lineal(X_train, y_train):
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    y_pred = regr.predict(X_train)  
    return(y_pred,regr.coef_,regr.intercept_)
      
def polinomyc2( X_train, y_train):
    pf = PolynomialFeatures(degree = 2)    # usaremos polinomios de grado 3
    X_trainpol = pf.fit_transform(X_train.reshape(-1,1))  # transformamos la entrada en polinómica 
    regr2 = linear_model.LinearRegression()
    regr2.fit(X_trainpol, y_train)
    return(valores_pol2( X_train, regr2.coef_, regr2.intercept_), regr2.coef_, regr2.intercept_)

def valores_pol2( X_train,w,b):
     y=[]
     for x in X_train:
        val=b+(w[1]*x)+((x**2)*w[2])
        y.append(val)  
     return (y)   
              
def polinomyc3( X_train, y_train):
    pf = PolynomialFeatures(degree = 3)    # usaremos polinomios de grado 3
    X_trainpol = pf.fit_transform(X_train.reshape(-1,1))  # transformamos la entrada en polinómica 
    regr3 = linear_model.LinearRegression()
    regr3.fit(X_trainpol, y_train)
    return(valores_pol3( X_train, regr3.coef_, regr3.intercept_), regr3.coef_, regr3.intercept_)
    
def valores_pol3( X_train,w,b):
     y=[]
     for x in X_train:
        val=b+(w[1]*x)+((x**2)*w[2])+((x**3)*w[3])
        y.append(val)  
     return (y)  
       
def ecuacion_desviacion(A,B,x):#en esta ecuación se obtiene  
    y= (A*x)+B 
    return(y)
    
def graficar1 (r, alf):#en esta funcion se grafican los datos en forma de rectangulos con ancho variable dependiendo de la profundidad donde se encuentre y se retorna la imagen
    #img1 = np.zeros(((yeje),(xeje),3), np.uint8)
    depht = 5
    x_v = []
    y_v = []
    for i in range(len(r)):
        x,y = triangulacion_datos( r[i], alf[i])
        if abs(x)>depht or abs(y)>depht:
           x = 0
           y = 0
        x_v.append(x)
        y_v.append(y)
    return(x_v, y_v)
       
def graficar2 (matriz_rdralfa):#en esta funcion se grafican los datos en forma de rectangulos con ancho variable dependiendo de la profundidad donde se encuentre y se retorna la imagen
    #img1 = np.zeros(((yeje),(xeje),3), np.uint8)
    depht = 5
    x_vo = []
    y_vo = []
    for i in range(len(matriz_rdralfa)):
        xo,yo = triangulacion_datos( matriz_rdralfa[i][0], matriz_rdralfa[i][2])
        if abs(xo)>depht or abs(yo)>depht:
           xo = 0
           yo = 0
        x_vo.append(xo)
        y_vo.append(yo)
    return(x_vo, y_vo)

def triangulacion_datos( ro, alfo):#determina el X y Y dependiendo del radio y ángulo
        alfo = alfo + (pi/2)
        Y=(((math.sin(alfo-(pi/2)))*ro))
        X=(((math.cos(alfo-(pi/2)))*ro))
        return(X,Y)    
    
    
    
