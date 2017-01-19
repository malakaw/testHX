#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import datetime
import json
# 是否打印返回结果
print_response = True
import re
pattern_header_value = re.compile(r"^\$api_\d{1,3}_response_.*\$$")

def getNowDateStr():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


def getFromDict(dataDict, keys):
    d = json.loads(str(dataDict))
    try:
        for k in keys.split("/"): d = d[k]
    except:
        print "error in getFromDict"
        d = "error--get-assert val"
    return d

def getApiResponseKey(responseSourceStr):
    api_number   = responseSourceStr.split("_")[1]
    response_key = responseSourceStr.split("_response_")[1][:-1]
    return [api_number,response_key]

# field_1 : header  name
# field_2 : header  set value 
def getHeader(field_1,field_2,response_dict):
    result_h2 = ""
    if pattern_header_value.match(field_2):
        temp_h =  getApiResponseKey(field_2)
        # api number
        result_h2 = getFromDict(json.dumps(response_dict[str(temp_h[0])]) ,str(temp_h[1]))
    else:
        result_h2 = field_2
    return result_h2    
    

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

    k = "dataMap/success"
    k = "code"
    print getFromDict(json_s,k)
#    getApiResponseKey("$api_1_response_data$")
