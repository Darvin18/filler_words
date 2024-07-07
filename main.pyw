import tkinter as tk
import keyboard
import json
from pathlib import Path
import threading
from tkinter import messagebox
import sys
import os

#main window
win = tk.Tk()
photo = tk.PhotoImage(file='images/logo.png')
win.iconphoto(False, photo)
win.title('Filler Words')
win.geometry('500x600+750+250')
win.resizable(False, False)

#functions
def restart():
    win.destroy()
    os.startfile("Filler Words.exe")
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        win.destroy()
        sys.exit()

win.protocol("WM_DELETE_WINDOW", on_closing)
def load_json():
    with open('words/words.json') as file:
        words = json.load(file)
        for word in words:
            keyboard.add_abbreviation(str(word), '')
        keyboard.wait()

threading.Thread(target=load_json, daemon=True).start()
def get_entry():
    received_word = entry_filler.get()
    if received_word != '':
        path = Path('words/words.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        if received_word not in data:
            data.append(str(received_word))
            path.write_text(json.dumps(data), encoding='utf-8')
            keyboard.add_abbreviation(str(received_word), '')
def delete_words():
    with open("words/words.json", "w") as file:
        file.truncate()
    sp = []
    a = 'ъюэй'
    with open('words/words.json', 'w') as file:
        sp.append(a)
        json.dump(sp, file)
        restart()
def get_delete_word():
    word = delete_word.get()
    path = Path('words/words.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    try:
        data.remove(str(word))
        path.write_text(json.dumps(data), encoding='utf-8')
        restart()
    except ValueError:
        fail_deleted = tk.Label(win, text='There is no such word', font=('Arial', 10),
                                        fg='#ea3e53')
        fail_deleted.place(rely=0.59, relx=0.38)

#design
#1
filler_label = tk.Label(win, text='Filler Words', font=('Arial', 20), pady=15)
filler_label.pack()

entry_filler = tk.Entry(win, width=30, font=('Arial', 13))
entry_filler.pack()

#2
filler_button = tk.Button(win, text='Add filler word', font=('Arial', 13), padx=20, activebackground='#d5d5d5',
                          command=get_entry)
filler_button.place(rely=0.17, relx=0.33)

delete_button = tk.Button(win, text='Delete ALL words', font=('Arial', 13), padx=40, pady=10, background='red',
                          activebackground='#ca241a', command=delete_words)
delete_button.place(rely=0.25, relx=0.28)

#3
delete_word_label = tk.Label(win, text='Delete word:', font=('Arial', 20))
delete_word_label.place(rely=0.38, relx=0.33)

delete_word = tk.Entry(win, width=30, font=('Arial', 13))
delete_word.place(rely=0.46, relx=0.23)

delete_word_button = tk.Button(win, text='Delete word', font=('Arial', 13), padx=20, activebackground='#d5d5d5',
                               command=get_delete_word)
delete_word_button.place(rely=0.52, relx=0.37)

win.mainloop()
