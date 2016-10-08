# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/9/29'
#    __Desc__ = 实现命令行下的翻译程序实现

from urllib2 import *
import json

def getHtml(type=True, text='English'):
    if type:
        translate_url = "http://fanyi.baidu.com/v2transapi?query=%s"%text
    else:
        translate_url = "http://fanyi.baidu.com/v2transapi?from=zh&to=en&query=%s" % text
    data = urlopen(translate_url).read()
    return data


def main():

    flag = raw_input("英文转汉语输入1，汉语转英文输入0：".encode('gbk')).encode('utf8')
    # 这里使用encode为gbk的方式是为了在Windows的DOS界面下不发生乱码的情况
    querytext = raw_input("请输入您想查询的内容\n".encode('gbk')).decode('gbk')
    if flag == 1:
        data = getHtml(type=False, text=querytext)
    else:
        data = getHtml(text=querytext)
    data = json.loads(data)
    # 分析json数据串，定向的获取到相应的解释信息
    # 首先打印出单词的简单含义
    print "\nResult:"
    print data['trans_result']['data'][0]['dst']



if __name__ == '__main__':
   main()


