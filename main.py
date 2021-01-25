from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # number of characters in our password
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)  # join just joins elements inthe sequence together with the separation btn the ''

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copies the newly generated password to a paper clip for the user to use on the website


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    username = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    if not website:  # no email was entered
        messagebox.showinfo(title='Oops', message='enter a website')
    elif not username:  # no email was entered
        messagebox.showinfo(title='Oops', message='enter an email or user name')
    elif not password:  # no password was entered
        messagebox.showinfo(title='Oops', message='enter a password')
    else:
        is_okay = messagebox.askokcancel(title='confirm entries', message=f'Please confirm the user-name and '
                                                                          f'password\n\n '
                                                                          f'user-name:  {username}\n password: {password}')
        if is_okay:
            with open('password_manager.txt', 'a+') as data_file:
                data_file.write(f'{website} | {username} | {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'sanshinehamza@gmail.com')
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = Button(text='Generate Password', highlightthickness=0, width=15, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
