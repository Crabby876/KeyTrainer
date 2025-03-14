import random
import tkinter as tk

window = tk.Tk()

window.geometry("800x500")
window.title("Tastaturschreiben")

label = tk.Label(window, text="")
label.pack(padx=20, pady=20)

file = open("DE words.txt")
content = file.read()
germanWords = content.split(" ")
file.close()

randomText = ""

for i in range(10):
    if(i==9):
        randomText = randomText + germanWords[random.randint(1,500)]
    else:
        randomText = randomText + germanWords[random.randint(1,500)] + " "
label.config(text=randomText)

window.mainloop()