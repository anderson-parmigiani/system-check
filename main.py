import customtkinter
import pyperclip
from tkinter import messagebox
from store import os_info

class TextFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = customtkinter.CTkLabel(master=self, text="INFORMACIÓN", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.entries = []
        self.labels = ["Sistema Operativo", "Nombre de equipo", "CPU", "RAM", "Disco", "IP", "MAC"]

        for i, label_text in enumerate(self.labels):
            label = customtkinter.CTkLabel(master=self, text=label_text)
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")

            entry = customtkinter.CTkEntry(master=self, state=customtkinter.DISABLED, width=220)
            entry.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
            entry.bind("<Button-1>", self.copy_text)
            entry.bind("<Button-3>", self.copy_text)

            self.entries.append(entry)

    def insert_text_into_entries(self, texts):
        for entry, text in zip(self.entries, texts):
            entry.configure(state=customtkinter.NORMAL)
            if text is None:
                text = "n/d"
            entry.insert(0, text)
            entry.configure(state=customtkinter.DISABLED)

    def copy_text(self, event):
        entry = event.widget
        text = entry.get()
        pyperclip.copy(text)

        messagebox.showinfo("Copiado", "El texto ha sido copiado al portapapeles.")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("System Check")
        self.geometry("400x350")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        central_frame = customtkinter.CTkFrame(self)
        central_frame.grid(row=0, column=0, sticky="")

        central_frame.grid_columnconfigure(0, weight=1)
        central_frame.grid_rowconfigure(1, weight=1)

        self.text_frame = TextFrame(central_frame)
        self.text_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.text_frame.insert_text_into_entries([
            os_info.version(),
            os_info.hostname(),
            os_info.cpu(),
            os_info.ram(),
            os_info.disk_usage(),
            os_info.get_ip_address(),
            os_info.get_mac_address()
        ])

if __name__ == "__main__":
    app = App()
    app.mainloop()