import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain:
    def __init__(self):
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        n = 1
        while self.urls.has_new_url() and n < 2:
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_data(new_data)
            n = n + 1
        self.outputer.output_disk()


if __name__ == "__main__":
    root_url = "http://www.tuku.cn/bizhi/class17_page1.aspx"
    main = SpiderMain()
    main.craw(root_url)
