
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (accuracy_score, confusion_matrix,
                              classification_report, ConfusionMatrixDisplay)
# Load your local dataset
df = pd.read_csv("datasets/breast_cancer_dataset.csv")
print("Dataset shape:", df.shape)
print(df['diagnosis_label'].value_counts())
X = df.drop(columns=['diagnosis', 'diagnosis_label'])
y = df['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_model.fit(X_train_scaled, y_train)
y_pred = svm_model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc*100:.2f}%")
print("\nClassification Report:\n", classification_report(
    y_test, y_pred, target_names=['malignant', 'benign']))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm, display_labels=['malignant', 'benign'])
disp.plot(cmap='Blues')
plt.title("SVM - Confusion Matrix (Breast Cancer Diagnosis)")
plt.tight_layout()
plt.savefig("svm_confusion_matrix.png", dpi=150)
plt.show()
svm_linear = SVC(kernel='linear', C=1.0, random_state=42)
svm_linear.fit(X_train_scaled, y_train)
acc_linear = accuracy_score(y_test, svm_linear.predict(X_test_scaled))
print(f"\nLinear kernel accuracy: {acc_linear*100:.2f}%")
print(f"RBF kernel accuracy   : {acc*100:.2f}%")