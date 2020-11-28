import discord
import os
import sys
import subprocess
import time
import json
import sqlite3
sys.dont_write_bytecode = True
from discord.ext import commands
from dotenv import load_dotenv


def get_prefix(client, message):
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(
    command_prefix=get_prefix, 
    help_command=None,
    activity = discord.Activity(name='your servers!', 
    type=discord.ActivityType.watching),
    intents = discord.Intents.all(),
    case_insensitive = True
    )


load_dotenv()
load = os.getenv("TOKEN")


subprocess.Popen(['java', '-jar', 'src/Lavalink.jar'])
time.sleep(40)


@client.event
async def on_ready():
    print(a)
    db = sqlite3.connect("Welcome.sqlite")
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS main(
            guild_id TEXT,
            welcome TEXT,
            goodbye TEXT,
            channel_id TEXT
        )

        CREATE TABLE IF NOT EXISTS warn(
            reason TEXT,
            id TEXT,
            moderator TEXT,
        )
        """
    )
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'loading {filename}')
    

a = """
====================================
|           Developed by:          |
|            DistinctNoot          |
=====================================
        """

client.run(load)
