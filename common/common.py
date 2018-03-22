# -*-coding:utf-8 -*-
#从excel文件中读取测试用例
import os

from xlrd import open_workbook

proDir = os.path.split(os.path.realpath(__file__))[0]
def get_xls(xls_name, sheet_name):
    cls = []
    #获取xls文件的路径
    xlsPath = os.path.join(proDir, "testFile", xls_name)
    #打开xls文件
    file = open_workbook(xlsPath)
    #根据sheet_name获取sheet
    sheet = file.sheet_by_name(sheet_name)
    #获得该sheet的行数
    rows = sheet.nrows
    for i in range(rows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls
