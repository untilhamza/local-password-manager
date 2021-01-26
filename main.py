from tkinter import *
from tkinter import messagebox
import pyperclip
import json
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
    password = ''.join(password_list)  # join just joins elements in the sequence together with the separation btn
    # the ''

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copies the newly generated password to a paper clip for the user to use on the website


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    username = email_entry.get()
    website = website_entry.get().title()
    password = password_entry.get()

    if not website:  # no email was entered
        messagebox.showinfo(title='Oops', message='enter a website')
    elif not username:  # no email was entered
        messagebox.showinfo(title='Oops', message='enter an email or user name')
    elif not password:  # no password was entered
        messagebox.showinfo(title='Oops', message='enter a password')
    else:
        is_okay = messagebox.askokcancel(title=f'confirm entries for {website}',
                                         message=f'Please confirm the user-name and '
                                                 f'password\n\n user-name:  {username}\n '
                                                 f'password: {password}')
        if is_okay:
            # create the data to be entered into the json file
            new_data = {
                website: {  # top level key is website for searching our entries
                    'email': username,
                    'password': password
                }
            }
            try:
                with open('data.json', 'r') as data_file:
                    # read old data
                    data = json.load(data_file)  # do only one thing here that can fail so you catch it
            except FileNotFoundError:  # file not yet created, we shall create it now and dump our data
                with open("data.json", "w") as data_file:  # create this file and dump that new data (first entry)
                    json.dump(new_data, data_file, indent=4)
                    # data_file.write(f'{website} | {username} | {password}\n')
            else:  # file exists so we read its data and updated that data, so now we must dump it there
                with open('data.json', 'w') as data_file:
                    data.update(new_data)  # add to the dictionary that we got from the json file
                    json.dump(data, data_file, indent=4)
            finally:  # clear the entry fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title='Password saved', message='Your entries have been saved successfully')


def find_password():
    if not website_entry.get():  # if no website was entered to search
        messagebox.showinfo(title='website not entered', message='Enter a website to search password')
    else:
        try: # makes sure the file of passwords actually exists
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title='Password Vault Empty', message='Store some passwords first')
        else:
            site = website_entry.get().title()
            print(site)
            try:  # check if site is in the dictionary return from json.load
                username = data[site]['email']
                password = data[site]['password']
            except KeyError: # the website is not in our file
                messagebox.showinfo(title='Not found', message=f'No details for {site} in vault')
            else:
                messagebox.showinfo(title=site, message=f'Username: {username} \n Password: {password}')


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

my_label = Label(text='@Hamza Works', fg='#ec4646')
my_label.grid(column=2, row=6)

# entries
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1, padx=10, pady=10)
website_entry.focus()

email_entry = Entry(width=47)
email_entry.grid(column=1, row=2, columnspan=2, padx=10, pady=10)
email_entry.insert(0, 'sanshinehamza@gmail.com')

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, columnspan=1, padx=15, pady=15)

# buttons
Search = Button(text='Search', width=13, highlightthickness=0, command=find_password)
Search.grid(column=2, row=1)

generate_password_button = Button(text='Generate Password', highlightthickness=0, width=15, command=generate_password)
generate_password_button.grid(column=2, row=3, padx=10, pady=10)

add_button = Button(text='Add', width=36, highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2, padx=10)

window.mainloop()
