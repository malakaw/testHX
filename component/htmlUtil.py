#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from pyhtml import html,body,div,hr,br,pre
import common as comm
  

def pushApisContent(c_number , resultAssert):
    htm = html(
        body(
            div("case-%s" % c_number),
            map(lambda x:div(hr,u"%s ok:%s" % (x[0] , x[1]),br ,pre(x[2])) ,resultAssert)
        )
    )
    return htm.render()
    

def writeHtml(c_number , resultAssert):
    filename = "../result/C%s_%s.html" % (c_number ,comm.getNowDateStr())
    file_object = open(filename, 'w')
    file_object.write(pushApisContent(c_number ,resultAssert).encode('utf-8'))
    file_object.close()
    return filename

    
if __name__ == "__main__":
    print ""
