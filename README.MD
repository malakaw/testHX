

# 准备工作 #

步骤一
安装2.7 python 

步骤二
安装pip

步骤三
pip install requests
pip install pyhtml
pip install xlrd


步骤四
 git clone https://github.com/malakaw/testHX.git


# 使用 #

## 1）文件目录 ##

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

action/acc.py 是启动执行文件
case目录是存放case的配置目录，都是excel文件
result是存放执行后的结果文件，都是html,action/acc.py执行完自动打开

## 2)acc.py ##
`    
if __name__ == "__main__":
    action(3,True)
`
