import os

file_path = 'assets/finished_file.xlsx'

if os.path.isfile(file_path):
    os.remove(file_path)
    print('Success')
else:
    print("File doesn't exist")