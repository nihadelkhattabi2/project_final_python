import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import joblib
from model import train_model, predict_image

cat_images = []
dog_images = []
test_image_path = ""
model = None

def select_images(label, target_list, category):
    files = filedialog.askopenfilenames(title=f"Sélectionner 10 images de {category}")
    if len(files) != 10:
        messagebox.showerror("Erreur", f"Tu dois choisir exactement 10 images de {category}")
        return
    target_list.clear()
    target_list.extend(files)
    label.config(text=f"{len(files)} images chargées")

def train():
    global model
    if len(cat_images) != 10 or len(dog_images) != 10:
        messagebox.showerror("Erreur", "Charge 10 images de chaque catégorie")
        return
    model = train_model(cat_images, dog_images)
    messagebox.showinfo("Succès", "Modèle entraîné avec succès!")

def load_test_image():
    global test_image_path
    file = filedialog.askopenfilename(title="Choisir une image à tester")
    if file:
        test_image_path = file
        img = Image.open(file).resize((100, 100))
        img = ImageTk.PhotoImage(img)
        test_img_label.config(image=img)
        test_img_label.image = img

def predict():
    if not model or not test_image_path:
        messagebox.showerror("Erreur", "Modèle non entraîné ou image non sélectionnée")
        return
    probas = predict_image(model, test_image_path)
    result = f"{round(probas[1]*100)}% chien" if probas[1] > probas[0] else f"{round(probas[0]*100)}% chat"
    result_label.config(text=result)

# --- Interface Tkinter ---
root = tk.Tk()
root.title("Application IA Chat / Chien")
root.geometry("500x600")

tk.Label(root, text="Sélectionner 10 images de chats :").pack()
cat_label = tk.Label(root, text="Aucune image")
cat_label.pack()
tk.Button(root, text="Charger chats", command=lambda: select_images(cat_label, cat_images, "chat")).pack()

tk.Label(root, text="Sélectionner 10 images de chiens :").pack()
dog_label = tk.Label(root, text="Aucune image")
dog_label.pack()
tk.Button(root, text="Charger chiens", command=lambda: select_images(dog_label, dog_images, "chien")).pack()

tk.Button(root, text="Entraîner le modèle", command=train, bg="lightgreen").pack(pady=10)

tk.Label(root, text="Nouvelle photo à tester :").pack()
test_img_label = tk.Label(root)
test_img_label.pack()
tk.Button(root, text="Charger photo test", command=load_test_image).pack()

tk.Button(root, text="Prédiction", command=predict, bg="lightblue").pack(pady=10)
result_label = tk.Label(root, text="Résultat s'affichera ici")
result_label.pack()

root.mainloop()
