import requests
import urllib3
# 禁用安全请求警告
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
r = urllib3.PoolManager()
res = r.request('GET', 'https://news-at.zhihu.com/api/4/news/latest')
print(res.data)
# r = requests.get('https://news-at.zhihu.com/api/4/news/latest')
# print(r.text)