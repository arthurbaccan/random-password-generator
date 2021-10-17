from random import randint
from tkinter import *

special_characters: list = ['!', '"', '#', '$', '%', '&', '(', ')', ',', '-', '.', '/', ':', ';', '+', '*'
                            '<', '=', '>', '?', '@', '[', ']', '_', '{', '}']
numbers: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
text_characters: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_characters: list = [special_characters, numbers, text_characters]


def generate_password(length: int = 10, numbers_allowed: bool = True, special_characters_allowed: bool = True,
                      text_allowed: bool = True):
    numbers_to_choose = [0, 1, 2]

    # don't allow the special character list if the user didn't allow special characters
    if not special_characters_allowed:
        numbers_to_choose[0] = False
    # don't allow the numbers list if the user didn't allow numbers
    if not numbers_allowed:
        numbers_to_choose[1] = False
    # don't allow the text list if the user didn't allow text characters
    if not text_allowed:
        numbers_to_choose[2] = False

    password: str = ''

    # generates the password string
    for c in range(0, length):

        chosen_number: int = randint(0, len(all_characters) - 1)
        # Tries to get an allowed list
        while type(numbers_to_choose[chosen_number]) == bool:
            chosen_number: int = randint(0, len(all_characters) - 1)
        # chooses one of the allowed lists
        chosen_list: list = all_characters[chosen_number]
        # chooses a character from the list
        chosen_character = chosen_list[randint(0, len(chosen_list) - 1)]

        password += str(chosen_character)

    print(password)
    return password


def main():
    def on_password_button_clicked():
        # the try, except and the if's bellow check if the correct password length is typed and if numbers, text
        # and special characters are allowed
        try:
            password_length = int(length_entry.get())
        except ValueError:
            password_length = 10
        if state_special_characters.get():
            special_characters_allowed = True
        else:
            special_characters_allowed = False
        if not state_numbers_allowed.get():
            numbers_allowed = False
        else:
            numbers_allowed = True
        if not state_text_allowed.get():
            text_characters_allowed = False
        else:
            text_characters_allowed = True

        if not numbers_allowed and not text_characters_allowed and not special_characters_allowed:
            return False

        password = generate_password(password_length, numbers_allowed, special_characters_allowed,text_characters_allowed)
        # updates the password label text to display the generated password
        generated_password_label['text'] = 'Generated Password: ' + str(password)

    window = Tk()
    window.geometry('400x250')
    window.title('Password Generator')
    # window.iconbitmap('lock.ico')

    state_numbers_allowed = IntVar()
    state_special_characters = IntVar()
    state_text_allowed = IntVar()

    button_height = 40
    button_width = 150

    entry_width = 50
    entry_height = 20

    generate_password_button = Button(window, text='Generate Password', command=on_password_button_clicked, fg='blue')
    generate_password_button.place(x=120, y=150, width=button_width, height=button_height)

    label_length = Label(window, text='length:', fg='black', font=('Arial Black', 17))
    label_length.place(x=30, y=100)

    length_entry = Entry(window)
    length_entry.place(x=130, y=110, width=entry_width, height=entry_height)

    special_characters_check_button = Checkbutton(window, text='Use Special Characters', font=('Arial Black', 13),
                                                  variable=state_special_characters, offvalue=0, onvalue=1)
    special_characters_check_button.place(x=30, y=70)

    numbers_check_button = Checkbutton(window, text='Use Numbers', font=('Arial Black', 13),
                                       variable=state_numbers_allowed, offvalue=0, onvalue=1)
    numbers_check_button.place(x=30, y=40)

    text_check_button = Checkbutton(window, text='Use text characters', font=('Arial Black', 13),
                                    variable=state_text_allowed, onvalue=1, offvalue=0)
    text_check_button.place(x=30, y=10)

    generated_password_label = Label(window, font=('Calibri Light', 12), text=' ', wraplength=390, justify='left')
    generated_password_label.place(x=10, y=190, width=390)

    window.mainloop()


if __name__ == '__main__':
    main()
