# -*- coding: utf-8 -*-
import web
import web.db
import sae.const

class dbOperation:    
    db = web.database(
        dbn='mysql', 
        port=int(sae.const.MYSQL_PORT), 
        host=sae.const.MYSQL_HOST, 
        db=sae.const.MYSQL_DB, 
        user=sae.const.MYSQL_USER, 
        pw=sae.const.MYSQL_PASS
    ) 
    
    def addfk(username, fktime, fkcontent):      	
   		if(db)
        	return db.insert('fk', user=username, time=fktime, fk_content=fkcontent)
        else:
            return "Error"
	def get_fkcontent():
		return db.select('fk', order='id')