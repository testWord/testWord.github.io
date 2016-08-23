__author__ = '张伟伟'

import xlrd

# 读取绝对路径下的excel文档下的数据

class ReadTest:
    workbook = xlrd.open_workbook('E:\\test.xls')

    def read_excel(self,col,row):


        # print(self.workbook.sheet_names())
    # [u'sheet1', u'sheet2'])
        sheet2_name = self.workbook.sheet_names()[0]

  # 根据sheet索引或者名称获取sheet内容
        sheet2 = self.workbook.sheet_by_index(0)
  # sheet索引从0开始
        sheet2 = self.workbook.sheet_by_name('sheet1')

  # sheet的名称，行数，列数
  #       print (sheet2.name,sheet2.nrows,sheet2.ncols)
  # 获取整行和整列的值（数组）
  # rows = sheet2.row_values(row)
  # 获取第四行内容
  # cols = sheet2.col_values(col)
        vlause =sheet2.cell_value(col,row)
        return vlause


