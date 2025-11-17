from logic.converter import Converter
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

# Temporary version, global variables are not to be used
file_input: str = ""
file_output: str = ""


def choisir_fichier() -> str | None:
    global file_input

    filepath = filedialog.askopenfilename(
        title="Choisir un fichier",
        filetypes=[("Fichier excel", "*.xlsx")]
    )
    if filepath:
        file = filepath
        file_input = file
        return filepath
    else:
        return None

def choisir_fichier() -> str | None:
    global file_output
    
    filepath = filedialog.askopenfilename(
        title="Choisir un fichier",
        filetypes=[("Fichier excel", "*.xlsx")]
    )
    if filepath:
        file = filepath
        file_output = file
        return filepath
    else:
        return None

def completer_action():
    messagebox.showinfo("Action", "Bouton 'Completer' pressé !")
    current_path = Path('.').absolute()
    assets_path = current_path.join("assets").join("coordinates.csv")

    c = Converter(file, str(assets_path))
    print(c.reader.map)
    print(c.get_from_to())
    c.loader.close()
    # Add logic around here

def run():
    # Create main window
    root = tk.Tk()
    root.title("Soft transformer")
    root.geometry("300x150")

    # Store file path
    selected_file = tk.StringVar()

    # Buttons
    btn_choisir = tk.Button(root, text="Input file", command=choisir_fichier, width=15)
    btn2_choisir = tk.Button(root, text="Output file", command=choisir_fichier, width=15)
    btn_completer = tk.Button(root, text="Just do it!", command=completer_action, width=15)

    btn_choisir.pack(pady=10)
    btn2_choisir.pack(pady=10)
    btn_completer.pack(pady=10)

    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    run()
    exit(0)
