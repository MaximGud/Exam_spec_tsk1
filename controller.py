import view
import model


def start():
	while True:
		choice = view.main_menu()
		
		match choice:
			case 1:
				model.add_note()
			case 2:
				model.save_note('notes.json', model.note)
				pass
			case 3:
				model.print_notes(model.load_notes())
				pass
			case 4:
				model.edit_note()
				pass
			case 5:
				model.delete_note()
				pass
			case 6:
				break
			