import sqlite_manager as db
import sys
import csv

if __name__ == '__main__':
    data = db.get_all_data()
    with open('all.csv','w') as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)
