import  json
import yaml

notes = {"username": "Алексей", "title": "Список покупок","content": "Купить продукты","status": "новая",
         "created_date": "27-11-2024","issue_date": "30-11-2024"}

def save_notes_to_file(notes,filename):
    with open(filename,'w',encoding='utf-8') as file:
        file.write((yaml.dump(notes,indent=4,allow_unicode=True)))
        file.write((yaml.dump(notes,indent=4,allow_unicode=True)))
    return filename
save_notes_to_file(notes,'notes.txt')








