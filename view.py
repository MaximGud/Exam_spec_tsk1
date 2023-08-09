import text

def main_menu() -> int:
	print(text.main_menu)
	while True:
		choice = input(text.input_choice)	
		if choice.isdigit() and 0< int(choice)<7:
			return int(choice)
