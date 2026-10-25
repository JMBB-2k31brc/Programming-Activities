
def verifyPattern(generatedRows, generatedColumns, rows, columns):
    if generatedRows == rows and generatedColumns == columns:
        print("Pattern verified.")
    else:
        print("Pattern verification failed.")



def displayPattern(rows, columns):
    generatedRows = 0
    generatedColumns = 0

    for i in range(rows):
        generatedColumns = 0

        for j in range(1, columns + 1):
            print(j, end=" ")
            generatedColumns += 1

        print()
        generatedRows += 1

    print("Generated rows:", generatedRows)
    print("Generated columns:", generatedColumns)

    verifyPattern(generatedRows, generatedColumns, rows, columns)

################################## triple j

while True:
    try:
        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid input. Rows must be a positive whole number.")
            continue

        break

    except ValueError:
        print("Invalid input. Rows must be a positive whole number.")

while True:
    try:
        columns = int(input("Enter number of columns: "))

        if columns <= 0:
            print("Invalid input. Columns must be a positive whole number.")
            continue

        break

    except ValueError:
        print("Invalid input. Columns must be a positive whole number.")

displayPattern(rows, columns)
