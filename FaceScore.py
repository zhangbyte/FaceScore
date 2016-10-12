#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64,urllib,urllib2,json,time,re

api_url = 'http://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi'
img_url = 'http://kan.msxiaobing.com/Api/Image/UploadBase64'

def didImg(imgUrl):
    """
    接收图片URL，将其转换为base64字符串形式
    """
    file = urllib2.urlopen(imgUrl)
    imgData = base64.b64encode(file.read())
    return imgData

def upload(imgData):
    """
    上传本地图片到微软服务器,返回json格式服务器的图片地址
    """
    return curl(img_url, imgData)

def curl(url, data):
    """
    发送post请求
    """
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    return response.read()

def getScore(imgUrl):
    """
    获取照片颜值
    """
    imgData = didImg(imgUrl)
    imgRes = upload(imgData)
    imgJsonData = json.loads(imgRes)
    nowTime = str(int(time.time()))
    values = {
        'MsgId': nowTime+"123",
        'CreateTime': nowTime,
        'Content[imageUrl]': imgJsonData['Host']+imgJsonData['Url']
    }
    data = urllib.urlencode(values)
    res = curl(api_url, data)
    resJsonData = json.loads(res)
    text = resJsonData['content']['text']
    nums = re.search(r'\d+.\d+', text)
    output = {
        'score': nums.group(0) if nums else 0,
        'text': text,
        'img_url': resJsonData['content']['imageUrl']
    }
    return output

if __name__=="__main__":
    url = 'http://d.hiphotos.baidu.com/zhidao/pic/item/c9fcc3cec3fdfc0371b93114d63f8794a5c2265d.jpg'
    print getScore(url)