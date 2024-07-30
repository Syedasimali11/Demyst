import csv

spec = [
    ("Field1", 10),
    ("Field2", 15),
    ("Field3", 5),
    ("Field4", 20)
]

def parse_fixed_width_file(input_filename, output_filename, spec):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow([field[0] for field in spec])  # Write header
        for line in infile:
            record = [line[sum(field[1] for field in spec[:i]):sum(field[1] for field in spec[:i+1])].strip() for i in range(len(spec))]
            writer.writerow(record)

parse_fixed_width_file('fixed_width.txt', 'output.csv', spec)
