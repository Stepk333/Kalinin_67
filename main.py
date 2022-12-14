import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo, showerror
from rsa import RSA
class App(tk.Tk):
    #ширина окна
    WIDTH = 800
    #высота окна
    HEIGHT = 600
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("(с) Калинин")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.lbl = tk.Label(text="Электронная цифровая подпись на основе алгоритма RSA", font=("Arial Bond", 20))
        self.lbl.pack()
        self.rsa = RSA()

    def __create_data_window(self):
        if not (self.rsa.check_simple_number(int(self.entry_p.get())) and self.rsa.check_simple_number(int(self.entry_q.get()))):
            showerror(title="Ошибка", message="p или q должны быть простыми числами", default=OK)
        else:
            self.rsa.p = int(self.entry_p.get())
            self.rsa.q = int(self.entry_q.get())
            self.rsa.text = self.entry_text.get()
            self.rsa.calculate_open_close_key()
            showinfo(title="Сообщение", message="Данные", detail=f"Сообщение: {self.rsa.text}\nОткрытый ключ: {(self.rsa.n, self.rsa.e)}\nЗакрытый ключ {(self.rsa.n, self.rsa.d)}", icon=INFO, default=OK)

    def __calculate_data_signature_window(self):
        text, s = self.rsa.сalculate_signature()
        showinfo(title="Сообщение", message="Данные", detail=f"Сообщение: {text}\nПодпись {s}", icon=INFO, default=OK)

    def __check_data_signature_windows(self):
        if self.rsa.check_signature():
            showinfo(title="Информация", message="Подписи совпадают", default=OK)
        else:
            showerror(title="Ошибка", message="Подписи не совпадают", default=OK)

    def signature_calculate(self):
        #вычисляем подпись
        button1 = tk.Button(text="Вычислить электронную подпись", bg="green", command=self.__calculate_data_signature_window).pack(padx=10, pady=10)
        
    def signature_check(self):
        #проверяем подпись
        button2 = tk.Button(text="Проверить электронную подпись", bg="green", command=self.__check_data_signature_windows).pack(padx=10, pady=10)

    def EntryManager(self):
        self.lbl = tk.Label(text="Введите два простых числа p и q")
        self.lbl.pack()
        self.lbl = tk.Label(text="Введите p")
        self.lbl.pack()
        self.entry_p = tk.Entry()
        self.entry_p.pack()
        self.lbl = tk.Label(text="Введите q")
        self.lbl.pack()
        self.entry_q = tk.Entry()
        self.entry_q.pack()
        self.lbl = tk.Label(text="Введите текст")
        self.lbl.pack()
        self.entry_text = tk.Entry()
        self.entry_text.pack()
        self.button = tk.Button(text="Принять", command=self.__create_data_window).pack()

    def open(self):
        tk.mainloop()
if __name__ == "__main__":
    app = App()
    app.EntryManager()
    app.signature_calculate()
    app.signature_check()
    app.open()


