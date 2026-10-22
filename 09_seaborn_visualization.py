import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("datasets/Ben10Dataset.csv")
print("\n1. Display Dataset\n2. Scatter Plot\n3. Histogram\n4. Box Plot\n5. Heatmap\n6. Violin Plot\n7. Count Plot\n8. Pair Plot\n0. Exit")
while True:
    try:
        ch = int(input("Enter Your Choice: "))
        match ch:
            case 1:
                print("\n---------- Ben 10 Alien Dataset ----------")
                print(data.head(5))
            case 2:
                print("\n---------- Scatter Plot ----------")
                sns.scatterplot(data=data, x="Height (m)", y="Power Level", hue="Series")
                plt.title("Alien Height vs Power Level")
                plt.show()
            case 3:
                print("\n---------- Histogram ----------")
                sns.histplot(data=data, x="Power Level", bins=8, kde=True)
                plt.title("Distribution of Alien Power Levels")
                plt.show()
            case 4:
                print("\n---------- Box Plot ----------")
                sns.boxplot(data=data, x="Series", y="Height (m)")
                plt.title("Alien Height by Series")
                plt.xticks(rotation=30)
                plt.tight_layout()
                plt.show()
            case 5:
                print("\n---------- Heatmap ----------")
                corr = data[["Power Level", "Height (m)", "First Appearance Year"]].corr()
                sns.heatmap(corr, annot=True, cmap="coolwarm")
                plt.title("Alien Dataset Correlation Heatmap")
                plt.show()
            case 6:
                print("\n---------- Violin Plot ----------")
                sns.violinplot(data=data, x="Series", y="Power Level")
                plt.title("Power Level Distribution by Series")
                plt.xticks(rotation=30)
                plt.tight_layout()
                plt.show()
            case 7:
                print("\n---------- Count Plot ----------")
                sns.countplot(data=data, x="Element")
                plt.title("Number of Aliens by Element")
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            case 8:
                print("\n---------- Pair Plot ----------")
                sns.pairplot(data, vars=["Power Level", "Height (m)", "First Appearance Year"], hue="Series")
                plt.show()
            case 0:
                print("Program terminated.")
                break
            case _:
                print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)