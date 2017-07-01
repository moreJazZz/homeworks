# -*- coding: utf-8 -*-
#
# Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.


def write_to_file(data):
    file = open('datafile.txt', 'w')
    file.write(data)
    file.close


def read_file_data():
    with open('datafile.txt', 'r') as f:
        return f.read()


write_to_file('Test message!')
a = read_file_data()
print(a)
