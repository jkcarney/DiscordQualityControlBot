import os
import discord
from dotenv import load_dotenv

load_dotenv('secrets.env')

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('{client.user} has connected to Discord!')

client.run(TOKEN)
