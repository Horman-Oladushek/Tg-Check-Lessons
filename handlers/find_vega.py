import xlrd
def Find(exp):
    #открываем файл
    rb = xlrd.open_workbook(f'file/file_1.{exp}', formatting_info=True)

    #выбираем активный лист
    sheet = rb.sheet_by_index(0)
    lst = []
    #получаем список значений из всех записей
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    # print('Балыкин' in j for j in x for x in vals)
    for x in range(len(vals)):
        for j in range(len(vals[x])):
            if 'Балыкин' in vals[x][j]:
                lst.append(vals[x][j])
    strok = '\n'
    for j in lst:
        strok += j + '\n'
    return strok
