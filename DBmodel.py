# -*- coding: utf-8 -*-
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

def addfk(username, fktime, fkcontent):      	
	return db.insert('fk', user='41512241', time='2017', fk_content='hello')

def get_fkcontent():
    return db.select('fk', order='id')