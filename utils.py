import cv2
import numpy as np

def extract_features(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (64, 64))  # Redimensionne
    return img.flatten()  # Convertit en vecteur

def load_images_features(paths):
    return [extract_features(p) for p in paths]
