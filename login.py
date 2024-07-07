import customtkinter as ctk
from run import App
import tkinter as tk

root = ctk.CTk()
root.geometry("400x400+600+300")
root.title("Авторизация")
root.resizable(False, False)

font1 = ("Arial", 18, "bold")
font2 = ("Arial", 10)
font3 = ("Arial", 14, "bold")


def ran_database_app():
    root.destroy()
    app = App()
    app.mainloop()


lg_btn = ctk.CTkButton(root, text="Войти", font=font3, command=ran_database_app)
lg_btn.place(x=150, y=250)

root.mainloop()

if __name__ == '__main__':
    pass
