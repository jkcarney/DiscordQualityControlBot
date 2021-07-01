import os
import discord
import sqlite.sqlite_manager as db
import role_utils as roles

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('secrets.env')

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    #if message.author == client.user or message.author.name in os.getenv('WHITELIST').split(','):
    #    return

    if message.content != '':
        await message.channel.send('SILENCE, {0}! BANNED.'.format(message.author.name))
        await ban_member(message.author, 'NO TEXT. ONLY SHITPOSTS.')
        db.erase_member(message.author)
    else:
        db.add_to_member_score(message.author)


async def ban_member(member: discord.Member, reason=None):
    await member.ban(reason=reason)

db.initialize_db()

client.run(TOKEN)
