import xlrd
from database.repo import Id_UsersRepo
def Find(exp):
    #открываем файл
    rb = xlrd.open_workbook(f'file/file_1.{exp}', formatting_info=True)

    #выбираем активный лист
    sheet = rb.sheet_by_index(0)
    slov = {}
    #получаем список значений из всех записей
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

    for user in Id_UsersRepo.get_all():
        for x in range(len(vals)):
            for j in range(len(vals[x])):
                if user.surname in vals[x][j]:
                    if user.telegram_id not in slov:
                        slov[user.telegram_id] = vals[x][j]
                    else:
                        slov[user.telegram_id] = str(slov[user.telegram_id]) + vals[x][j]
    strok = '\n'
    end = {}
    for telegram_id, text in slov.items():
        strok += text + '\n'
        end[telegram_id] = text
    return end
Find('xls')