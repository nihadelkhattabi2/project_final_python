from sklearn.svm import SVC
import joblib

def train_model(cat_paths, dog_paths):
    from utils import load_images_features

    X = load_images_features(cat_paths + dog_paths)
    y = [0]*len(cat_paths) + [1]*len(dog_paths)

    model = SVC(probability=True)
    model.fit(X, y)
    joblib.dump(model, 'model.pkl')
    return model

def predict_image(model, img_path):
    from utils import extract_features
    feat = extract_features(img_path)
    probas = model.predict_proba([feat])[0]
    return probas  # [proba_chat, proba_chien]
