import pandas as p
import numpy as np
print("\n1. Head Row\n2. Tail Row\n3. Specific Head and Tail Row\n4. Column Selection\n5. Add New Column\n6. Filter Data\n7. DataFrame Information\n8. Fillna\n9. Dropna\n10. IsNull and NotNull\n11. Replace\n12. Exit")
def Main():
    n = int(input("Enter the number of Series: "))
    name = []
    episodes = []
    year = []
    for i in range(n):
        print(f"---------- Enter Series {i+1} Details ----------")
        na = input("Enter Series Name: ")
        ep = int(input("Enter Episode Count: "))
        yr = int(input("Enter Release Year: "))

        name.append(na)
        episodes.append(ep)
        year.append(yr)
    data = {
        "Series Name": name,
        "Episode Count": episodes,
        "Release Year": year
    }
    df = p.DataFrame(data)
    print("\n------------- DataFrame ---------------")
    print(df)
    Implement(df)

def Implement(df):
    while True:
        try:            
            ch = int(input("Enter Your Choice: "))
            match ch:
                case 1:
                    print("Head Row:\n", df.head())
                case 2:
                    print("Tail Row:\n", df.tail())
                case 3:
                    h = int(input("Enter the Number of Rows: "))
                    print("Head Row:\n", df.head(h))
                    print("Tail Row:\n", df.tail(h))
                case 4:
                    print("All Columns:\n", df.columns)
                    s = input("Enter Specific Column: ")
                    print(df[s])
                case 5:
                    ne = input("Enter the New Column Name: ")
                    da = []
                    for i in range(len(df)):
                        data = input("Enter the Data: ")
                        da.append(data)
                    df[ne] = da
                    print("New DataFrame:\n", df)
                case 6:
                    ma = int(input("Enter the Minimum Episode Count: "))
                    print("Filtered Data:\n", df[df["Episode Count"] > ma])
                case 7:
                    print("DataFrame Information:")
                    df.info()
                    print("DataFrame Description:\n", df.describe())
                    print("DataFrame Shape:", df.shape)
                case 8:
                    print("Fillna:")
                    df["Episode Count"] = df["Episode Count"].fillna(df["Episode Count"].mean())
                    print(df["Episode Count"])
                case 9:
                    print("Dropna:")
                    print(df["Episode Count"].dropna())
                case 10:
                    print("IsNull:")
                    print(df.isnull())
                    print("NotNull:")
                    print(df.notnull())
                case 11:
                    print("Replace:")
                    print(df["Episode Count"].replace(np.nan, 0))
                case 12:
                    break
                case _:
                    print("Invalid Choice!")
        except Exception as e:
            print("Error:", e)
try:
    Main()
except Exception as e:
    print("Error:", e)