#!/usr/bin/python
#coding:utf-8
#author:joe011
#from:https://github.com/joe011/python/blob/master/check_ip138.py

import sys
import urllib2
import re

def ISIP(s):
    return len([i for i in s.split('.') if (0 <= int(i) <= 255)]) == 4

def URL(ip):
    try:
        uip = urllib2.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%ip)
        fip = uip.read()
        rip=re.compile(r"<br/><b>查询结果：(.*)</b><br/>")
        result=rip.findall(fip)
        if result:
            print "%s\t %s" %(ip,result[0].decode('utf-8'))

    except urllib2.URLError,e:
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code:', e.code)
        elif hasattr(e, 'reason'):
            print('We failed to reach a server')
            print('Reason', e.reason)

def DO(domain):
    try:
        url=urllib2.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%domain)
        f=url.read()
        r=re.compile(r"&gt; \r\n(.*)\t\r\n<br/><b>查询结果：(.*)</b><br/>")
        result=r.findall(f)
        for i in result:
            print "%s\t %s\t %s\t" %(domain,i[0],i[1].decode('utf-8'))
    except urllib2.URLError,e:
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code:', e.code)
        elif hasattr(e, 'reason'):
            print('We failed to reach a server')
            print('Reason', e.reason)

if __name__ == "__main__":
    try:
        tmpArgv = sys.argv[1:]
        ip = "".join(tmpArgv)
        errInfo = "输入的IP地址和域名格式不对！"
        if not re.findall('(\d{1,3}\.){3}\d{1,3}',ip):
            if re.findall(r'(\w+\.)?(\w+)(\.\D+){1,2}',ip) :
                domain=ip
                DO(domain)
            else:
                print "%s"%errInfo.decode('utf-8')
        else:
            if ISIP(ip):
                URL(ip)
            else:
                print "%s"%errInfo.decode('utf-8')
    except KeyboardInterrupt:
        print "You press Ctrl+C"
        sys.exit()
    
