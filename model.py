# _*_ coding:utf-8 _*_
import web
import web.db
db = web.database(
    dbn='mysql',
    db='app_simplewechat',
    user='wechat',
    pw='41512227',
    host='120.78.135.116',
    port=3306
)

def upoj(oj_id,oj_name,oj_url,contest_name,oj_time,oj_week,oj_acess):
    return db.insert('recentoj', id=oj_id, oj=oj_name, url=oj_url, name=contest_name, time=oj_time, week=oj_week,
                     acess=oj_acess)

def get_ojmessage():
    return db.select('recentoj', order='id')

def delectoj():
    return db.delete('recentoj', where='id<30')




