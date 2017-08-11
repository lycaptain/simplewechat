# -*- coding: utf-8 -*-
import web
import web.db
import sae.const

class dbOperation:
    
	db = web.database(
         dbn='mysql',
         host=sae.const.MYSQL_HOST,
         port=int(sae.const.MYSQL_PORT),
         user=sae.const.MYSQL_USER,
         passwd=sae.const.MYSQL_PASS,
         db=sae.const.MYSQL_DB
	)
    
	def addfk(username, fktime, fkcontent):
        	ans = db.insert('fk', user=username, time=fktime, fk_content=fkcontent)
   		return ans
    							
    def get_fkcontent( ):
       	ans = db.select('fk', order='id')
    	return ans