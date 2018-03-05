# -*- coding:utf-8 -*-
import sys

import os

from common import HTMLTestRunner
import time
import unittest
#项目参数设置
prj_path = 'F:\workspace\ZhihuApiTest\ZhihuApiTest'
#测试报告路径
report_path = os.path.join(prj_path, 'report', 'testReport')
def run():
    test_dir = './testCase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = report_path + '\\' + 'TestResult' + now + '.html'
    with open(reportname, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title=u'测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)
        time.sleep(3)

if __name__ == '__main__':
    run()
