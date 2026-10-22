def covariance(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    total = 0
    for i in range(n):
        total += (x[i] - mean_x) * (y[i] - mean_y)
    return total / (n - 1)
def correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = 0
    sum_x = 0
    sum_y = 0
    for i in range(n):
        dx = x[i] - mean_x
        dy = y[i] - mean_y
        numerator += dx * dy
        sum_x += dx ** 2
        sum_y += dy ** 2
    denominator = (sum_x * sum_y) ** 0.5
    if denominator == 0:
        return "Correlation cannot be calculated"
    return numerator / denominator
n = int(input("Enter number of data points: "))
x = []
y = []
for i in range(n):
    x.append(float(input("Enter X value: ")))
    y.append(float(input("Enter Y value: ")))
print("\n--- MENU ---")
print("1. Display Data")
print("2. Covariance")
print("3. Correlation")
print("0. Exit")
while True:
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("X =", x)
        print("Y =", y)
    elif ch == 2:
        if n < 2:
            print("Enter at least 2 data points")
        else:
            print("Covariance =", covariance(x, y))
    elif ch == 3:
        if n < 2:
            print("Enter at least 2 data points")
        else:
            print("Correlation =", correlation(x, y))
    elif ch == 0:
        print("Program terminated.")
        break
    else:
        print("Invalid choice!")
