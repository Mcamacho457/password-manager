import tkinter as tk
from tkinter import messagebox
import customtkinter

def add():
    #asks user for username
    username = entryName.get()

    #asks user for password
    password = entryPassword.get()

    if username and password:
        with open("passwords.txt", 'a') as passwordFile:
            passwordFile.write(f"{username} {password}\n")
        messagebox.showinfo("Valid Password", "Password has been added!!")
    else:
        messagebox.showerror("Invalid Password", "Please enter a value for BOTH fields.")

def get():
    #ask user for username
    username = entryName.get()

    passwords = {}

    #checks to see if file exists
    try:
        with open("passwords.txt", 'r') as passwordFile:
            for line in passwordFile:
                i = line.split(' ')
                #sets key-value pairs for usernames and passwords
                passwords[i[0]] = i[1]
    except:
        print("Error opening file!")

    if passwords:
        for i in passwords:
            if username == i:
                mess = f"Password for {i} is {passwords[i]}\n"
                break
        else:
            mess = f"No password exists for user {username}!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "No passwords exist!")

def getall():
    passwords = {}

    try:
        with open("passwords.txt", 'r') as passwordFile:
            for line in passwordFile:
                i = line.split(' ')
                #sets key-value pairs for usernames and passwords
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!")

    if passwords:
        message = "List of passwords:\n"
        for name, password in passwords.items():
            message += f"Password for {name} is {password}\n"
        messagebox.showinfo("Passwords", message)
    else:
        messagebox.showinfo("Passwords", "No passwords are saved!")

def delete():
    username = entryName.get()

    temp_passwords = []
    
    try:
        with open("passwords.txt", 'r') as passwordFile:
            for line in passwordFile:
                i = line.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")
        
        with open("passwords.txt", 'w') as passwordFile:
            for line in temp_passwords:
                passwordFile.write(line)
            messagebox.showinfo("Complete", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")

def show_pass():
    if entryPassword.cget('show') == '*':
        entryPassword.configure(show = '')
    else:
        entryPassword.configure(show = '*')

mode = "light"
def darkMode():
    global mode
    if mode == "light":
        app._set_appearance_mode("dark")
        mode = "dark"
    else:
        app._set_appearance_mode("light")
        mode = "light"

if __name__ == "__main__":
    app = customtkinter.CTk()
    app._set_appearance_mode("Dark")

    app.geometry("560x270")
    app.title("Password Manager")

    #username block
    labelName = customtkinter.CTkLabel(app, text = "Username/email:")
    labelName.grid(row = 0, column = 0, padx = 15, pady = 15)
    entryName = customtkinter.CTkEntry(app)
    entryName.grid(row = 0, column = 1, padx = 15, pady = 15)

    #password block
    labelPassword = customtkinter.CTkLabel(app, text = "Password:")
    labelPassword.grid(row = 1, column = 0, padx = 10, pady = 5)
    entryPassword = customtkinter.CTkEntry(app, show = '*')
    entryPassword.grid(row = 1, column = 1, padx = 10, pady = 5)

    #add button
    buttonAdd = customtkinter.CTkButton(app, text = "ADD", command = add)
    buttonAdd.grid(row = 2, column = 0, padx = 15, pady = 8, sticky = "we")

    #Get Button
    buttonGet = customtkinter.CTkButton(app, text = "GET", command = get)
    buttonGet.grid(row = 2, column = 1, padx = 15, pady = 8, sticky = "we")

    #getall button
    buttonGetAll = customtkinter.CTkButton(app, text = "GET ALL", command = getall)
    buttonGetAll.grid(row = 3, column = 0, padx = 15, pady = 8, sticky = "we")

    #delete button
    buttonDelete = customtkinter.CTkButton(app, text = "DELETE", command = delete)
    buttonDelete.grid(row = 3, column = 1, padx = 15, pady = 8, sticky = "we")

    #show button
    buttonShow = customtkinter.CTkCheckBox(app, text = "Show password", command = show_pass)
    buttonShow.grid(row = 1, column = 2)

    #dark-mode button
    """buttonDark = customtkinter.CTkSwitch(app, text = "Dark Mode", command = darkMode)
    buttonDark.grid(row = 2, column = 2, padx = 15, pady = 8, sticky = "we")
"""
    app.mainloop()