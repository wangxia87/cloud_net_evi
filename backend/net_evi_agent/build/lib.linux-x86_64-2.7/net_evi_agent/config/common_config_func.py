#!/usr/bin/python
#-*- coding:UTF-8 -*-
def strPartition(str1,str2):
        string_tup=str1.partition(str2)
        return string_tup

def fillExtraInfoDict(dic,line):
        tup=strPartition(line,"=")
        key=tup[0].strip()
        value=tup[2].strip()
        dic[key]=value
        return

