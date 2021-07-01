import sqlite_manager as db
import sys

# python3 set_member_score.py jkc_boi#4751 100
if __name__ == "__main__":
    db.set_member_score(sys.argv[1], sys.argv[2])
