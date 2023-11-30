import csv


def read_csv(input_files, row_list):
    with open(input_files) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)

def find_total_visits(rows):
    total_visits = 0

    for person in rows:
        for day in ['S', 'M', 'T', 'W', 'Th', 'F', 'S']:
            total_visits += int(person[day])

    return total_visits


# Main function
def ex2():
    total = find_total_visits()
    print(f"Total visits: {total}.")


ex2()
