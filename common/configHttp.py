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

    def set_method(self, method):
        self.method = method

    def set_headers(self, headers):
        self.headers = headers

    def get(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            return response
        except TimeoutError:
            print("Time out----get")
            return None

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data)
            return response
        except TimeoutError:
            print("Time out----post")
            return None

if __name__ == "__main__":
    print("ConfigHTTP")



