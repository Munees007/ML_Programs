import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('datasets/loan.csv')
print(df.head())
df.info()
sns.countplot(data=df, x='purpose', hue='not.fully.paid')
plt.xticks(rotation=45, ha='right')
plt.title("Loan Purpose vs Payment Status")
plt.tight_layout()
plt.show()
pre_df = pd.get_dummies(df, columns=['purpose'], drop_first=True)
print(pre_df.head())
from sklearn.model_selection import train_test_split
X = pre_df.drop('not.fully.paid', axis=1)
y = pre_df['not.fully.paid']
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    classification_report,
)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")
print("\nAccuracy:", accuracy)
print("F1 Score:", f1)
print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap='Blues')
plt.title("Naive Bayes - Confusion Matrix")
plt.tight_layout()
plt.show()
