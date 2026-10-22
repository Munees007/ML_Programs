import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
# Load the given dataset
df = pd.read_ex("datasets/elective_dataset.xlsx")
X = df[["GENDER", "UG", "Cross Major"]]
y = df["ELECTIVE"]
X = pd.get_dummies(X, dtype=int)
print("\nEncoded Features:")
print(X)
feature_names = X.columns.tolist()
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.5,
    random_state=42,
    stratify=y
)
clf = DecisionTreeClassifier(
    criterion="gini",
    random_state=42
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {acc:.4f}")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("TEXT REPRESENTATION OF DECISION TREE")
print(export_text(
    clf,
    feature_names=feature_names
))
plt.figure(figsize=(15, 8))
plot_tree(
    clf,
    feature_names=feature_names,
    class_names=[str(c) for c in clf.classes_],
    filled=True,
    rounded=True
)
plt.title("Decision Tree - Elective Prediction")
plt.show()