import customtkinter as ct

app = ct.CTk()
app.title("CustomTkinter")
app.geometry("300x200")

app._set_appearance_mode("dark")
app.CTkLabel(text="which type of animals you are?").pack(padx=10, pady=10)

