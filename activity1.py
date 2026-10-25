def getSum(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i
    return total



while True:
    try:
        limit = int(input("Hi there! Please enter your age: "))

        if limit <= 0:
            print("Invalid input.")
            print("Please enter a positive whole number.")
            continue
        break
    except ValueError:
        print("Invalid input.")
        print("Please enter a positive whole number.")

expected = limit * (limit + 1) // 2
result = getSum(limit)

print("Expected sum is", expected)
print("After calling the function getSum, the sum of all numbers from 1 to", limit, "is:", result)

if result == expected:
    print("Output Verified.")
else:
    print("Output verification failed.")
