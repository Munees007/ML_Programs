import numpy as np
try:
    ro = int(input("Enter the No of Rows: "))
    co = int(input("Enter the No of Columns: "))
    if ro <= 0 or co <= 0:
        raise ValueError("Rows and columns must be positive.")
    arr = np.zeros((ro, co), dtype=int)
    def cre(arr, ro, co):
        for i in range(ro):
            for j in range(co):
                arr[i, j] = int(input(f"Enter the Number [{i},{j}]: "))
        return arr
    def PrintArr(arr):
        rows, cols = arr.shape
        for i in range(rows):
            for j in range(cols):
                print(arr[i, j], end="  ")
            print()
    arr = cre(arr, ro, co)
    while True:
        try:
            print("\nPress 1 for Display\nPress 2 for Transpose\nPress 3 for Min and Max\nPress 4 for Sum\nPress 5 for Row and Column Sum\nPress 6 for Diagonal Values\nPress 7 for Update\nPress 8 for Array Details\nPress 9 for Sub Array\nPress 10 for Matrix Addition and Subtraction\nPress 0 to Exit")
            ch = int(input("Enter your Choice: "))
            match ch:
                case 1:
                    print("Array Elements are:")
                    PrintArr(arr)
                case 2:
                    print("Transpose Array:")
                    PrintArr(arr.T)
                case 3:
                    print(f"Minimum Element: {np.min(arr)}")
                    print(f"Maximum Element: {np.max(arr)}")
                case 4:
                    print(f"Sum of Array: {np.sum(arr)}")
                case 5:
                    print(f"Sum of Rows: {np.sum(arr, axis=1)}")
                    print(f"Sum of Columns: {np.sum(arr, axis=0)}")
                case 6:
                    if ro == co:
                        print(f"Diagonal Values: {np.diag(arr)}")
                    else:
                        print("Row and column sizes are not the same.")
                case 7:
                    r = int(input("Update Row Index: "))
                    c = int(input("Update Column Index: "))

                    if 0 <= r < ro and 0 <= c < co:
                        arr[r, c] = int(input("Enter New Element: "))
                        print("Element updated successfully!")
                    else:
                        print("Index out of bounds!")
                case 8:
                    print(f"Array Size: {np.size(arr)}")
                    print(f"Array Dimensions: {np.ndim(arr)}")
                    print(f"Array Shape: {np.shape(arr)}")
                case 9:
                    print(f"Row indices: 0 to {ro - 1}, Column indices: 0 to {co - 1}")
                    rs = int(input("Sub Array Row Start Index: "))
                    re = int(input("Sub Array Row End Index: "))
                    cs = int(input("Sub Array Column Start Index: "))
                    ce = int(input("Sub Array Column End Index: "))

                    if 0 <= rs <= re < ro and 0 <= cs <= ce < co:
                        subarray = arr[rs:re + 1, cs:ce + 1]
                        print("Extracted Sub Array:")
                        PrintArr(subarray)
                    else:
                        print("Invalid indices!")
                case 10:
                    print("Enter Elements for Matrix 2:")
                    arr2 = cre(np.zeros((ro, co), dtype=int), ro, co)
                    print("Matrix Addition Result:")
                    PrintArr(arr + arr2)
                    print("Matrix Subtraction Result:")
                    PrintArr(arr - arr2)
                case 0:
                    print("Exiting program. Goodbye!")
                    break
                case _:
                    print("Invalid choice! Please try again.")
        except (ValueError, IndexError) as e:
            print("Invalid input:", e)
        except Exception as e:
            print("Error:", e)
except (ValueError, OverflowError) as e:
    print("Invalid input:", e)
except Exception as e:
    print("Error:", e)
