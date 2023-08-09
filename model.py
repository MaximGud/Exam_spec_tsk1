import json
from datetime import datetime
import text

notes = []
path = 'notes.json'
note={}

def add_note():
	
	global note 
	note = {}
	#загружаем список словаерей(заметок)
	notes = load_notes()
	#определяем новый id исходя из максимального уже созданного
	max_id = None
	for note in notes:
		if max_id is None or note['id'] > max_id:
			max_id = note['id']
	note['id'] = max_id + 1 

	note['title'] = input(text.input_title)
	note['body'] = input(text.input_body)
	date = datetime.now()
	note['date'] = date.strftime('%Y-%m-%d %H:%M:%S')
	print("--------------------------------------")
	print(text.create_successful)
	print(f"Вы создали заметку: {note}\nЧтобы сохранить данные, перейдите к пункту 2.")
	

# Функция для сохранения заметки в формате json
def save_note(path, note):
			f = open(path, 'a+',encoding='utf-8')
			#сначала удаляем последний символ файла json, скобку ], чтобы добавить новое значение
			f.seek(0,2)                 # конец файла
			size=f.tell()               # размер файла
			f.truncate(size-1)          # сокращаем файл на 1 символ
			f.write(',')								#ставим запятую послу послденего значения
			json.dump(note, f)    			#вставляем новые данные
			f.write(']')								#закрываем файл json
			f.close()
			print("--------------------------------------")
			print(text.save_successful)

	
	
# Функция загрузки словаря из файла json
def load_notes():
	with open('notes.json','r',encoding='utf-8') as f:
		notes = json.load(f)
	return notes

# Функция чтения всех заметок
def print_notes(notes: dict[int,str,str,datetime]):
	print("--------------------------------------")
	print(text.notes_list)
	if notes:
		for note in notes:
			print(f'ID записи:"{note.get("id")}"; Заголовок: "{note.get("title")}"; Текст заметки: "{note.get("body")}"; Дата и время: {note.get("date")}')
	else: print(text.notes_empty)

# Редактирование заметки
def edit_note():
	
	# Получение id от пользователя
	id = int(input(text.input_id))
	#загружаем список словаерей(заметок)
	notes = load_notes()
	note_data={}
	# находим заметку по id
	for note in notes:
		if note['id'] == id:
			#удаляем в списке указанный словарь по id
			notes.remove(note)
			# Вводим новые данные
			note_data['id'] = int(id)
			note_data['title'] = input(text.input_new_title)
			note_data['body'] = input(text.input_new_body)
			date = datetime.now()
			note_data['date'] = date.strftime('%Y-%m-%d %H:%M:%S')
			#вставляем в список словарей новые словарь(заметку)
			notes.insert(id-1, note_data)
			# Записываем новые данные в файл
			with open(path, "w",encoding='utf-8') as f:
				f.write(json.dumps(notes))
			print("--------------------------------------")
			print(text.change_successful)
		else: pass
		
def delete_note():
	id = int(input(text.input_id))
	#загружаем спиcок из файла
	notes = load_notes()
	#получаем данные словаря по id
	for note in notes:
		if note['id'] == id:
			#удаляем из списка notes данные указанного id словаря
			notes.remove(note)
			#записываем новые данные в файл
			with open(path, "w",encoding='utf-8') as f:
				f.write(json.dumps(notes))
			print("--------------------------------------")
			print(text.delete_successful)
		else: pass
	



