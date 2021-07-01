import discord
import discord.utils
from dotenv import load_dotenv
import os, sys

load_dotenv('secrets.env')

#{"1:simpleton","5:normie","20:edgy"...}
ROLES = os.getenv('ROLES').split(',')


def check_rank(score):
    score = str(score)
    for rule in ROLES:
        if score in rule:
            return rule.split(':')[1]
    return None
