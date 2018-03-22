import unittest

import paramunittest

from common import common

zhihu_xls = common.get_xls("zhihu_zpi.xls", "zhihu")

@paramunittest.parametrized(*zhihu_xls)
class Zhihu(unittest.TestCase):
    def setParameters(self, case_name, url, data, method, headers):
        self.case_name = str(case_name)
        self.url = url
        self.data = data
        self.method = method
        self.headers = headers

    def description(self):
        self.case_name

    def setUp(self):
        print('知乎api测试开始')

    def testZhihu(self):
        self.url

