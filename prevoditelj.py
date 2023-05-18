from translate import Translator
import customtkinter as ctk
import time
from tkinter import messagebox


class Prevoditelj(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Prevoditelj")
        self.geometry('500x350')
        self.resizable(False, False)
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")

        def prevedi(event):
            perf_time_start = time.perf_counter()
            ent_output.delete(0, ctk.END)
            prevoditelj = Translator(from_lang='en', to_lang='hr')
            prijevod = prevoditelj.translate(ent_input.get())
            ent_output.insert(0, prijevod)
            if not ent_input.get() == "":
                self.clipboard_clear()
                self.clipboard_append(prijevod)
                vrijeme = f"Prevedeno za {time.perf_counter() - perf_time_start} sekundi..."
                lbl_status.configure(text=vrijeme)
            else:
                messagebox.showinfo("Informacije", "Niste utipkali ništa za prijevod...")

        lbl_input = ctk.CTkLabel(master=self, text="Unesi tekst za prijevod:")
        lbl_input.pack(padx=10, pady=10)

        ent_input = ctk.CTkEntry(master=self, width=400, height=50, font=('Arial', 14))
        ent_input.pack(padx=10, pady=5)

        lbl_output = ctk.CTkLabel(master=self, text="Prijevod teksta:")
        lbl_output.pack(padx=10, pady=10)

        ent_output = ctk.CTkEntry(master=self, width=400, height=50, font=('Arial', 14))
        ent_output.pack(padx=10, pady=10, )

        btn_prevedi = ctk.CTkButton(master=self, text="Prevedi")
        btn_prevedi.pack(padx=10, pady=10)

        lbl_status = ctk.CTkLabel(master=self, text="")
        lbl_status.pack(padx=10, pady=10)

        self.bind('<Return>', prevedi)
        btn_prevedi.bind('<Button-1>', prevedi)


if __name__ == "__main__":
    prevoditelj = Prevoditelj()
    prevoditelj.mainloop()
