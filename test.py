import os
import unittest

import requests
import urllib3
import time
# 禁用安全请求警告
from urllib3.exceptions import InsecureRequestWarning
#项目参数设置
prj_path = 'F:\workspace\ZhihuApiTest\ZhihuApiTest'
#测试报告路径
report_path = os.path.join(prj_path, 'report', 'testReport')
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# r = urllib3.PoolManager()
# res = r.request('GET', 'https://news-at.zhihu.com/api/4/news/latest')
# print(res.data)
# r = requests.get('https://news-at.zhihu.com/api/4/news/latest')
# print(r.text)
from common.HTMLTestRunner import HTMLTestRunner
def run():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = urllib3.PoolManager()
    res = r.request('GET', 'https://news-at.zhihu.com/api/4/news/latest')
    print(res.data)
    test_dir = './testCase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title=u'测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)

        time.sleep(3)
    f.close()

if __name__ == "__main__":
    run()