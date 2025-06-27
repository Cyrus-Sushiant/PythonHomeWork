import csv

with open("d:\Workspace\Python\HomeWork25\input.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)  # Reads the first row (header)

    with open("d:\Workspace\Python\HomeWork25\output.csv", "w", newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Product Name", "Price", "Quantity", "Total Price"])
        for row in reader:
            writer.writerow([row[0], row[1], row[2], (int(row[1]) * int(row[2]))])

        output_file.close()