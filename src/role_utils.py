import discord
import discord.utils
import os, sys, sqlite3




def check_rank(score):
    conn = sqlite3.connect(r'sqlite\members.db')
    c = conn.cursor()
    c.execute("SELECT role_name FROM roles WHERE threshold=?", (score,))

    role = c.fetchone()

    if role is None:
        conn.close()
        return None
    else:
        conn.close()
        return role[0]
