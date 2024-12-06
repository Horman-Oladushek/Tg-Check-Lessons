import xlrd, xlwt
import os
from database.repo import Id_UsersRepo
def Find(username):
    #открываем файл
    file_path = 'file/old.xls'
    if not os.path.exists(file_path):
        # Если файла нет, создаем его
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('Лист 1')
        wb.save(file_path)

    rb_old = xlrd.open_workbook(f'file/old.xls', formatting_info=True)
    rb_new = xlrd.open_workbook(f'file/new.xls', formatting_info=True)

    #выбираем активный лист
    sheet_old = rb_old.sheet_by_index(0)
    sheet_net = rb_new.sheet_by_index(0)
    #получаем список значений из всех записей
    vals_old = [sheet_old.row_values(rownum) for rownum in range(sheet_old.nrows)]
    vals_new = [sheet_net.row_values(rownum) for rownum in range(sheet_net.nrows)]
    flag = False
    for i in range(len(vals_new)):
        try:
            if vals_old[i] != vals_new[i]:
                flag = True
        except Exception:
            flag = True
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('Лист 1')
    for i, row in enumerate(vals_new):
        for j, value in enumerate(row):
            sheet.write(i, j, value)
    wb.save('file/old.xls')

    slov = {}
    if flag is False:
        for user in Id_UsersRepo.get_all():
            if user.telegram_id == str(username):
                for x in range(len(vals_new)):
                    for j in range(len(vals_new[x])):
                        if user.surname in vals_new[x][j]:
                            if user.telegram_id not in slov:
                                slov[user.telegram_id] = '\nГруппа: ' + vals_new[0][j] + vals_new[x][j] + '\n'
                            else:
                                slov[user.telegram_id] = str(slov[user.telegram_id]) + '\nГруппа: ' + vals_new[0][j] + vals_new[x][j] + '\n'
        return f'Расписание не изменялось, ваше расписание: \n{slov.get(str(username))}'
    elif flag is True:
        for user in Id_UsersRepo.get_all():
            for x in range(len(vals_new)):
                for j in range(len(vals_new[x])):
                    if user.surname in vals_new[x][j]:
                        if user.telegram_id not in slov:
                            slov[user.telegram_id] = '\nГруппа: ' + vals_new[0][j] + vals_new[x][j] + '\n'
                        else:
                            slov[user.telegram_id] = str(slov[user.telegram_id]) + '\nГруппа: ' + vals_new[0][j] + vals_new[x][j] + '\n'

    strok = '\n'
    end = {}
    for telegram_id, text in slov.items():
        strok += text + '\n'
        
        end[telegram_id] = text
    return end
