#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import requests

dict_content = {"json": {"content-type": "application/json"},
                "text": {"Content-Type": "text/plain"}}

head_json = {"content-type" : "application/json"}

def getRsponse(url,params,content,method = requests.post,is_json_content=False):
    header_ = dict_content.get(content,None)
    print params
    print header_
    r = method(url , data = params,headers = header_)
    return r.json()




if __name__ == "__main__":
    params = {'username' : '18605106755' ,
              'password' : 'e10adc3949ba59abbe56e057f20f883e',
              'appId'    : 'c3'}
    result = getRsponse("http://api-user.test.rs.com/api/user/authenticate" , params,"form")
    print result
    print result['code']



