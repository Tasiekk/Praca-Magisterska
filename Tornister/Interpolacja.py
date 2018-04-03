# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:06:30 2018

@author: Tasiek
"""
import numpy as np
import matplotlib.pyplot as plt
def interpolation(x,y,degree):
#    plt.scatter(x, y)
#    xp = np.linspace(2014, 2018, 100)
    z = np.polyfit(x, y, degree)
    p = np.poly1d(z)
#    plt.plot(x,y,".",xp,p(xp),'-')
#    plt.show()
    return p(2018)

def error(x,y,degree):
    z = np.polyfit(x, y, degree)
    p = np.poly1d(z)
    error = np.zeros(4)
    for i in range(0,4):
        error[i]=(p(x[i])-y[i])*(p(x[i])-y[i])
    error = np.sqrt(np.sum(error))
    return error


