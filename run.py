# pip install -r requirements.txt
import data.database as db
from data.database import db_insert_random
import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        self.geometry("810x420+600+300")
        self.title("База данных")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        font1 = ("Arial", 18, "bold")
        font2 = ("Arial", 10)
        font3 = ("Arial", 14, "bold")

        self.left_frame = ctk.CTkFrame(self, fg_color="transparent", width=250, height=360)
        self.left_frame.place(x=0, y=0)

        self.right_frame = ctk.CTkFrame(self, fg_color="transparent", width=560, height=360)
        self.right_frame.place(x=250, y=0)

        self.down_frame = ctk.CTkFrame(self, fg_color="transparent", width=810, height=60)
        self.down_frame.place(x=0, y=360)

        # left_frame
        self.lf_entry_id = ctk.CTkEntry(self.left_frame, placeholder_text="ID", width=230, height=40, font=font1)
        self.lf_entry_id.place(x=10, y=10)

        self.lf_entry_name = ctk.CTkEntry(self.left_frame, placeholder_text="Имя", width=230, height=40, font=font1)
        self.lf_entry_name.place(x=10, y=60)

        self.lf_entry_fam = ctk.CTkEntry(self.left_frame, placeholder_text="Фамилия", width=230, height=40, font=font1)
        self.lf_entry_fam.place(x=10, y=110)

        self.lf_entry_age = ctk.CTkEntry(self.left_frame, placeholder_text="Возраст", width=230, height=40, font=font1)
        self.lf_entry_age.place(x=10, y=160)

        self.lf_frame_phone = ctk.CTkEntry(self.left_frame, placeholder_text="Телефон", width=230, height=40,
                                           font=font1)
        self.lf_frame_phone.place(x=10, y=210)
        self.values = ["Менеджер", "Бухгалтер", "Юрист", "Программист", "Дизайнер", "Консультант", "Секретарь"]
        self.lf_combo_job = ctk.CTkComboBox(self.left_frame, values=self.values, width=230, height=40, font=font1,
                                            state="readonly")
        self.lf_combo_job.place(x=10, y=260)
        self.lf_combo_job.set("Менеджер")

        self.lf_combo_gender = ctk.CTkComboBox(self.left_frame, values=["Мужчина", "Женщина"], width=230, height=40,
                                               font=font1,
                                               state="readonly")
        self.lf_combo_gender.place(x=10, y=310)
        self.lf_combo_gender.set("Мужчина")
        # down_frame

        self.df_btn_add = ctk.CTkButton(self.down_frame, text="Добавить\nданные", width=123, height=40, font=font3,
                                        command=self.insert)
        self.df_btn_add.place(x=10, y=10)

        self.df_btn_del_all = ctk.CTkButton(self.down_frame, text="Новые\nданные", width=123, height=40, font=font3,
                                            command=lambda: self.clear(True))
        self.df_btn_del_all.place(x=143, y=10)

        self.df_btn_upd = ctk.CTkButton(self.down_frame, text="Обновить\nданные", width=123, height=40, font=font3,
                                        command=self.update)
        self.df_btn_upd.place(x=276, y=10)

        self.df_btn_del = ctk.CTkButton(self.down_frame, text="Удалить\nданные", width=123, height=40, font=font3,
                                        command=self.delete)
        self.df_btn_del.place(x=409, y=10)

        self.df_btn_del_all = ctk.CTkButton(self.down_frame, text="Удалить\nвсе данные", width=123, height=40,
                                            font=font3,
                                            command=self.delete_all)
        self.df_btn_del_all.place(x=542, y=10)

        self.df_btn_random = ctk.CTkButton(self.down_frame, text="Случайные\nданные", width=123, height=40, font=font3,
                                           command=self.random_insert)
        self.df_btn_random.place(x=675, y=10)

        # right_frame
        self.style = ttk.Style(self.right_frame)
        self.style.theme_use("clam")
        self.style.configure("Treeview", font=font2, foreground="#fff", background="#343638", fieldbackground="#343638")
        self.style.map("Treeview", background=[("selected", "#1f538d")])

        self.tree = ttk.Treeview(self.right_frame, height=15)
        self.tree.place(x=5, y=15)

        self.tree["columns"] = ("ID", "Имя", "Фамилия", "Возраст", "Телефон", "Должность", "Пол")

        self.tree.column("#0", width=0, stretch="NO")
        self.tree.column("ID", width=30, anchor="c")
        self.tree.column("Имя", width=80, anchor="c")
        self.tree.column("Фамилия", width=100, anchor="c")
        self.tree.column("Возраст", width=54, anchor="c")
        self.tree.column("Телефон", width=114, anchor="c")
        self.tree.column("Должность", width=87, anchor="c")
        self.tree.column("Пол", width=65, anchor="c")

        self.tree.heading("ID", text="ID", anchor="c")
        self.tree.heading("Имя", text="Имя", anchor="c")
        self.tree.heading("Фамилия", text="Фамилия", anchor="c")
        self.tree.heading("Возраст", text="Возраст", anchor="c")
        self.tree.heading("Телефон", text="Телефон", anchor="c")
        self.tree.heading("Должность", text="Должность", anchor="c")
        self.tree.heading("Пол", text="Пол", anchor="c")

        self.scrollbar_ver = ctk.CTkScrollbar(self.right_frame, height=332, command=self.tree.yview)
        self.scrollbar_ver.place(x=540, y=13)
        self.tree.configure(yscrollcommand=self.scrollbar_ver.set)

        self.select_db()

        self.tree.bind('<ButtonRelease>', self.display_data)

    def random_insert(self):
        db.db_delete_all()
        dialog = ctk.CTkInputDialog(text="Сколько записей вставить:", title="Вставка случайных данных")
        dialog.geometry("+700+400")
        text = str(dialog.get_input())
        if not text.isdigit():
            CTkMessagebox(title="Error", message="Нужно ввести число")
        else:
            db_insert_random(int(text))
            self.select_db()

    def select_db(self):
        self.tree.delete(*self.tree.get_children())
        for i in db.db_select():
            self.tree.insert("", "end", values=i[1:])

    def clear(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
        self.lf_entry_id.delete(0, "end")
        self.lf_entry_id.configure(placeholder_text="ID")
        self.lf_entry_name.delete(0, "end")
        self.lf_entry_name.configure(placeholder_text="Имя")
        self.lf_entry_fam.delete(0, "end")
        self.lf_entry_fam.configure(placeholder_text="Фамилия")
        self.lf_entry_age.delete(0, "end")
        self.lf_entry_age.configure(placeholder_text="Возраст")
        self.lf_frame_phone.delete(0, "end")
        self.lf_frame_phone.configure(placeholder_text="Телефон")
        self.lf_combo_job.set("Менеджер")
        self.lf_combo_gender.set("Мужчина")

    def insert(self):
        user_id = self.lf_entry_id.get()
        user_name = self.lf_entry_name.get()
        user_fam = self.lf_entry_fam.get()
        user_age = self.lf_entry_age.get()
        user_phone = self.lf_frame_phone.get()
        user_job = self.lf_combo_job.get()
        user_gen = self.lf_combo_gender.get()
        if user_id == "" or user_name == "" or user_fam == "" or user_age == "" or user_phone == "":
            self.lf_combo_job.focus_set()
            CTkMessagebox(title="Error", message="Заполните все поля")
            return
        if not db.id_exist(user_id):
            self.lf_combo_job.focus_set()
            CTkMessagebox(title="Error", message="Такой ID уже существует")
            return
        db.db_insert(user_id, user_name, user_fam, user_age, user_phone, user_job, user_gen)
        self.lf_combo_job.focus_set()
        CTkMessagebox(title="Success", message="Данные были добавлены")
        self.select_db()
        self.clear()

    def display_data(self, event):
        item = self.tree.focus()
        if not item:
            return
        values = self.tree.item(item, "values")
        self.clear()
        self.lf_entry_id.insert(0, values[0])
        self.lf_entry_name.insert(0, values[1])
        self.lf_entry_fam.insert(0, values[2])
        self.lf_entry_age.insert(0, values[3])
        self.lf_frame_phone.insert(0, values[4])
        self.lf_combo_job.set(values[5])
        self.lf_combo_gender.set(values[6])

    def delete(self):
        item = self.tree.focus()
        if not item:
            CTkMessagebox(title="Error", message="Ничего не выбрано")
        else:
            user_id = self.tree.item(item, "values")[0]
            db.db_delete(user_id)
            CTkMessagebox(title="Success", message="Данные были удалены")
        self.select_db()
        self.clear()

    def delete_all(self):
        db.db_delete_all()
        self.select_db()
        self.clear()

    def update(self):
        item = self.tree.focus()
        if not item:
            CTkMessagebox(title="Error", message="Ничего не выбрано")
        else:
            user_id = self.tree.item(item, "values")[0]
            user_name = self.lf_entry_name.get()
            user_fam = self.lf_entry_fam.get()
            user_age = self.lf_entry_age.get()
            user_phone = self.lf_frame_phone.get()
            user_job = self.lf_combo_job.get()
            user_gen = self.lf_combo_gender.get()
            if user_name == "" or user_fam == "" or user_age == "" or user_phone == "":
                CTkMessagebox(title="Error", message="Заполните все поля")
                return
            db.db_update(user_id, user_name, user_fam, user_age, user_phone, user_job, user_gen)
            self.df_btn_upd.focus_set()
            CTkMessagebox(title="Success", message="Данные были обновлены")
        self.select_db()
        self.clear()

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
