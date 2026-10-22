
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("datasets/Ben10Dataset.csv")
def MinMax(val, min, max, nmin, nmax):
    if min == max:
        return "Normalization cannot be calculated."
    result = (((val - min) / (max - min)) * (nmax - nmin)) + nmin
    return f"{val} ====> {np.round(result, 2)}"
def ZScore(val, mean, std):
    if std == 0:
        return "Z-Score cannot be calculated."
    result = (val - mean) / std
    return f"{val} ====> {round(result, 2)}"
def decimal(val):
    dig = len(str(abs(int(val))))
    return val / 10**dig
num = df.describe().columns.to_list()
print("\n1. MinMax Normalization\n2. Z-Score Normalization\n3. Decimal Scale Normalization\n4. Exit")
while True:
    try:
        ch = int(input("Enter Your Choice: "))
        match ch:
            case 1:
                print("\n---------- MinMax Normalization ----------")
                for index, col in enumerate(num):
                    print(f"{index} => {col}", end="  ")
                colindex = int(input("\nEnter Column Index: "))
                min = df[num[colindex]].head(10).min()
                max = df[num[colindex]].head(10).max()
                print("Minimum:", min, "Maximum:", max)
                val = float(input("Enter the Value: "))
                nmin = float(input("Enter the New Min Value: "))
                nmax = float(input("Enter the New Max Value: "))
                print(MinMax(val, min, max, nmin, nmax))
            case 2:
                print("\n---------- Z-Score Normalization ----------")
                for index, col in enumerate(num):
                    print(f"{index} => {col}", end="  ")
                colindex = int(input("\nEnter Column Index: "))
                mean = df[num[colindex]].head(10).mean()
                std = df[num[colindex]].head(10).std()
                print("Mean:", round(mean, 2), "Standard Deviation:", round(std, 2))
                val = float(input("Enter the Value: "))
                print(ZScore(val, mean, std))
            case 3:
                print("\n---------- Decimal Scale Normalization ----------")

                val = int(input("Enter the Number: "))

                print("Normalized Value:", decimal(val))
            case 4:
                print("Exit Program")
                break
            case _:
                print("Invalid Choice!")
    except Exception as e:
        print("Error:", e)