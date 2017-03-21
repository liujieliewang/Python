import requests
from random import randint
from lxml import etree
from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET
import time
import threading

app = Flask(__name__)

@app.route('/Hello')
def hello():
    return "Python Say: Hello"

@app.route('/',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        print('coming Get')
        data = request.args
        token = '**********'
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        s = s.encode()
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    if request.method == 'POST':
        xml_str = request.stream.read()
        xml = ET.fromstring(xml_str)
        toUserName=xml.find('ToUserName').text
        fromUserName = xml.find('FromUserName').text
        createTime = xml.find('CreateTime').text
        msgType = xml.find('MsgType').text
        if msgType != 'text':
            reply = '''
            <xml>
            <ToUserName><![CDATA[%s]]></ToUserName>
            <FromUserName><![CDATA[%s]]></FromUserName>
            <CreateTime>%s</CreateTime>
            <MsgType><![CDATA[%s]]></MsgType>
            <Content><![CDATA[%s]]></Content>
            </xml>
            ''' % (
                fromUserName,
                toUserName,
                createTime,
                'text',
                'Unknow Format, Please check out'
                )
            return reply
        content = xml.find('Content').text
        #msgId = xml.find('MsgId').text
        if u'笑话' in content:
            global jokes,TimeUpdata
            joke =  jokes[randint(0,len(jokes))]
            reply = '''
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[%s]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    ''' % (fromUserName, toUserName, createTime, msgType, joke)
            TimeNow = time.time()
            #print('now',TimeNow,'updata',TimeUpdata,'=',TimeNow-TimeUpdata)
            if (TimeNow - TimeUpdata) > 600:
                t = threading.Thread(target=getjoke, args=())
                t.start()
            return reply
        else:
            if type(content).__name__ == "unicode":
                content = content[::-1]
                content = content.encode('UTF-8')
            elif type(content).__name__ == "str":
                print(type(content).__name__)
                #content = content.decode('utf-8')
                content = content[::-1]
            reply = '''
                    <xml>
                    <ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime>
                    <MsgType><![CDATA[%s]]></MsgType>
                    <Content><![CDATA[%s]]></Content>
                    </xml>
                    ''' % (fromUserName, toUserName, createTime, msgType, content)
            return reply
def getjoke():
    global jokes, TimeUpdata
    url = 'http://www.qiushibaike.com/text/'
    r = requests.get(url)
    tree = etree.HTML(r.text)
    contentlist = tree.xpath('//div[contains(@id, "qiushi_tag_")]')
    jokes = []
    for i in contentlist:
        content = i.xpath('a/div[@class="content"]/span/text()')
        contentstring = ''.join(content)
        contentstring = contentstring.strip('\n')
        jokes.append(contentstring)
    TimeUpdata = time.time()
    print(jokes[0])

if __name__ == "__main__":
    global jokes,TimeUpdata
    getjoke()
    app.run(host='0.0.0.0', port=80)
