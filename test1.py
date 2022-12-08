# pip install XlsxWriter
import random
import os

import pandas

# Чтение исходного файла
started_file_path = 'assets/started_file.xlsx'
data_frame = pandas.read_excel(started_file_path)


# Редактирование дата фрейма
columns = data_frame.columns.values
rows = []
frame_list = data_frame

for i in frame_list:
    for j in i:
        summand = random.uniform(-j * 0.1, j * 0.1)
        i[i.index(j)] = round(j + summand, 3)
    if i[0] / i[0] == 1.0:
        rows.append(i)
print(data_frame)
print(rows)
# Создание и запись в файл
# finished_file_path = 'assets/finished_file.xlsx'
# writer = pandas.ExcelWriter(finished_file_path, engine='xlsxwriter')
# data_frame.to_excel(writer, 'Sheet1')
# writer.save()

# Проблемы с записью новых значений