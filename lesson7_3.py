import os
import shutil


for target, folders, files in os.walk('my_project'):
    # Перенос первой найденной директории <templates> в <my_project/templates>
    if 'templates' in folders and not \
            os.path.exists(os.path.join(os.getcwd(), 'my_project/templates')):
        shutil.move(os.path.join(target, folders[0]), os.path.join(os.getcwd(), 'my_project'))

    # Поэлементный перенос данных из последующих директорий <templates> в <my_project/templates>
    elif 'templates' in folders:
        for target_t, folders_t, files_t in os.walk(os.path.join(target, 'templates')):

            # Перенос директорий
            for folder in folders_t:
                try:
                    shutil.move(
                        os.path.join(target_t, folder),
                        os.path.join(os.getcwd(), 'my_project/templates'))

                # Если обрабатываемая директория уже существует в <my_project/templates>, то
                # переименовываем её с постфиксом "_1" и переносим
                except:
                    folder_ren = f'{folder}_1'
                    os.rename(
                        os.path.join(target_t, folder),
                        os.path.join(target_t, folder_ren))
                    shutil.move(
                        os.path.join(target_t, folder_ren),
                        os.path.join(os.getcwd(), 'my_project/templates'))

            # Перенос файлов
            for file in files_t:
                try:
                    shutil.move(
                        os.path.join(target_t, file),
                        os.path.join(os.getcwd(), 'my_project/templates'))

                # Если обрабатываемый файл уже существует в <my_project/templates>, то
                # переименовываем его с постфиксом "_1" и переносим
                except:
                    file_ren = f'{file[:file.find(".")]}_1{file[file.find("."):]}'
                    os.rename(
                        os.path.join(target_t, file),
                        os.path.join(target_t, file_ren))
                    file = file_ren
                    shutil.move(
                        os.path.join(target_t, file),
                        os.path.join(os.getcwd(), 'my_project/templates'))

            # Удаление пустой директории <templates>
            os.rmdir(os.path.join(target, 'templates'))
