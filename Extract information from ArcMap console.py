#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import math
import time
import numpy as np

def readandwrite(txtfilename):
    # read elevation
    f = open(txtfilename, "r", encoding='utf-8')
    # skip head
    # for i in range(6):
    #     f.readline()
    # AltiList = []
    linelist = []
    resultlist = []

    flines = f.readlines()
    for fline in flines:
        line = fline.split()
        linelist.append(line)

    for i in range(2,1834,14):
        resultlist.append([linelist[i][10].split('"')[0], linelist[i+9][3].split('。')[0]])
        
    return resultlist

def main():
    txt1 = ''
    txt2 = ''

    result = readandwrite(txt2)

    f = open("result.csv",'w')
    # f.write('picturename,count,SVF\n')
    for dataline in result:
        f.write(str(dataline[0])+','+str(dataline[1]))
        f.write('\n')

    print("Done!")
    
if __name__ == '__main__':
    main()
