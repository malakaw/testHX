#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import datetime
import json
# 是否打印返回结果
print_response = True

def getNowDateStr():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


def getFromDict(dataDict, keys):
    d = json.loads(dataDict)
    try:
        for k in keys.split("/"): d = d[k]
    except:
        print "error in getFromDict"
        d = "error--get-assert val" 
    return d

    

if __name__ == "__main__":
    json_s = '''
    {
     "message": "成功", 
     "code": "200", 
     "dataMap": {
      "message": "领取失败", 
      "success": false
     }
    }     
    '''

    k = "dataMap/success1"
    print getFromDict(json_s,k)
