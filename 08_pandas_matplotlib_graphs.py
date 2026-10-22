import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("datasets/DataSet.csv")
print("\n1. Display Dataset Structure\n2. Display Statistical Summary\n3. Characters by Series (Bar Graph)\n4. Characters by Character Type (Bar Graph)\n5. First Appearance Year (Line Graph)\n6. Series Distribution (Pie Chart)\n7. Exit")
while True:
    try:
        ch = int(input("Enter Your Choice: "))
        match ch:
            case 1:
                print("\n\tDataset Structure")
                print(data)
                print("\n\tFirst Five Characters")
                print(data.head())
                print("\n\tLast Five Characters")
                print(data.tail())
                print("\nDataset Shape:", data.shape)
                print("\nColumn Names:", data.columns)
                print("\nData Types:\n", data.dtypes)
                print("\nDataset Information:")
                data.info()
                print("\nMissing Values:\n", data.isnull().sum())
            case 2:
                print("\n\tStatistical Summary")
                print(data.describe(include="all"))
            case 3:
                print("\n\tCharacters by Series")
                counts = data["Series"].value_counts()
                print(counts)
                counts.plot(kind="bar", title="Characters by Series")
                plt.xlabel("Series")
                plt.ylabel("Number of Characters")
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()
            case 4:
                print("\n\tCharacters by Character Type")
                counts = data["Character Type"].value_counts()
                print(counts)
                counts.plot(kind="bar", title="Characters by Type")
                plt.xlabel("Character Type")
                plt.ylabel("Number of Characters")
                plt.xticks(rotation=45, ha="right")
                plt.tight_layout()
                plt.show()
            case 5:
                print("\n\tCharacters by First Appearance Year")
                counts = data["First Appearance Year"].value_counts().sort_index()
                print(counts)
                counts.plot(kind="line", marker="o", title="Characters by First Appearance Year")
                plt.xlabel("First Appearance Year")
                plt.ylabel("Number of Characters")
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            case 6:
                print("\n\tSeries Distribution")
                counts = data["Series"].value_counts()
                print(counts)
                counts.plot(kind="pie", autopct="%1.1f%%", title="Series Distribution")
                plt.ylabel("")
                plt.tight_layout()
                plt.show()
            case 7:
                print("Program terminated.")
                break
            case _:
                print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)