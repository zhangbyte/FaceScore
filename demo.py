#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FaceScore import getScore

img_url = 'http://d.hiphotos.baidu.com/zhidao/pic/item/c9fcc3cec3fdfc0371b93114d63f8794a5c2265d.jpg'
data = getScore(img_url)

print data