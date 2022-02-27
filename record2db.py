from datetime import datetime

import psycopg2

with open("gzrecord", "r") as fin:
    # line= fin.readline()
    # print(line)
    # line=fin.readline()
    # print(line)
    # a=eval(line.replace("new Date",''))
    # print(a)
    nline = 0
    format = "%a,%d %b %Y %H:%M:%S GMT"
    while True:
        nline += 1
        line = fin.readline()
        if nline<508095:
            continue
        if not line:
            break
        if line.strip()[-3:] == "GMT" or len(line) < 3:
            continue
        # if nline > 4:
        #     break
        # print(line)
        try:

            a = eval(line.replace("new Date", ""))

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
            print(line)
            with open("errlog", "a") as fout:
                fout.writelines(str(nline) + "\n")
                fout.writelines(str(e.args) + "\n")
                fout.writelines(line)

