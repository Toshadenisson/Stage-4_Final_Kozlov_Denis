import  json

import yaml

notes = {"username": "А1лексей", "title": "Список покупок","content": "Купить продукты","status": "новая",
         "created_date": "27-11-2024","issue_date": "30-11-2024"}
def  append_notes_to_file(notes, filename):
    try:
        file_check = open(filename)
        file_check.close()
    except FileNotFoundError:
        file_check = open(filename,'x',encoding='utf-8')
        file_check.close()
        with open(filename,'a', encoding='utf-8') as file:
            file.write(yaml.dump(notes,indent=4,allow_unicode=True))
            file.write(yaml.dump(notes,indent=4,allow_unicode=True))
        return filename
append_notes_to_file(notes,'notes.txt')













