# coding:utf8
import url_manager, html_downloader, html_parser4, html_outputer
import traceback

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser1 = html_parser4.HtmlParser1()
        self.parser2 = html_parser4.HtmlParser2()
        self.parser3 = html_parser4.HtmlParser3()
        self.parser4 = html_parser4.HtmlParser4()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self, root_url):  # 爬虫的调度程序
        count = 1 # 记录当前爬取的Url
        self.urls.add_new_url(root_url1)
        while self.urls.has_new_url():  # url管理器中有待爬取的Url时
            try:    # 有的网页无要爬取内容
                new_url = self.urls.get_new_url()   # 获取一个
                print 'craw %d : %s ' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载页面，结果存储
                new_urls, new_data = self.parser1.parse(new_url, html_cont)  # 解析器，得到新的Url列表以及新的数据
                self.urls.add_new_urls(new_urls)    # 添加进Url管理器（批量）
                self.outputer.collect_data(new_data)  # 收集数据

                if count == 1:
                    break
                count = count + 1
            except Exception as e:
                traceback.print_exc()
                print 'craw failed'
        self.outputer.output_html()

        count = 1  # 记录当前爬取的Url
        self.urls.add_new_url(root_url2)
        while self.urls.has_new_url():  # url管理器中有待爬取的Url时
            try:  # 有的网页无要爬取内容
                new_url = self.urls.get_new_url()  # 获取一个
                print 'craw %d : %s ' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载页面，结果存储
                new_urls, new_data = self.parser2.parse(new_url, html_cont)  # 解析器，得到新的Url列表以及新的数据
                self.urls.add_new_urls(new_urls)  # 添加进Url管理器（批量）
                self.outputer.collect_data(new_data)  # 收集数据

                if count == 1:
                    break
                count = count + 1
            except Exception as e:
                traceback.print_exc()
                print 'craw failed'
        self.outputer.output_html()

        count = 1
        self.urls.add_new_url(root_url3)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s" % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser3.parse(new_url, html_cont)
                #self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if (count == 1):
                    break;
                count = count + 1
            except Exception, e:
                traceback.print_exc()
                print "craw failed"

        count = 1  # 记录当前爬取的Url
        self.urls.add_new_url(root_url4)
        while self.urls.has_new_url():  # url管理器中有待爬取的Url时
            try:  # 有的网页无要爬取内容
                new_url = self.urls.get_new_url()  # 获取一个
                print 'craw %d : %s ' % (count, new_url)
                html_cont = self.downloader.download(new_url)  # 下载页面，结果存储
                # print(html_cont)
                new_urls, new_data = self.parser4.parse(new_url, html_cont)  # 解析器，得到新的Url列表以及新的数据
                print(new_data)
                self.urls.add_new_urls(new_urls)  # 添加进Url管理器（批量）
                self.outputer.collect_data(new_data)  # 收集数据
                # self.sql.db(new_data)

                if count == 1:
                    break
                count = count + 1
            except Exception as e:
                traceback.print_exc()
                print 'craw failed'

if __name__ == "__main__":
    root_url1 = "http://www.usaco.org/"
    root_url2 = "http://acmicpc.info/archives/2119"
    root_url3 = 'http://acmicpc.info/'
    root_url4 = "http://acmicpc.info/archives/224"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url1)
