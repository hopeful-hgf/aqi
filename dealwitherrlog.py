import psycopg2
with open('poi_errlog','r',encoding='gbk')  as fin:
    flg=True
    while True:
        line=fin.readline()
        if not line:
            break
#         print(line)
        flg=not flg
        if not flg:
            continue
#             print(line)
        poi=eval(line)
        parent = poi['parent']
        if 'address' not in poi or type(poi['address'])!=str:
            address=""
        else:
            address = poi['address']
        pname = poi['pname']
        biz_type = poi['biz_type']
        cityname = poi['cityname']
        poitype = poi['type']
        typecode = poi['typecode']
        childtype = poi['childtype']
        adname = poi['adname']
        name = poi['name']
        location = poi['location']
        tel = poi['tel']
        id = poi['id']
        
#        print(address)       
        pname=pname.replace("'","''")
        name=name.replace("'","''")
        address=address.replace("'","''")
        conn = psycopg2.connect(
            database="aqi",
            user="postgres",
            password="thebestisyet2B",
            host="localhost",
            port="5432",
        )
        cur = conn.cursor()
        sql = "insert into amappoi(parent,address,pname,biz_type,cityname,type,typecode,childtype,adname,name,location,tel,id) values('{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}')".format(
            parent, address, pname, biz_type, cityname, poitype, typecode, childtype, adname, name, location, tel, id)
        cur.execute(sql)
        conn.commit()
