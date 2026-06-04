import os
import tkinter as tk
from tkinter import filedialog, messagebox

def popraw_nazwe(sciezka):
    folder = os.path.dirname(sciezka)
    nazwa = os.path.basename(sciezka)
    
    baza, ext = os.path.splitext(nazwa)
    
    
    nowa_baza = baza.replace(".", "_").replace(",", "_").replace("!","")
    nowa_nazwa = nowa_baza + ext
    nowa_sciezka = os.path.join(folder, nowa_nazwa)
    
    
    if nowa_sciezka != sciezka:
        os.rename(sciezka, nowa_sciezka)
        return nowa_nazwa
    return None


root = tk.Tk()
root.withdraw()  


plik = filedialog.askopenfilename(title="Wybierz plik do poprawienia nazwy")

if plik:
    nowa_nazwa = popraw_nazwe(plik)
    if nowa_nazwa:
        messagebox.showinfo("Gotowe", f"Plik został zmieniony na:\n{nowa_nazwa}")
    else:
        messagebox.showinfo("Info", "Nie było zmian do wprowadzenia.")
else:
    messagebox.showinfo("Info", "Nie wybrano żadnego pliku.")
