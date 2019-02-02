import os
f_name = 'file_operation.txt'
f_new_name = 'file_operation_new.txt'

old_str = '刘亦菲'
new_srt = '张嘉倪'

f = open('file_operation.txt', mode='r', encoding='utf-8')
f_new = open('file_operation_new.txt', mode='w', encoding='utf-8')
f_new.close()
f_new = open('file_operation_new.txt', mode='a', encoding='utf-8')

for line in f:
    if old_str in line:
        new_line = line.replace(old_str, new_srt)
    else:
        new_line = line

f_new.write(new_line)

f.close()
f_new.close()

os.renames(f_name, f_new_name)