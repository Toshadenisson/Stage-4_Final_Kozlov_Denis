import  json
notes = {"username": "А123667лексей", "title": "Список покупок","content": "Купить продукты","status": "новая",
         "created_date": "27-11-2024","issue_date": "30-11-2024"}

def save_notes_json(notes,filename):

    with open(filename,'w',encoding='utf-8') as file:
        try:
            res = json.dump(notes,file,indent=4,ensure_ascii=False)
        except AttributeError:
            info = json.dumps(notes,indent=4,ensure_ascii=False)
            res = file.write(info)
            print(res)
            return res


save_notes_json(notes,filename='errr.json')