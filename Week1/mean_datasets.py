# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:21:47 2017

@author: ursa
"""
import numpy as np
def mean_datasets(csv):
  res = np.loadtxt(csv[0],delimiter=',')
  for i in range(1,len(csv)):
    res += np.loadtxt(csv[i], delimiter=',')
  res = np.round(res/len(csv),1)
  return res

if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))