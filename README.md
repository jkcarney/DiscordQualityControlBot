# DiscordQualityControlBot

<br>

<p align="center"><img width=50% src="https://i.imgur.com/DgGIKII.png"></p>


## Overview
The QualityControlBot (or QCB) is my answer to a social experiment idea I had. That idea was, "If everyone in a Discord server could only communicate via images and videos, what would happen?"

The QCB accomplishes this pretty simply: it sees if each message in the chat contains text. If it does, the sender is immediately banned from the server. However, if they post a video or image with no text, then they are rewarded points that go towards an server rank. 

QCB is fairly lightweight. It utilizes the discord.py library as well as Python's built in sqlite3 library for database interaction.

<br> 

## Setup
First in the root of the folder, you must create a file, ```secrets.env```. The .env file will serve for holding your discord token and a few other things. The file should contain two lines that looks like this:

```DISCORD_TOKEN=ABCD...``` where ABCD... is your token. 

```WHITELIST=user_guy#1234,user_lady#5678,``` where the users are replaced with names you may wish to whitelist. Whitelisted names are not affected by the bot and will never increment their internal score. The format must have the names separated by commas (it also must end in a comma) I recommend putting administrators and the bot itself into the whitelist.

<br>

In ```sqlite_manager.py```, the table populating for the roles is located in the function ```def populate_roles_table(conn)```

Change the strings and numbers to match the role you want at the specified threshold. For example, if you wanted the role "Cool-Guy" to be achieved at 100 points, in data you would add a tuple that looks like: 

```(100, 'Cool-Guy'),...``` 

(this way of changing the roles and thresholds is temporary and will be changed to something more intuitive later.)

<br>

To run the bot, navigate to the root and run ```python3 quality_control.py```. This will initialize the database for you as well.
