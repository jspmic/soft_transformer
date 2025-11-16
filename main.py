from logic.converter import Converter
import tkinter as tk
from tkinter import filedialog, messagebox

file: str = ""


def choisir_fichier() -> str | None:
    filepath = filedialog.askopenfilename(
        title="Choisir un fichier",
        filetypes=[("Fichier excel", "*.xlsx")]
    )
    if filepath:
        file = filepath
        return filepath
    else:
        return None

def completer_action():
    messagebox.showinfo("Action", "Bouton 'Completer' pressé !")

    c = Converter(file, "./assets/coordinates.csv")
    print(c.reader.map)
    print(c.get_from_to())
    c.loader.close()
    # You can add your own logic here

def run():
    # Create main window
    root = tk.Tk()
    root.title("Soft transformer")
    root.geometry("300x150")

    # Store file path
    selected_file = tk.StringVar()

    # Buttons
    btn_choisir = tk.Button(root, text="Choisir", command=choisir_fichier, width=15)
    btn_completer = tk.Button(root, text="Completer", command=completer_action, width=15)

    btn_choisir.pack(pady=10)
    btn_completer.pack(pady=10)

    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    run()
    exit(0)
