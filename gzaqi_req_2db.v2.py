import requests as rq
import psycopg2

url = "http://112.94.64.160:8023/api/public/gzhbapp/airQuality/getairQualityTimes/GetAllRealTimeData"
response=rq.get(url)
header=response.headers
curtime=header['Date']
curaqi=response.text


# with open ('aqi/gzrecord','a') as fout:
#     fout.writelines(curtime)
#     fout.writelines('\n')
#     fout.writelines(curaqi)
#     fout.writelines('\n')

curaqi=curaqi.replace(":null,",':"null",')
a=eval(curaqi)
b=a['data']

for c in b:
    try:
        
        aqi= c["AQI"] 
        aqitime= c["AQITIME"] 
        aqi_= c["AQI_"] 
        co= c["CO"] 
        co_24h= c["CO_24H"] 
        co_iaqi= c["CO_IAQI"] 
        displayname= c["DISPLAYNAME"] 
        dwcode= c["DWCODE"] 
        dwname= c["DWNAME"] 
        msg= c["MSG"] 
        no2= c["NO2"] 
        no2_24h= c["NO2_24H"] 
        no2_iaqi= c["NO2_IAQI"] 
        o3= c["O3"] 
        o3_24h= c["O3_24H"] 
        o3_8h= c["O3_8H"] 
        o3_8h_24h= c["O3_8H_24H"] 
        o3_8h_iaqi= c["O3_8H_IAQI"] 
        o3_iaqi= c["O3_IAQI"] 
        pm10= c["PM10"] 
        pm10_24h= c["PM10_24H"] 
        pm10_iaqi= c["PM10_IAQI"] 
        pm2_5= c["PM2_5"] 
        pm2_5_24h= c["PM2_5_24H"] 
        pm2_5_iaqi= c["PM2_5_IAQI"] 
        primary= c["PRIMARY"] 
        primary_= c["PRIMARY_"] 
        quality= c["QUALITY"] 
        quality_= c["QUALITY_"] 
        so2= c["SO2"] 
        so2_24h= c["SO2_24H"] 
        so2_iaqi= c["SO2_IAQI"] 
        stcode= c["STCODE"] 
        stname= c["STNAME"] 
        x= c["X"] 
        y= c["Y"] 
        _nullflags= c["_NULLFLAGS"] 

        if displayname=='全市平均':
            x=0
            y=0
        conn = psycopg2.connect(
        database="aqi",
        user="postgres",
        password="thebestisyet2B",
        host="localhost",
        port="5432",
        )
        cur = conn.cursor()
        sql = "insert into gzrecord2(aqi, aqitime, aqi_, co, co_24h, co_iaqi, displayname, dwcode, dwname, msg, no2, no2_24h, no2_iaqi, o3, o3_24h, o3_8h, o3_8h_24h, o3_8h_iaqi, o3_iaqi, pm10, pm10_24h, pm10_iaqi, pm2_5, pm2_5_24h, pm2_5_iaqi, primarywrw, primary_, quality, quality_, so2, so2_24h, so2_iaqi, stcode, stname, x, y, _nullflags) values({},'{}',{},{},{},{}, '{}', '{}', '{}', '{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}, '{}','{}','{}', '{}', {},{},{},'{}','{}',{},{},'{}');".format(
        aqi,
        aqitime,
        aqi_,
        co,
        co_24h,
        co_iaqi,
        displayname,
        dwcode,
        dwname,
        msg,
        no2,
        no2_24h,
        no2_iaqi,
        o3,
        o3_24h,
        o3_8h,
        o3_8h_24h,
        o3_8h_iaqi,
        o3_iaqi,
        pm10,
        pm10_24h,
        pm10_iaqi,
        pm2_5,
        pm2_5_24h,
        pm2_5_iaqi,
        primary,
        primary_,
        quality,
        quality_,
        so2,
        so2_24h,
        so2_iaqi,
        stcode,
        stname,
        x,
        y,
        _nullflags,

        )
        # print(sql)
        cur.execute(sql)
        conn.commit()

    except Exception as e:
        print(e.args)
        print(c)
        with open("errlog2", "a") as fout:
            fout.writelines(str(e.args) + "\n")
            fout.writelines(str(c)+'\n')
