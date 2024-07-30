import csv
import faker

fake = faker.Faker()

with open('large_input.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])

    for _ in range(10000000):  # 10 million rows
        writer.writerow([
            fake.first_name(),
            fake.last_name(),
            fake.street_address(),
            fake.date_of_birth()
        ])