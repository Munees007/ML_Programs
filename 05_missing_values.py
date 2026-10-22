import pandas as p
import numpy as np
print("\n1. Fillna (Mean)\n2. DropNa\n3. IsNull and NotNull\n4. Replace Value\n5. Fillna (Median)\n6. Exit")
def CSV():
    df = p.read_csv("datasets/handle_missing.csv")
    Main(df)
def Main(df):
    while True:
        try:
            ch = int(input("Enter Your Choice: "))
            match ch:
                case 1:
                    print("-------------- FillNa (Mean) --------------")
                    df["Episode Count"] = round(df["Episode Count"].fillna(df["Episode Count"].mean()), 2)
                    print("Mean To Fill Value:\n", df)
                case 2:
                    print("-------------- DropNa --------------")
                    print(df["Episode Count"].dropna())
                case 3:
                    print("-------------- IsNull --------------")
                    print(df.isnull())
                    print("-------------- NotNull --------------")
                    print(df.notnull())
                case 4:
                    print("-------------- Replace --------------")
                    value = int(input("Enter the Replace Value: "))
                    print(df["Episode Count"].replace(np.nan, value))
                case 5:
                    print("-------------- FillNa (Median) --------------")
                    df["Episode Count"] = round(df["Episode Count"].fillna(df["Episode Count"].median()), 2)
                    print("Median To Fill Value:\n", df)
                case 6:
                    print("Program terminated.")
                    break
                case _:
                    print("Invalid Choice!")
        except Exception as e:
            print("Error:", e)
try:
    CSV()
except Exception as e:
    print("Error:", e)

