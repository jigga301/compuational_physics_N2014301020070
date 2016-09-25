# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:13:49 2016

@author: asus
"""
import os
import time
os.system('cls')
A=[[' ' for i in range(80)]for j in range(80)]
B=[[' ' for i in range(80)]for j in range(80)]
A[20][20]='*'
A[20][21]='*'
A[20][22]='*'
A[20][23]='*'
A[21][20]='*'
A[19][20]='*'
A[18][20]='*'
A[21][21]='*'
A[21][19]='*'
A[21][18]='*'
A[22][21]='*'
A[23][21]='*'

B[19][19]='*'
B[19][22]='*'
B[20][20]='*'
B[20][21]='*'
B[21][20]='*'
B[21][21]='*'
B[22][19]='*'
B[22][22]='*'
for k in range (1000):
    for i in range(80):
        for j in range(80):
            print A[i][j],
        print ''
    time.sleep(0.02)
    os.system('cls')
    for i in range(80):    
        for j in range(80):
            print B[i][j],
        print ''
    time.sleep(0.02)
    os.system('cls')
