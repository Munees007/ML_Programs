import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import ExtraTreesClassifier
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
model = ExtraTreesClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
importance = model.feature_importances_
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})
feature_importance = feature_importance.sort_values(
    by="Importance",
    ascending=False
)
print("\n1. Display Dataset\n2. Feature Importance\n3. Plot Feature Importance\n4. Predict Iris Species\n0. Exit")
while True:
    try:
        ch = int(input("Enter Your Choice: "))
        match ch:
            case 1:
                print("\n---------- Iris Dataset ----------")
                print(X.head(10))
                print("\nTarget Species:")
                print(iris.target_names)
            case 2:
                print("\n---------- Feature Importance ----------")
                print(feature_importance)
            case 3:
                print("\n---------- Feature Importance Graph ----------")
                plt.figure(figsize=(8, 5))
                plt.bar(
                    feature_importance["Feature"],
                    feature_importance["Importance"]
                )
                plt.xticks(rotation=45)
                plt.xlabel("Features")
                plt.ylabel("Importance")
                plt.title("Feature Selection using Extra Trees Classifier")
                plt.tight_layout()
                plt.show()
            case 4:
                print("\n---------- Predict Iris Species ----------")
                sl = float(input("Enter Sepal Length (cm): "))
                sw = float(input("Enter Sepal Width (cm): "))
                pl = float(input("Enter Petal Length (cm): "))
                pw = float(input("Enter Petal Width (cm): "))
                new_data = pd.DataFrame(
                    [[sl, sw, pl, pw]],
                    columns=iris.feature_names
                )
                prediction = model.predict(new_data)
                print("Predicted Iris Species:", iris.target_names[prediction[0]])
            case 0:
                print("Program terminated.")
                break
            case _:
                print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)