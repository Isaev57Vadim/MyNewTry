# Программа анализа .csv файлов

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st

# Создание главного окна
window = tk.Tk()
window.geometry("550x550")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
label_00 = tk.Label(text = "Файл;")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text = "")
label_01.grid(row=0, column=1, sticky="w")

label_10 = tk.Label(text = "Строк:")
label_10.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_11 = tk.Label(text = "")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text = "Столбцов:")
label_20.grid(row=2, column=0, padx=10, pady=10, sticky="e")

label_21 = tk.Label(text = "")
label_21.grid(row=2, column=1, sticky="w")

# Создание текстового вывода c прокруткой
output_text = st(height = 22, width = 50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")


# Запуск цикла mainloop
window.mainloop()
