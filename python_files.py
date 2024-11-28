import os
import shutil

# Открытие файла open(file, mode, encoding)
# file - путь к файлу (абсалютный или относительно скрипта)
# mode - режим открытия файла
# encoding - кодировка

# Основные режимы:
    # r - чтение, r+ - режим для чтения и записи
    # w - запись с пересозданием файла
    # a - добавление в конец файла
    # b - бинарный формат (картинка, звук и т.д.)

# encoding='utf-8' - добавляется, если в тексте есть русске символы

my_file = open(file='myfile.txt', mode='w', encoding='utf-8') # файловый дискриптор <class '_io.TextIOWrapper'>
print(type(my_file))

# write - запись в файл, принимает строку
my_file.write('Python!!!\n')
text = 'Forever!!!\n'
my_file.write(text)

my_list = [' alena', 'elena!']

for item in my_list:
    my_file.write(item.strip(',! ')+'\n') # strit('') - убирает из строки лишние элементы

# names = '\n'.join(my_list)
# my_file.write(names)

# \t - табуляция
# \n - символ конца строки

# Закрытие файла, после завершения работы с ним
my_file.close()

# Открытие файла в режиме добавления в конец
my_file = open(file='myfile.txt', mode='a', encoding='utf-8')
my_file.write('Python!!!\n')
my_file.writelines(my_list) # принимает список
my_file.close()

# Открытие файла для чтения
my_file = open(file='myfile.txt', mode='r', encoding='utf-8')
text_from_file = my_file.read() # .read() считывает текст файла, возвращает строку
text_rows = text_from_file.split('\n')
print(text_from_file)
print(text_rows)

my_file.seek(0) # перемещает курсор в начало файла
text_lines = my_file.readlines() # список строк, где элементы включают \n
print(text_lines)

print('alex', 'ivanov', sep='\n') # sep меняет разделитель (по умолчанию пробел)

file_name = 'myfilenew.txt'
# Проверка существования пути
if os.path.exists(file_name):
    with open(file=file_name, mode='r', encoding='utf-8') as my_file: # файловый контекстный менеджер
        text_from_f = my_file.read()
        # файл закрывать не нужно
        # все созданные тут переменные доступны дальше в коде
else:
    print(f'{file_name} не существует')
    with open(file=file_name, mode='w', encoding='utf-8') as my_file: # файловый контекстный менеджер
        pass

# Переименование файла
file_name_new = f'new_{file_name}'
if os.path.exists(file_name):
    if not os.path.exists(file_name_new):
        os.rename(file_name, file_name_new)
        print(f'Файл {file_name} --> {file_name_new}')
    else:
        print(f'Файл {file_name_new} уже существует!')

# Удаление файла
if os.path.exists(file_name_new):
    os.remove(file_name_new)
    print(f'Файл {file_name_new} удалён')

# Создание каталога
dir_name = 'files'
if not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=True)

os.makedirs(dir_name, exist_ok=True) # exist_ok=True - не выдаст ошибку, если каталог уже существует

with open(file=f'{dir_name}/{file_name}', mode='w', encoding='utf-8') as my_file:
    pass

# Удаление каталога
# os.rmdir(dir_name) - удаление пустого каталога
shutil.rmtree(dir_name) # удаление каталога с файлами