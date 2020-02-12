# Prints a list of students for a given house in alphabetical order from students.db

from sys import argv
import cs50


def main():
    if len(argv) != 2:
        print("Usage: roster.py [House Name]")
        exit(1)

    db = cs50.SQL("sqlite:///students.db")

    # Query database
    query_result = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first ASC", argv[1])

    for row in query_result:
        if row['middle'] == None:
            print(row['first'], row['last']+", born", row['birth'])
        else:
            print(row['first'], row['middle'], row['last']+", born", row['birth'])


main()