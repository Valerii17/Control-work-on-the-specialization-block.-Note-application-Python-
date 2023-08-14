import functions

def main():
    global notes
    notes = functions.load_notes()
    
    while True:
        command = input("Введите команду (add, edit, delete, filter, list, quit): ")
        
        if command == "add":
            functions.add_note()
        elif command == "edit":
            functions.edit_note()
        elif command == "delete":
            functions.delete_note()
        elif command == "filter":
            functions.filter_notes_by_date()
        elif command == "list":
            functions.print_all_notes()
        elif command == "quit":
            break
        else:
            print("Неверная команда")
            
if __name__ == "__main__":
    main()