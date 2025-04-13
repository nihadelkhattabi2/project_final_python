import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk

def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path).resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        img_label.configure(image=img_tk)
        img_label.image = img_tk
        print("Image chargée :", file_path)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Application IA - Classifier Chat/Chien")
root.geometry("400x300")

# Bouton pour charger une image
btn = tk.Button(root, text="Charger une image", command=load_image)
btn.pack(pady=10)

# Label pour afficher l'image
img_label = Label(root)
img_label.pack()

# Lancer l'interface
root.mainloop()
