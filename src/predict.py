import joblib
import pandas as pd

model = joblib.load("../models/logistic_regression.pkl")

def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    data = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)"
        ]
    )

    prediction = model.predict(data)

    return prediction[0]

if __name__ == "__main__":
    print("FLOWER CLASSIFICATION")
    sl = float(input("Enter Sepal Length: "))
    sw = float(input("Enter Sepal Width: "))
    pl = float(input("Enter Petal Length: "))
    pw = float(input("Enter Petal Width: "))

    result = predict_flower(sl, sw, pl, pw)

    print("Predicted Flower Species:", result)
