# coding:utf8
import re
import urlparse
from string import strip
from bs4 import BeautifulSoup
import html_sql4
from lxml import etree


class HtmlParser1(object):
    def __init__(self):
        self.sql = html_sql4.HtmlSql1()
    def _get_new_urls(self, page_url, soup):    # 获取页面中所有其他词条的Url
        new_urls = set()
        return new_urls

    def _get_new_data(self, page_url, soup,html):  # 解析数据 title summery
        # url放入数据中，便于后续使用
        # print(soup)
        res_data = [[] for i in range(2)]
        res_data[0]=page_url
        # print(soup)
        content = soup.find_all('div', class_="panel")[9]
        # print content.find('h2')
        tips = content.get_text().split('\n')
        for tip in tips:
            tip = tip.replace(' ', '')
            res_data[0] = page_url
            res_data[1]=tip
            # print tip
            self.sql.db(res_data)
        res_data = tips
        return res_data

    def parse(self, page_url, html_cont):  # 从cont中解析出两个数据，新的url列表和数据
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8') # 将cont加载近soup
        # 两个链接
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup,html_cont)
        return new_urls, new_data

class HtmlParser3():
    def __init__(self):
        self.sql = html_sql4.HtmlSql3()
    def _get_new_urls(self, page_url, soup):

        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"http://acm\.\w+\.edu.cn/"))
        # print links
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

        res_data = [[] for i in range(8)]
        one_node = []
        two_node = []
        three_node = []
        four_node = []
        five_node = []

        # url放入数据中，便于后续使用
        res_data[0] = page_url
        table = soup.find_all('table')[0]
        # print t.get_text()
        count=0
        body = table.find('tbody').find_all('tr')
        for cl in body:
            count+=1
            if count==1:
                count+=1
                continue
            th = cl.find_all('td')
            res_data[1] = th[0].get_text()
            a=th[0].find('a')
            if th[0].find('a')!=None:
                res_data[2] = a['href']
            else:
                res_data[2] =None
            res_data[3] = th[1].get_text()
            res_data[4] = th[2].get_text()
            res_data[5] = th[3].get_text()
            res_data[6] = th[4].get_text()
            a2=th[4].find('a')
            if a2!=None:
                res_data[7]=a['href']
            else:
                res_data[7]=None
            self.sql.db(res_data)
            # res_data[6] = th[5].get_text()
            # print(res_data)
        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

class HtmlParser2(object):
    def __init__(self):
        self.sql2 = html_sql4.HtmlSql2()
    def _get_new_urls(self, page_url, soup):    # 获取页面中所有其他词条的Url
        new_urls = set()
        return new_urls

    def _get_new_data(self, page_url, soup,html):  # 解析数据 title summery
        # url放入数据中，便于后续使用
        res_data = [[] for i in range(8)]
        res_data[0] = page_url
        # print(soup)
        table = soup.find_all('table')[1]
        head = table.find('thead').find_all('th')
        for th in head:
            print th.get_text()
        body = table.find('tbody').find_all('tr')
        for cl in body:
            th = cl.find_all('td')
            res_data[1] = th[0].get_text()
            res_data[2] = th[1].get_text()
            res_data[3] = th[2].get_text()
            res_data[4] = th[3].get_text()
            res_data[5] = th[4].get_text()
            res_data[6] = th[5].get_text()
            # if th[5].find('a')!=None:
            #     res_data[7] = None
            # else:
            #     res_data[7]=None
            self.sql2.db(res_data)
            # for t in th:
            #     i=0
            #     print t.get_text().encode("utf8")
            #     res_data[i++]=

        res_data = head + body
        return res_data

    def parse(self, page_url, html_cont):  # 从cont中解析出两个数据，新的url列表和数据
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8') # 将cont加载近soup
        # 两个链接
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup,html_cont)
        return new_urls, new_data

class HtmlParser4(object):
    def __init__(self):
        self.sql = html_sql4.HtmlSql4()

    def _get_new_urls(self, page_url, soup):    # 获取页面中所有其他词条的Url
        new_urls = set()
        # 获取所有的连接 /view/123.htm
        links = soup.find_all('a', href=re.compile(r"http://acmicpc.info/archives/\d+$"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)  # 按照page_url的格式，拼接成完全的url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):  # 解析数据 title summery
        res_data = [[] for i in range(7)]
        oj_node = []
        name_node = []
        start_node = []
        week_node = []
        access_node = []
        # url放入数据中，便于后续使用
        res_data[0] = page_url
        # print(soup)
        # tables = soup.find_all('div', class_="dataTables_wrapper")
        table = soup.find('table',class_="wp-table-reloaded wp-table-reloaded-id-1")
        # print(table)
        #coming
        tips = table.find_all('tr')
        # print(len(tips))
        count = 0
        for row in tips:
            count+=1
            # print(count)
            cols = row.find_all('td')
            # print(len(cols))
            if len(cols)==0:
                count-=1
                continue
            a=cols[1].find('a')
            # print a
            oj_node.append(cols[0].get_text())
            # print name_node
            name_node.append(cols[1].get_text())
            # print cols[1].get_text()
            start_node.append(cols[2].get_text())
            # print cols[2].get_text()
            week_node.append(cols[3].get_text())
            # print cols[3].get_text()
            access_node.append(cols[4].get_text())
            res_data[1] = cols[0].get_text()
            res_data[2] = cols[1].get_text()
            res_data[3]=a['href']
            res_data[4] = cols[2].get_text()
            res_data[5] = cols[3].get_text()
            res_data[6]=cols[4].get_text()
            self.sql.db(res_data)
        return res_data

    def parse(self, page_url, html_cont):  # 从cont中解析出两个数据，新的url列表和数据
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8') # 将cont加载近soup
        # 两个链接
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data