from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- Search PASSWORD ------------------------------- #


def find_password():
    search = website_input.get().capitalize()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    else:
        if search in data:
            messagebox.showinfo(search, f"Email: {data[search]['email']}\n"
                                f"Password: {data[search]['password']}")
        else:
            messagebox.showinfo("Not Found", f" No details for {search} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get().capitalize()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#   Label
website_label = Label(text="Websites:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=24)
website_input.grid(column=1, row=1, sticky=W)

# Entries
email_input = Entry(width=52)
email_input.insert(0, "martinbobo92@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky=W)

password_input = Entry(width=24,)
password_input.grid(column=1, row=3, sticky=W)

#   Button

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1, sticky=W)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)


window.mainloop()
