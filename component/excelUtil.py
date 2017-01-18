#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import xlrd


def readFile(fname):
    data = xlrd.open_workbook(fname)
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        print table.row_values(i)
        
def getValues(fname , sheets_number):
    vals = []
    data = xlrd.open_workbook(fname)
    table = data.sheets()[sheets_number]
    nrows = table.nrows
    for i in range(nrows):
        vals.append(table.row_values(i))
    return vals
        
def getParams(fname):
    return getValues(fname , 1)
        
def getApis(fname):
    return getValues(fname , 0)

def getAssert(fname):
    return getValues(fname , 2)

def getHeaders(fname):
    return getValues(fname , 3)

def getVal(fname):
    return getValues(fname , 4)


if __name__ == "__main__":
#    print getApis("/Users/wengxiaojun/work/redstar/python/testHX/case/c1/c1.xlsx")
    print getVal("/Users/wengxiaojun/work/redstar/python/github_hx/testHX/case/c2/c2.xlsx")
    val_ = getVal("/Users/wengxiaojun/work/redstar/python/github_hx/testHX/case/c2/c2.xlsx")
    print val_[0][1]
    eval(val_[0][1])
    #eval(compile(val_[0][1], '', 'eval'))
