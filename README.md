# FaceScore
python2.7  

## 使用
```python
from FaceScore import getScore
img_url = 'http://d.hiphotos.baidu.com/zhidao/pic/item/c9fcc3cec3fdfc0371b93114d63f8794a5c2265d.jpg'
data = getScore(img_url)
```
  
## 返回数据
		{    
			score: ‘6.8’,  
			text: ‘颜值6.8分，哥哥不错，备胎竞争向来很激烈，千万别松懈！’，  
			img_url: 'http://mediaplatform.trafficmanager.cn/image/fetchimage?key=UQAfAC8ABAAAAFcAFgAGABYASgAwAEIANABDAEIANgAxADgARAAzAEYAOABBADkAMwA2AEYAMgAyADMANABBADIARgBBAEYARABCADQARgA2ADAA'
		}