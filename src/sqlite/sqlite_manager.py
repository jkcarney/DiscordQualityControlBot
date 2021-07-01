import sqlite3, os, discord

def initialize_db():
    if(not os.path.exists(r'sqlite\members.db')):
        print('Database not found. Initializing one...')
        conn = sqlite3.connect(r'sqlite\members.db')
        c = conn.cursor()
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='members' ''')
        if(c.fetchone()[0] == 1):
            print('Table exists')
        else:
            create_tables(conn)
            print('Table created.')
    else:
        print('Database already exists')

def create_tables(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE members (
                username text,
                post_count integer
                )''')
    conn.commit()
    conn.close()


def add_to_member_score(author):
    conn = sqlite3.connect(r'sqlite\members.db')
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE username=?", (str(author),))

    # add user to db if none found
    if(c.fetchone() is None):
        initialize_member(conn, str(author))
    else:
        add_score(conn, str(author))

    c.execute("SELECT * FROM members WHERE username=?", (str(author),))
    data = c.fetchone()
    score = data[1]
    print('Updated member score: {}'.format(data))

    conn.close()
    return score


def initialize_member(conn, author):
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES (?, ?)", (author, 1))
    conn.commit()
    c.close()


def add_score(conn, author):
    c = conn.cursor()
    c.execute("SELECT post_count FROM members WHERE username=?", (author,))

    current_score = c.fetchone()
    #fetch one returns a tuple yipee
    current_score = int(current_score[0])
    current_score = current_score + 1

    c.execute("UPDATE members SET post_count=? WHERE username=?", (current_score,author))
    conn.commit()
    c.close()


#for use if a user is banned
def erase_member(member):
    user = str(member)
    conn = sqlite3.connect(r'sqlite\members.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM members WHERE username=?",(user,))
        conn.commit()
        print('{} got banned, therefore he was deleted from the database')
    except:
        print('An exception occured when trying to delete {} from the DB (probably they didn\'t exist)'.format(user))

    c.close()
    conn.close()
###############################
# These are utility functions #
###############################
def set_member_score(member, desired_score):
    conn = sqlite3.connect(r'members.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE members SET post_count=? WHERE username=?", (desired_score,member))
        conn.commit()
        print('Successfully updated {} to score {}'.format(member, desired_score))
    except Exception as e:
        print('Setting score failed for {}. Maybe a typo with the username?: '.format(member, e))
    conn.close()


def get_all_data():
    conn = sqlite3.connect(r'members.db')
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    data = c.fetchall()
    conn.close()
    return data
