# _*_ coding:utf-8 _*_
import web
import web.db
import sae.const


db = web.database(
	db_name = 'mysql',
    user = sae.const.MYSQL_USER,
    pwd = sae.const.MYSQL_PASS,
    host = sae.const.MYSQL_HOST,
    port=int(sae.const.MYSQL_PORT)
)