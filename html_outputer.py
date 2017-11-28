import requests


class HtmlOutputer(object):

    def __init__(self):
        self.data = set()

    def collect_data(self, new_data):
        for dataa in new_data:
            self.data.add(dataa)

    def output_html(self):
        print(self.data)

    def output_disk(self):
        n = 1
        for img_url in self.data:
            img_res = requests.get(img_url)
            with open('imgs/'+str(n)+'.jpg', 'wb') as f:
                f.write(img_res.content)
            n = n + 1