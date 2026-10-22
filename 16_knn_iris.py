from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
irisData = load_iris()
x = irisData.data
y = irisData.target
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=30
)
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
print("Iris Dataset Loaded Successfully")
print("Model Accuracy:", knn.score(x_test, y_test))
s1 = float(input("Enter sepal length: "))
s2 = float(input("Enter sepal width: "))
s3 = float(input("Enter petal length: "))
s4 = float(input("Enter petal width: "))
user_pre = knn.predict([[s1, s2, s3, s4]])
flower = irisData.target_names[user_pre[0]]
print("\nPredicted Flower Name:", flower)
print("\nPredictions on Test Data:")
print(knn.predict(x_test))
