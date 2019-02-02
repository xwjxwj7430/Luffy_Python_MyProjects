f = open('file_operation.txt', mode='r+', encoding='utf-8')

f.write('alex')
f.seek(7)
f.truncate(31)

f.close()