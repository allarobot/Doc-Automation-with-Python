#!/Users/jayhan/VirtualEnvs/flask_py3/bin python
# -*- coding: utf-8 -*-
import xlrd
import openpyxl

fileName = ""
wb = xlrd.open_workbook(fileName)
for table in wb.sheets():
    nrows = table.nrows #行数
    for row in table.row_values():
        print("row")

