# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:32:38 2016
Reference - MITx: 6.00.1x Introduction to Computer Science and Programming Using Python

@author: ericgrimson
"""

def selSort(L):
    for i in range(len(L) - 1):
        print(L)
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):                #At the end of one while loop one element will be sorted. 
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp


test = [1, 5, 3, 8, 4, 9, 6, 2]
