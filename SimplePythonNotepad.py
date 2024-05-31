import time, os, random


def clear():
    return os.system('clear')

def print_notes():
    for number, note in note_list.items():
        print(f"{number}. {note}")

def text_color(color):
    colors = {'BLACK' : '\033[30m',
            'RED' : '\033[31m',
            'GREEN' : '\033[32m',
            'YELLOW' : '\033[33m',
            'BLUE' : '\033[34m',
            'MAGENTA' : '\033[35m',
            'CYAN' : '\033[36m',
            'LIGHT_GRAY' : '\033[37m',
            'DARK_GRAY' : '\033[90m',
            'BRIGHT_RED' : '\033[91m',
            'BRIGHT_GREEN' : '\033[92m',
            'BRIGHT_YELLOW' : '\033[93m',
            'BRIGHT_BLUE' : '\033[94m',
            'BRIGHT_MAGENTA' : '\033[95m',
            'BRIGHT_CYAN' : '\033[96m',
            'WHITE' : '\033[97m',
            'RESET' : '\033[0m'}
    return colors.get(color.upper(), '\033[0m')

def create_note(note_list):
    note_number = len(note_list) + 1
    note = input("Please enter your note: ")
    note_list[note_number] = note

def display_menu():
    title = f"{text_color('BRIGHT_RED')}LEE'S NOTEBOOK"
    second_title = f"{text_color('BRIGHT_GREEN')}ADD, REMOVE and EDIT NOTES"
    option_one = f"{text_color('BRIGHT_BLUE')}Option 1: Add a note"
    option_two = f"{text_color('BRIGHT_BLUE')}Option 2: Edit a note"
    option_three = f"{text_color('BRIGHT_BLUE')}Option 3: Delete a note"
    border_top = f"{text_color('YELLOW')}------------------------"
    border_bottom = f"{text_color('BRIGHT_CYAN')}------------------------"

    print(f"{title:^35}")
    time.sleep(0.5)
    print(f"{second_title:^35}")
    print("")
    time.sleep(0.5)
    print(f"{border_top:^35}")
    print(f"{option_one:^35}")
    time.sleep(0.5)
    print(f"{option_two:^35}")
    time.sleep(0.5)
    print(f"{option_three:^35}")
    print(f"{border_top:^35}")
    time.sleep(0.5)
    print("")
    print(f"{border_bottom:^35}")
    print("Notes:")

    print_notes()

    print(f"{border_bottom:^35}")

note_list = {}
while True:
    clear()
    display_menu()
    option = input("Choose an option (1-3) or 'q' to quit: ").strip().lower()
    if option == "1":
        clear()
        create_note(note_list)
    elif option == "2":
        clear()
        print_notes()
        note_number = int(input("What note would you like to edit? "))
        if note_number in note_list:
            print("You are editing the following note:")
            print(f"{note_list[note_number]}")
            new_note = input("Enter your new note.. \n")
            note_list[note_number] = new_note
        continue
    elif option == "3":
        clear()
        print_notes()
        note_number = int(input("What note would you like to delete? "))
        if note_number in note_list:
            print("You are deleting the following note:")
            time.sleep(0.5)
            print(f"{note_list[note_number]}")
            delete_note = input("Are you sure? (yes/no) ").lower()
            if delete_note == "yes":
                del note_list[note_number]    
            else:
                continue
        continue
    else:
        break
    
