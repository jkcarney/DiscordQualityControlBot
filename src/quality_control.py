import os
import discord
import sqlite.sqlite_manager as db
import role_utils as roles
import bot_responses as responses
from discord.utils import get
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
    await responses.on_message_response(message, client)


async def ban_member(member: discord.Member, reason=None):
    await member.ban(reason=reason)

db.initialize_dbs()

client.run(TOKEN)
