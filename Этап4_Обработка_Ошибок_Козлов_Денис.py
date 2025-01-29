import  json
def load_notes_from_file(filename):
    try:
        with open(filename,encoding='utf-8') as file:
            notes = file.read()
            return notes
    except FileNotFoundError:
        with open('new_file','x', encoding='utf-8'):
            return print(f'Файл {filename} не найден. Создан новый файл - new_file.txt')
    except UnicodeDecodeError:
        print(f'Ошибка при чтении файла {filename}. Проверьте его содержимое')
    except PermissionError:
        print("Отсутствуют права доступа")

load_notes_from_file()









