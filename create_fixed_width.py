spec = [
    ("Field1", 10),
    ("Field2", 15),
    ("Field3", 5),
    ("Field4", 20)
]

data = [
    ("1234567890", "abcdefghijklmno", "12345", "ABCDEFGHIJKLMNOPQRST"),
    ("0987654321", "zyxwvutsrqponml", "54321", "ZYXWVUTSRQPONMLKJIHG"),
]

def generate_fixed_width_file(filename, data, spec):
    with open(filename, 'w', encoding='utf-8') as f:
        for record in data:
            line = ''.join([record[i].ljust(spec[i][1]) for i in range(len(record))])
            f.write(line + '\n')

generate_fixed_width_file('fixed_width.txt', data, spec)
