#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:09:41 2019

@author: protosem02
"""
'''
senti classifer
'''

SentimentDict={1:['good','nice','pleasant','awesome'],-1:['bad','worst','unsatisfactory'],0:'neutral'}
s=input().split(' ')
sentiscore=0
for i in s:
    for key,value in SentimentDict.items():
        if i in value:
            sentiscore+=SentimentDict[i]
print(sentiscore)