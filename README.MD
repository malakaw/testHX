testHX  1 是一个python2.7写的简单测试restful接口的通用工具，可以在excel中配置请求的接口／参数／断言，断言现在只支持“等于”，执行完后直接写入html,然后打开;现在只支持response是json格式的数据。
请求method支持 POST/GET

# 准备工作 #

步骤一
安装2.7 python 

步骤二
安装pip

步骤三
```
pip install requests
pip install pyhtml
pip install xlrd
```


# 使用 #

## 1）文件目录 ##
```
├── README.MD
├── action
│   ├── acc.py
├── case
│   ├── c1
│   │   └── c1.xlsx
├── component
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── common.py
│   ├── common.pyc
│   ├── excelUtil.py
│   ├── excelUtil.pyc
│   ├── htmlUtil.py
│   ├── htmlUtil.pyc
│   ├── requestUtil.py
│   ├── requestUtil.pyc
│   └── result_case1.html
└── result
```
action/acc.py 是启动执行文件
case目录是存放case的配置目录，都是excel文件
result是存放执行后的结果文件，都是html,action/acc.py执行完自动打开

## 2)acc.py ##
```    
if __name__ == "__main__":
    action(3,True)

```
参数3就是 case3 的意思，调用的是 case/c3/c3.excel配置文件;
参数True就是打印出页面显示的意思，默认都要打开




## 配置文件 .excel ##
这个里面有几个工作表

### 工作表1-apis ###
请求的 api
### 工作表2-params ###
请求 api需要传的参数
### 工作表3-assert ###
请求api对应的断言
### 工作表4-header ###
请求 api需要传的headers
