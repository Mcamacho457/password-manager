import tkinter
import customtkinter

app = customtkinter.CTk()

app.geometry("700x500")
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")

app.title("Password Manager 2.0")

left_frame = customtkinter.CTkFrame(master=app, fg_color="light gray")
left_frame.pack(side="left", fill="both",expand=True)

right_frame = customtkinter.CTkFrame(master=app, fg_color="white")
right_frame.pack(side="right", fill="both", expand=True)

startLabel = customtkinter.CTkLabel(master=right_frame, text="Welcome to Password Manager 2.0!", font=("Oswald",24),text_color="#C247EA",height=200)
startLabel.pack(side="top")

#startLabel2 = CTkLabel(master=right_frame, text)
usernameLabel = customtkinter.CTkLabel(master=right_frame, text="Username/Email:",font=("Oswald",18),text_color="#C247EA")
usernameLabel.pack(side="top")

"""frame1 = CTkFrame(master = app, fg_color = ("#C6CED8", "#080808"), border_color= ("#586B78", "#586B78"), width = 400, height = 200, border_width=2, corner_radius=20)
frame1.pack()"""








app.mainloop()