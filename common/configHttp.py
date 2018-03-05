import requests
class ConfigHttp:
    # url, data, method, headers
    def __init__(self):
        self.url = {}
        self.data = {}
        self.method = {}
        self.headers = {}

    def set_url(self,url):
        self.url = url

    def set_data(self,data):
        self.data = data

    def set_method(self,method):
        self.method = method

    def set_headers(self,headers):
        self.headers = headers

    def get(self):
        try:
            response = requests.get(self.url,headers = self.headers,)

