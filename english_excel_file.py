import openpyxl as xl
import random

class EnglishExcel:
    def __init__(self, day, start_row, end_row):
        self.workbook = xl.load_workbook('E:\영단어.xlsx')

        self.day = "Day " + str(day)
        self.sheet = self.workbook[self.day]

        self.start_row = 2
        self.end_row = self.sheet.max_row

        self.rows = list(range(start_row, end_row+1))
        random.shuffle(self.rows)

        ''' TEST Code
        for self.row in self.rows:
            print("영단어 : ", self.cell_data_func(self.row, 1), sep='')
            print("뜻 : ", self.cell_data_func(self.row, 2), sep='')
            self.find_merged_cell(self.row)
        '''

    def cell_data_func(self, func_row, func_column):
        # row, column 값을 입력받아 해당 위치의 데이터를 반환해주는 함수
        return self.sheet[chr(64+func_column)+str(func_row)].value

    def find_merged_cell(self, func_row):
        # 병합된 셀의 뜻을 찾아주는 함수
        global rows
        func_row += 1

        if self.cell_data_func(func_row, 1) == None:
            print("뜻 : ", self.cell_data_func(func_row, 2), sep='')
            del self.rows[self.rows.index(func_row)]
            self.find_merged_cell(func_row)

test_class = EnglishExcel(11, 2, 5)