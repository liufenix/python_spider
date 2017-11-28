import re
import urllib

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'tuji\d+\.aspx'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls



    def _get_new_data(self, url, soup):
        res_data = set()
        imgs = soup.find_all('img', src=re.compile(r'http://img.tuku.cn/(.*).jpg'))
        for img in imgs:
            res_data.add(img['src'])
        return res_data


    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls,new_data


