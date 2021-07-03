import os
import discord
import sqlite.sqlite_manager as db
import role_utils as roles
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

async def on_message_response(message, client):
    load_dotenv('secrets.env')

    if message.author == client.user or str(message.author) in os.getenv('WHITELIST').split(','):
        return

    if message.content != '' and not 'https://tenor.com/view/' in message.content:
        await message.channel.send('SILENCE, {0}! BANNED.'.format(message.author.mention))
        await ban_member(message.author, 'NO TEXT. ONLY SHITPOSTS.')
        db.erase_member(message.author)
    else:
        score = db.add_to_member_score(message.author)
        role_string = roles.check_rank(score)
        if(role_string is not None):
            role = get(message.guild.roles, name=role_string)
            await message.author.add_roles(role)
            await message.channel.send('CONGRATULATIONS {0} FOR ACHIEVING {1} RANK'.format(message.author.mention, role_string))

async def ban_member(member: discord.Member, reason=None):
    await member.ban(reason=reason)
