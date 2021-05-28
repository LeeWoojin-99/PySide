import openpyxl as xl
import random

def cell_data_func(func_row, func_column):
    # row, column 값을 입력받아 해당 위치의 데이터를 반환해주는 함수
    return sheet[chr(64+func_column)+str(func_row)].value

def find_merged_cell(func_row):
    # 병합된 셀의 뜻을 찾아주는 함수
    global rows
    func_row += 1

    if cell_data_func(func_row, 1) == None:
        print("뜻 : ", cell_data_func(func_row, 2), sep='')
        del rows[rows.index(func_row)]
        find_merged_cell(func_row)

workbook = xl.load_workbook('E:\영단어.xlsx')

#day = input("Day를 입력해주세요 : ")
#start_row, end_row = map(int, input("시작 행과 끝 행을 적어주세요 : "))
day = "11"
day = "Day "+day

sheet = workbook[day]

start_row = 2
end_row = sheet.max_row
end_row = 3

rows = list(range(start_row, end_row+1))
#random.shuffle(rows)

'''
for row in rows:
    print("영단어 : ", cell_data_func(row, 1), sep='')
    print("뜻 : ", cell_data_func(row, 2), sep='')
    find_merged_cell(row)
'''