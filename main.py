import os, shutil
while True:
    do = input('что желаете сделать?')
    if do == 'создать папку':
        try:
            os.mkdir(input('введите название папки'))
        except:
            pass
    if do == 'удалить (файл/папку)':
        file_or_dir = input('введите название папки или файла')
        try:
            action = os.remove(file_or_dir) if os.path.isfile(file_or_dir) else os.rmdir(file_or_dir)
            action
        except:
            pass
    if do == 'копировать (файл/папку)':
        src = input('введите название папки/файла')
        dst = input('новое название папки/файла')
        try:
            action = shutil.copyfile(src, dst) if os.path.isfile(src) else shutil.copytree(src, dst)
            action
        except:
            pass
    if do == 'просмотр содержимого рабочей директории':
        print(os.listdir())
    if do == 'посмотреть только папки':
        print([item for item in os.listdir() if os.path.isdir(item)])
    if do == 'посмотреть только файлы':
        print([item for item in os.listdir() if os.path.isfile(item)])
    if do == 'сохранить содержимое рабочей директории в файл':
        with open('listdir.txt', 'w') as f:
            f.write('files: ' + ', '.join([item for item in os.listdir() if os.path.isfile(item)]))
            f.write('\ndirs: ' + ', '.join([item for item in os.listdir() if os.path.isdir(item)]))
    if do == 'просмотр информации об операционной системе':
        print(os.uname())
    if do == 'создатель программы':
        print('this program is created by amirov sergey nemu.haibane@gmail.com')
    if do == 'смена рабочей директории':
        os.chdir(input('введите полный /home/user/... или относительный user/my/... путь'))
    if do == 'выход':
        break