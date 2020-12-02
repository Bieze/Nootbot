import discord
import os
import sys
import asyncio
import subprocess
import json
import time
import sqlite3
from forest.info import discordv
from forest.info import sqlitev
from forest.info import osv
from forest.info import pythonv
sys.dont_write_bytecode = True
from discord.ext import tasks, commands
from sqlite3.dbapi2 import sqlite_version, sqlite_version_info
from dotenv import load_dotenv  


client = commands.Bot(
    command_prefix=">", 
    help_command=None,
    intents = discord.Intents.all(),
    case_insensitive = True
    )


load_dotenv()
load = os.getenv("TOKEN")


subprocess.Popen(['java', '-jar', 'src/Lavalink.jar'])
time.sleep(5)


@client.event
async def on_ready():
    discordv()
    sqlitev()
    pythonv()
    osv()
    status.start()
    print(f"Logged in.")
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
        """)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'loading {filename}')
    

a = """
====================================
            Developed by:          
            DistinctNoot          
====================================
        """


@tasks.loop(seconds=5)
async def status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"to {len(client.guilds)} servers"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"to DistinctNoot"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Python 3.3"))
    await asyncio.sleep(5)




client.run(load)
