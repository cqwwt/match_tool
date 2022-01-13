# -*- coding:utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import os
import pandas as pd

# 导入所画的界面

# 自定义类
from table import Ui_MainWindow


class Tables(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 运行数据读取函数
        self.setupUi(self)
        # 运行数据读取函数
        self.dataprocess()
        # 运行tableWidget初始化函数
        self.initialize()
        # 运行按钮的点击事件
        self.saveButton.clicked.connect(self.save)

    # 定义表格的初始化参数
    def initialize(self):
        # 设置表格行数和列数
        self.tableWidget.setRowCount(len(self.rows))
        self.tableWidget.setColumnCount(len(self.columns))
        # 设置表格的列标签
        self.tableWidget.setHorizontalHeaderLabels(self.columns)
        # 重新设置表格区域的大小
        self.tableWidget.setGeometry(QtCore.QRect(220, 120, 1000, 800))
        # 将数据显示在表格中
        for i in range(len(self.rows)):
            for j in range(len(self.columns)):
                data = QTableWidgetItem(str(self.df.iloc[i][j]))
                self.tableWidget.setItem(i, j, data)
        # 列宽随着内容调整
        self.tableWidget.resizeColumnsToContents()
        # 行宽随着内容调整
        self.tableWidget.resizeRowsToContents()
        # 表格颜色交错显示
        self.tableWidget.setAlternatingRowColors(True)
        # 将表格中单元格改变时，触发tableChange事件
        self.tableWidget.itemChanged.connect(self.tableChange)

    # 当表格的内容改变时获取内容
    def tableChange(self, item):
        text = item.text()
        itemrow = item.row()
        itemcol = item.column()
        self.df.iloc[[itemrow], [itemcol]] = text

    # 数据读取
    def dataprocess(self):
        save_finalData = self.textEdit_8.toPlainText()
        self.df = pd.read_excel('/Users/gregorycui/Desktop/untitled folder/匹配表.xlsx')

        #self.df = pd.read_excel(save_finalData +'/匹配表.xlsx')
        # 获得数据的行标签和列标签
        self.columns = self.df.columns
        self.rows = self.df.index

    # 保存数据
    def save(self):
        #save_finalData = self.textEdit_8.toPlainText()
        #print(save_finalData)
        self.df.to_excel('/Users/gregorycui/Desktop/untitled folder/匹配表.xlsx', index=False)
        #self.df.to_excel(save_finalData + '/匹配表.xlsx', index=False)




#运行界面
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tables = Tables()
    tables.show()
    sys.exit(app.exec_())