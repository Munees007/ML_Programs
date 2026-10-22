import pandas as pd
data = pd.read_csv("datasets/DataSet.csv")
print("\n1. Display Dataset Structure\n2. Display Statistical Summary\n3. Particular Column Summary\n4. Group Characters by Series\n5. Group Characters by Character Type\n6. Group by First Appearance Year\n7. Series and Character Type\n8. Exit")
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
                print("\nAvailable Columns:\n", data.columns)
                col = input("Enter the Column Name: ")
                print("\n\tColumn Summary")
                print(data[col].describe())
            case 4:
                print("\n\tCharacters Grouped by Series")
                print(data.groupby("Series")["Character Name"].apply(list))
            case 5:
                print("\n\tCharacters Grouped by Character Type")
                print(data.groupby("Character Type")["Character Name"].apply(list))
            case 6:
                print("\n\tCharacters by First Appearance Year")
                print(data.groupby("First Appearance Year")["Character Name"].apply(list))
            case 7:
                print("\n\tSeries and Character Type")
                print(data.groupby(["Series", "Character Type"]).size())
            case 8:
                print("Program terminated.")
                break
            case _:
                print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)