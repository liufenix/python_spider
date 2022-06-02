
import requests
import json

if __name__ == '__main__':
    token = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjVmYzRkMTU2LTlhMTYtNDIyZi1iOTMxLTIzOTkwMmQ2YmM3NiJ9.t0cT7Qp8K1gPsOieWWUJ1dR2p7Xc_Ale4vdpeyb-NnjS6onjMw9QeiKeB4gLT4Tmz7_oQzTgT-iYvHqCtGzLCg"
    url = "https://www.zlib.cc/prod-api/book/book/"

    for i in range(2):

        headers = {'Authorization': token}
        req_url = url + str(i)
        resp = requests.get(req_url, headers=headers)
        if resp.status_code == 200:
            body = resp.content
            data = json.loads(body)
            print(json.loads(body))
