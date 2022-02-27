import requests as rq
import json
import psycopg2
from datetime import datetime

url = "http://112.94.64.160:8023/gzaqi_new/MapData.cshtml"
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

for it in itercur:
    try:

        a = eval(it.replace("new Date", ""))

        recordstamp = datetime.fromtimestamp(a["AQITIME"] / 1000)
        # recordstamp = a["AQITIME"] / 1000
        aqitime = a["AQITIME"]
        # print(aqitime)
        dwcode = a["DWCODE"]
        dwname = a["DWNAME"]
        so2_1h = a["SO2_1H"]
        so2_24h = a["SO2_24H"]
        no2_1h = a["NO2_1H"]
        no2_24h = a["NO2_24H"]
        pm10_1h = a["PM10_1H"]
        pm10_24h = a["PM10_24H"]
        co_1h = a["CO_1H"]
        co_24h = a["CO_24H"]
        o3_1h = a["O3_1H"]
        # o3_24h=a['O3_24H']
        o3_1h_24h = a["O3_1H_24H"]
        o3_8h = a["O3_8H"]
        o3_8h_24h = a["O3_8H_24H"]
        pm2_5_1h = a["PM2_5_1H"]
        pm2_5_24h = a["PM2_5_24H"]
        aqi0 = a["AQI"]
        quality = a["QUALITY"]
        primary = a["PRIMARY"]
        so2_1h_aqi = a["SO2_1H_AQI"]
        no2_1h_aqi = a["NO2_1H_AQI"]
        pm10_1h_a = a["PM10_1H_A"]
        co_1h_aqi = a["CO_1H_AQI"]
        o3_1h_aqi = a["O3_1H_AQI"]
        o3_8h_aqi = a["O3_8H_AQI"]
        pm2_5_1ha = a["PM2_5_1HA"]
        aqi_ = a["AQI_"]
        quality_ = a["QUALITY_"]
        primary_ = a["PRIMARY_"]
        _nullflags = a["_NullFlags"]
        msg = a["Msg"]

        conn = psycopg2.connect(
            database="aqi",
            user="postgres",
            password="thebestisyet2B",
            host="localhost",
            port="5432",
        )
        cur = conn.cursor()
        sql = "insert into gzrecord(recordstamp, aqitime, dwcode, dwname, so2_1h, so2_24h, no2_1h,no2_24h, pm10_1h, pm10_24h, co_1h, co_24h, o3_1h, o3_1h_24h, o3_8h, o3_8h_24h, pm2_5_1h, pm2_5_24h, aqi, quality, primarywrw, so2_1h_aqi, no2_1h_aqi, pm10_1h_a, co_1h_aqi, o3_1h_aqi, o3_8h_aqi, pm2_5_1ha, aqi_, quality_, _NullFlags, msg) values('{}','{}',{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},'{}','{}','{}');".format(
            recordstamp,
            aqitime,
            dwcode,
            dwname,
            so2_1h,
            so2_24h,
            no2_1h,
            no2_24h,
            pm10_1h,
            pm10_24h,
            co_1h,
            co_24h,
            o3_1h,
            o3_1h_24h,
            o3_8h,
            o3_8h_24h,
            pm2_5_1h,
            pm2_5_24h,
            aqi0,
            quality,
            primary,
            so2_1h_aqi,
            no2_1h_aqi,
            pm10_1h_a,
            co_1h_aqi,
            o3_1h_aqi,
            o3_8h_aqi,
            pm2_5_1ha,
            aqi_,
            quality_,
            _nullflags,
            msg,
        )
        # print(sql)
        cur.execute(sql)
        conn.commit()

    # except (SyntaxError, NameError,ValueError,TypeError):
    #     print(line)
    except Exception as e:
        print(e.args)
        print(it)
        with open("errdblog", "a") as fout:
            fout.writelines(str(e.args) + "\n")
            fout.writelines(it)

