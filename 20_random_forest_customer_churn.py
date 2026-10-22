
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report, ConfusionMatrixDisplay)
df = pd.read_csv("datasets/customer_churn_dataset.csv")
print("Dataset shape:", df.shape)
print(df['Churn'].value_counts())
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
df = df.drop(columns=['customerID'])
for col in df.select_dtypes(include=['object', 'str']).columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
X = df.drop(columns=['Churn'])
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)
y_pred = rf_model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc*100:.2f}%")
print("\nClassification Report:\n",
      classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap='Greens')
plt.title("Random Forest - Confusion Matrix")
plt.tight_layout()
plt.show()
importances = pd.Series(
    rf_model.feature_importances_, index=X.columns
).sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 5))
importances.plot(kind='barh')
plt.gca().invert_yaxis()
plt.title("Top 10 Features Influencing Customer Churn")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.show()