
import joblib
from pathlib import Path

model_path = Path(__file__).resolve().parent.parent / "models" / "spam_detection_pipeline.pkl"

bundle = joblib.load(model_path)

model = bundle['model']
vectorizer = bundle['vectorizer']

def predict_spam(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)

    if prediction[0] == 1:
        return "Spam"
    else:
        return "Ham"

def spam_detection_system():
    print("================================")
    print("       SPAM DETECTION SYSTEM")
    print("================================")

    message = input("Enter your message: ")
    result = predict_spam(message)

    print("\nPrediction:", result)
    print("================================")

if __name__ == "__main__":
    spam_detection_system()
