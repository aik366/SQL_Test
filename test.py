import customtkinter as ctk
from customtkinter import CTkButton, CTkEntry, CTkFrame
from random import choices


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("+200+200")
        self.title("rgb color generator")
        self.resizable(False, False)

        ctk.set_appearance_mode("Dark")

        self.button = CTkButton(self, text="Generate", width=200, height=50, font=("Arial", 24),
                                command=self.button_clicked)
        self.button.grid(row=7, column=0, padx=20, pady=10, columnspan=15)

        self.button_clicked()
    def rgb_color(self):
        return "#" + "".join(choices("0123456789ABCDEF", k=6))

    def button_clicked(self):
        for i in range(0, 4, 2):
            for j in range(15):
                self.frame = CTkFrame(self, width=80, )
                self.frame.grid(row=i, column=j, padx=10, pady=10)
                self.entry = CTkEntry(self, width=80, font=("Arial", 14), justify="center")
                self.entry.grid(row=i + 1, column=j, padx=10)
                color_rgb = self.rgb_color()
                self.frame.configure(fg_color=color_rgb)
                self.entry.delete(0, "end")
                self.entry.insert(0, color_rgb)


if __name__ == "__main__":
    app = App()
    app.mainloop()
