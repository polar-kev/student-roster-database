# Student Roster Database
This project uses Python to import student data into a SQL database, and then produce class rosters based on user input.


The purpose of this project:
- practice file I/O and SQL queries in Python



## Running the code

import.py - takes a csv file as a command line argument

roster.py - takes a Hogwards house as a command line argument

characters.csv - contains a class roster from Hogwarts

students.db - contains a students table with the class roster (Recreated everytime import.py is run)


#### Example
```
$ python import.py characters.csv
$ python roster.py Gryffindor

Lavender Brown, born 1979'
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980
```
