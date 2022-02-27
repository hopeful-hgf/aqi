import requests as rq
import json

# url = "http://112.94.64.160:8023/gzaqi_new/MapData.cshtml"
url = "http://112.94.64.160:8023/api/public/gzhbapp/airQuality/getairQualityTimes/GetAllRealTimeData"
header = {
            'Host': '112.94.64.160:8023',
            'Connection': 'keep-alive',
            'Content-Length': '21',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://112.94.64.160:8023',
            'Referer': 'http://112.94.64.160:8023/gzaqi_new/RealTimeDate.html',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
          }
parameters = {'OpType': 'GetAllRealTimeData'}

a = json.dumps(parameters)
# print(a)
response=rq.post(url,headers=header,data=parameters)
header=response.headers
curtime=header['Date']
curaqi=response.text
curaqi=curaqi.strip('[]')
curaqi = curaqi.replace('},{', '}∴{')
itercur=curaqi.split('∴')
# print(response.text)

with open ('aqi/gzrecord','a') as fout:
    fout.writelines(curtime)
    fout.writelines('\n')
    for it in itercur:
        fout.writelines(it)
        fout.writelines('\n')
    fout.writelines('\n')
