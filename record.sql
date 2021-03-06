create table gzrecord
(
recordstamp timestamp,
date_ymd timestamp,
AQITIME varchar(15),
DWCODE int,
DWNAME varchar(15),
SO2_1H real,
SO2_24H real,
NO2_1H real,
NO2_24H real,
PM10_1H real,
PM10_24H real,
CO_1H real,
CO_24H real,
O3_1H real,
O3_1H_24H real,
O3_8H real,
O3_8H_24H real,
PM2_5_1H real,
PM2_5_24H real,
AQI real,
QUALITY varchar(7),
PRIMARYwrw varchar(15),
SO2_1H_AQI real,
NO2_1H_AQI real,
PM10_1H_A real,
CO_1H_AQI real,
O3_1H_AQI real,
O3_8H_AQI real,
PM2_5_1HA real,
AQI_ real,
QUALITY_ varchar(7),
PRIMARY_ varchar(15),
_NullFlags varchar(7),
Msg varchar(255)
)