import statistics as st
print("\nPress 1 for Mean()\nPress 2 for Median()\nPress 3 for Mode()\nPress 4 for Standard Deviation\nPress 5 for Variance\nPress 6 for Harmonic Mean\nPress 7 for Median Low\nPress 8 for Median High\nPress 9 for Population Standard Deviation\nPress 10 for Population Variance\nPress 0 to Exit")
while True:
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 0:
                print("Program terminated.")
                break
            case 1:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Mean:", st.mean(data))
            case 2:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Median:", st.median(data))
            case 3:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Mode:", st.mode(data))
            case 4:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Standard Deviation:", st.stdev(data))
            case 5:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Variance:", st.variance(data))
            case 6:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Harmonic Mean:", st.harmonic_mean(data))
            case 7:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Median Low:", st.median_low(data))
            case 8:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Median High:", st.median_high(data))
            case 9:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Population Standard Deviation:", st.pstdev(data))
            case 10:
                data = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Population Variance:", st.pvariance(data))
            case _:
                print("Invalid choice!")
    except Exception as e:
        print("Error:", e)