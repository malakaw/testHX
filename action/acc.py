#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import webbrowser
import json
import requests
import os

import sys
sys.path.append("..")
import component.excelUtil   as excU
import component.requestUtil as req
import component.htmlUtil    as htmU
import component.common      as comm
excelFilePath_ = "../case/c%s/c%s.xlsx"

def assertR(api_url , result , assert_val):
    is_ok = u"☺"
    for k , v in assert_val.items():
        if str(comm.getFromDict(result,k)).lower() != str(assert_val[k]).lower():
            is_ok = u"☠☠☠☠"
    return is_ok

def getParams(params,api_number):
    api_params    = None
    paramstr_     = "param_%s_"  % api_number
    print "--->"
    print api_number
    print params
    api_params = {}
    for para in params:
        if paramstr_ in para[0] and "json" not in para[0]:
            api_params[para[1]] = para[2]
    for para_ in params:
        if paramstr_ in para_[0] and "json" in para_[0]:
            api_params =  para_[1]
    print api_number
    print api_params
    return api_params



        

def handleAPI(c_number,apis , params , asserts , headers):
    result_info = []
    for api in apis:
        print api
        print api[0]
        assert_ok     = None
        api_url       = None
        api_method    = None
        api_content   = None
        api_headers   = {}
        api_params    = {}
        api_assert    = {}

        api_number    = api[0].split("_")[1]
        paramstr_     = "param_%s_"  % api_number
        assert_       = "assert_%s_"  % api_number
        header_       = "header_%s_" % api_number
        api_url       = api[1]
        api_method    = api[2]
        api_content   = api[3]

        api_params = getParams(params,api_number)
        for h in headers:
            if header_ in h[0]:
                api_headers[h[1]] = h[2] 

        for asser in asserts:
            asser = filter(lambda x: len(str(x).strip()) > 0, asser)
            if len(asser) > 0 :
                if assert_ in asser[0]:
                    api_assert[asser[1]] = asser[2]
                    
        if "post" in api_method:
            result = req.getRsponse(api_url , api_params , api_content,api_headers, requests.post)
        else:
            result = req.getRsponse(api_url , api_params , api_content,api_headers,requests.get)
        print result
        print api_assert
        result_utf8 = json.dumps(result,indent=1,ensure_ascii=False).encode('utf8')
        assert_ok = assertR(api_url , result_utf8 , api_assert)

#        print unicode(result_utf8,"utf-8")
        result_info.append([api_url,assert_ok,unicode(result_utf8,"utf-8")])
    return htmU.writeHtml(c_number,result_info)

        
def action(c_number , openHtml = False):
    excelFilePath = excelFilePath_ % (c_number , c_number)
    apis          = excU.getApis(excelFilePath)
    params        = excU.getParams(excelFilePath)
    asserts       = excU.getAssert(excelFilePath)
    headers       = excU.getHeaders(excelFilePath)
    htmlFileName  = handleAPI(c_number,apis,params,asserts,headers)
    if openHtml:
        webbrowser.open_new('file://' + os.path.realpath(htmlFileName))

    
if __name__ == "__main__":
    action(3,True)
