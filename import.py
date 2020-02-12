# imports data from a CSV spreadsheet into a database

from sys import argv
import csv
import cs50


def main():

    # Check command line arguments
    if len(argv) != 2:
        print("Usage: import.py [csv file]")
        exit(1)

    # Create database
    open(f"students.db", "w").close()
    db = cs50.SQL("sqlite:///students.db")

    # Create students table
    db.execute("CREATE TABLE students (id INT, first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC, PRIMARY KEY(id))")

    # Initialize database id
    student_id = 0

    with open(argv[1], "r") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # Assume each student will have a first and last name OR a first, middle, and last name
            name = row['name'].split()
            if count_whitespaces(row['name']) == 1:
                first = name[0]
                middle = (None,)
                last = name[1]
            else:
                first = name[0]
                middle = name[1]
                last = name[2]

            # Insert student into database
            db.execute("INSERT INTO students (id, first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?, ?)",
                       student_id, first, middle, last, row['house'], row['birth'])

            student_id += 1

            # Testing
            # print(student_id, first, middle, last, row['house'], row['birth'])


def count_whitespaces(text):
    n = 0
    for c in text:
        if c.isspace():
            n += 1
    return n


main()