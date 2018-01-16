# _*_ coding:utf-8 _*_
import web
import web.db
import sae.const


db = web.database(
    dbn='mysql',
    port=int(sae.const.MYSQL_PORT),
    host=sae.const.MYSQL_HOST,
    db=sae.const.MYSQL_DB,
    user=sae.const.MYSQL_USER,
    pw=sae.const.MYSQL_PASS
)