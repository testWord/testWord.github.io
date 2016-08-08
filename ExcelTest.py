
import xlwt

workbook = xlwt.Workbook()

# 注意Workbook的开头W要大写
sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
def ExlWrit(row,testResult):
#向sheet页中写入数据
    sheet1.write(row,0,testResult)
    """
    #-----------使用样式-----------------------------------
    #初始化样式
    style = xlwt.XFStyle()
    #为样式创建字体
    font = xlwt.Font()
    font.name = 'Times New Roman'
    font.bold = True
    #设置样式的字体
    style.font = font
    #使用样式
    sheet.write(0,1,'some bold Times text',style)
    """
#保存该excel文件,有同名文件时直接覆盖
    workbook.save('E:\\test.xls')