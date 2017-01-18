#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests
import json
dict_content = {"json": {"content-type": "application/json"},
                "Json": {"Content-Type": "application/json"},
                "text": {"Content-Type": "text/plain"}}

head_json = {"content-type" : "application/json"}

def getRsponse(url,params,content,headers_,method = requests.post, is_json_content=False):
#    print url
#    print params
#    print content
#    print type(params)
    
    if "json" in content:
        r = method(url,json = json.loads(params),headers = headers_)
    else:
        r = method(url,data = params,headers = headers_)
    return r.json()




if __name__ == "__main__":
    params = '''{"mobilePhone" : "18217629954",
              "password" : "wap123456"
    }'''
    result = getRsponse("http://longguo.dev.rs.com/api/userInfoV2/login" ,
                        params,
                        "json",
                        {}
                        )
    print result['resDescription']
    print result
    print result['resCode']


    result = requests.get("http://api-bill.dev.rs.com/bill/B/billorder/detail/1701170018" , headers={"x-auth-token": result["data"]})
   # result = requests.get("http://api-bill.dev.rs.com/bill/B/billorder/detail/1701020117" , headers={"x-auth-token": "1ad24f76-0389-433a-8917-922c863e59b2"})
    print result.json()
    print result.json()["message"]

    r =  requests.post("http://192.168.124.13:53305/luckyDraw",headers={"Content-Type": "application/json"})
    print r.json()


    
   # params = {'username' : '18605106755' ,
   #           'password' : 'e10adc3949ba59abbe56e057f20f883e',
   #           'appId'    : 'c3'}
   # result = getRsponse("http://api-user.test.rs.com/api/user/authenticate" , params,"form")
   # print result
   # print result['code']

