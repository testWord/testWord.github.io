__author__ = '张伟伟'
from FileList import FileTest
from ReadTest import ReadTest
class MainFilePath:
    FilePath = FileTest()
    Number = ReadTest()
    for i in range(3,11):
        FilePath.testMap("root/admin",1,10,Number.read_excel(i,8),Number.read_excel(i,7),Number.read_excel(i,6))




