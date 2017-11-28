import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return
        res = requests.get(url)
        if res.status_code != 200:
            return

        return res.content

