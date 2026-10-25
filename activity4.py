def verifyOutput(skippedCount, expectedSkippedCount):
    if skippedCount == expectedSkippedCount:
        print("Output verified.")
    else:
        print("Output verification failed.")

def skippedMultiples(limit):
    skippedCount = 0

    for i in range(1, limit + 1):
        if i % 3 == 0:
            skippedCount += 1
            continue

        print(i, end=" ")

    print()
    return skippedCount



while True:
    try:
        limit = int(input("Enter limit: "))

        if limit <= 0:
            print("Invalid input.")
            print("Please enter a positive whole number.")
            continue
            
        break
      
    except ValueError:
        print("Invalid input.")
        print("Please enter a positive whole number.")

expectedSkippedCount = limit // 3
print("Expected skipped count is:", expectedSkippedCount)

skippedCount = skippedMultiples(limit)

print("After calling the function skippedMultiples, the computed skipped count is:", skippedCount)

verifyOutput(skippedCount, expectedSkippedCount)
