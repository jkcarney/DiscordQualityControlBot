import sqlite3, os, discord

def initialize_dbs():
    if(not os.path.exists(os.path.join('sqlite','members.db'))):
        print('Database not found. Initializing one...')
        conn = sqlite3.connect(os.path.join('sqlite','members.db'))
        c = conn.cursor()

        # Members table
        c.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='members' ''')
        if(c.fetchone()[0] == 1):
            print('Member table exists')
        else:
            create_member_table(conn)
            print('Member table created.')

        # Roles table
        c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name= 'roles' ")
        if(c.fetchone()[0] == 1):
            print('Roles table exists')
        else:
            create_roles_table(conn)
            print('Roles table created')
        conn.close()
    else:
        print('Database already exists')

def create_member_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE members (
                username text,
                post_count integer
                )''')
    conn.commit()

def create_roles_table(conn):
    c = conn.cursor()
    c.execute(''' CREATE TABLE roles (
                threshold integer,
                role_name text
                )''')
    conn.commit()
    populate_roles_table(conn)


def populate_roles_table(conn):
    c = conn.cursor()
    data = [(1, 'simpleton'),
            (5, 'normie'),
            (20, 'edgy'),
            (50, 'shitposter'),
            (100, 'based'),
            (200, 'shitpost-GOD'),
            (500, 'based-GOD'),
            (1000, 'GIGA-CHAD'),
            (2000, 'ENLIGHTENED')
            ]
    c.executemany('INSERT INTO roles VALUES(?, ?)', data)
    conn.commit()


def add_to_member_score(author):
    conn = sqlite3.connect(os.path.join('sqlite','members.db'))
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
    conn = sqlite3.connect(os.path.join('sqlite','members.db'))
    c = conn.cursor()
    try:
        c.execute("DELETE FROM members WHERE username=?",(user,))
        conn.commit()
        print('{0} got banned, therefore he was deleted from the database'.format(user))
    except:
        print('An exception occured when trying to delete {} from the DB (probably they didn\'t exist)'.format(user))

    c.close()
    conn.close()
###############################
# These are utility functions #
###############################
def set_member_score(member, desired_score):
    conn = sqlite3.connect(os.path.join('members.db'))
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE username=?", (str(author),))

    # add user to db if none found
    if(c.fetchone() is None):
        initialize_member(conn, str(author))
        
    try:
        c.execute("UPDATE members SET post_count=? WHERE username=?", (desired_score,member))
        conn.commit()
        print('Successfully updated {} to score {}'.format(member, desired_score))
    except Exception as e:
        print('Setting score failed for {}. Maybe a typo with the username?: '.format(member, e))
    conn.close()


def get_all_data():
    conn = sqlite3.connect(os.path.join('members.db'))
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    data = c.fetchall()
    conn.close()
    return data
