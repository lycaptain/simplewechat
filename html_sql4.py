import MySQLdb


class HtmlSql1(object):
    def db(self, res_data):
        # print(res_data[0])
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123qwe', db='test', charset='utf8',
                                   use_unicode=True)
        # res_data['url'] = res_data['url'].decode('utf8')
        # print(res_data['url'])
        self.cursor = self.con.cursor()
        sql3 = 'insert into 2017_2018_schedule(url,schedule) values(%s,%s)'
        try:
            self.cursor.execute(sql3, (res_data[0],res_data[1]))
            self.con.commit()
            self.cursor.close()
            self.con.close()

        except Exception as e:
            print e
            self.cursor.close()
            self.con.close()


class HtmlSql2(object):
    def db(self, res_data):
        # print(res_data[0])
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123qwe', db='test', charset='utf8',
                                   use_unicode=True)
        # res_data['url'] = res_data['url'].decode('utf8')
        # print(res_data['url'])
        self.cursor = self.con.cursor()
        sql3 = 'insert into ccpc_contest(url,contest_area,school,test_writer,internet_time,live_contest,board_name) ' \
               'values(%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql3, (res_data[0], res_data[1], res_data[2], res_data[3], res_data[4],
                                       res_data[5], res_data[6]))
            self.con.commit()
            self.cursor.close()
            self.con.close()

        except Exception as e:
            print e
            self.cursor.close()
            self.con.close()

class HtmlSql3(object):
    def db(self, res_data):
        # print(res_data[0])
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123qwe', db='test', charset='utf8',
                                   use_unicode=True)
        # res_data['url'] = res_data['url'].decode('utf8')
        # print(res_data['url'])
        self.cursor = self.con.cursor()
        sql3 = 'insert into icpc_contest(url,contest_area,contest_area_url,internet_time_sign,live_time_sign,' \
               'invite_contest,board_name,board_url) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql3, (res_data[0], res_data[1],res_data[2],res_data[3],res_data[4],res_data[5],
                                       res_data[6], res_data[7]))
            self.con.commit()
            self.cursor.close()
            self.con.close()

        except Exception as e:
            print e
            self.cursor.close()
            self.con.close()


class HtmlSql4(object):
    def db(self, res_data):
        print(res_data[0])
        self.con = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123qwe', db='test', charset='utf8',
                                   use_unicode=True)
        # res_data['url'] = res_data['url'].decode('utf8')
        # print(res_data['url'])
        self.cursor = self.con.cursor()
        sql3 = 'insert into oj_contest(url,oj_name,contest_name,contest_url,start_time,week,access) ' \
               'values(%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql3, (
            res_data[0], res_data[1], res_data[2], res_data[3], res_data[4], res_data[5], res_data[6]))
            self.con.commit()
            self.cursor.close()
            self.con.close()

        except Exception as e:
            print e
            self.cursor.close()
            self.con.close()
