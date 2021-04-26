# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:22:22 2021

@author: ahmed
"""
from math import sqrt


plot1 = [1,3]
plot2 = [2,5]


euclidean_distance = sqrt(sum((plot1[i] -plot2[i])**2 for i in range(len(plot1))))

print(euclidean_distance)