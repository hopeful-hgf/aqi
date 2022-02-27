import requests as rq
import json

# 20220120
# url = "http://112.94.64.160:8023/gzaqi_new/MapData.cshtml"
url = "http://112.94.64.160:8023/api/public/gzhbapp/airQuality/getairQualityTimes/GetAllRealTimeData"

response=rq.get(url)
header=response.headers
curtime=header['Date']
curaqi=response.text
# curaqi=curaqi.strip('[]')
# curaqi = curaqi.replace('},{', '}∴{')
# itercur=curaqi.split('∴')
# print(response.text)

with open ('aqi/gzrecord.v2','a') as fout:
    fout.writelines(curtime)
    fout.writelines('\n')
    fout.writelines(curaqi)
    fout.writelines('\n')
