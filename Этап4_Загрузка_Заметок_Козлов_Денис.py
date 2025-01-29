import  json
import yaml

def load_notes_from_file(filename):
    try:
        check_file = open(filename)
        if any(check_file) is False:
            return 'Указанный файл пуст!'
        else:
            check_file.close()
    except FileNotFoundError:
        return 'Такого файла не существует'
    with open(filename,'r',encoding='utf-8') as file:
        info = file.read()
        res = yaml.safe_load(info)
    return res

notes = load_notes_from_file('notes.txt')
print(notes)