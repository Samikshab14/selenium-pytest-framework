import xlrd


def read_excel_data(path, sheetname):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    header = next(rows)

    data_ = {}
    for ele in rows:
        data_[ele[0].value] = ele[1].value

    return data_
print(read_excel_data(r'C:\Users\Samiksha Bandgar\PycharmProjects\Apollo_Capgemini\Apollo_Capgemini\test_data\details.xls',"Data"))