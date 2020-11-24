import discord
import os
import sys
import subprocess
import time
import json
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
    intents = discord.Intents.all())


load_dotenv()
load = os.getenv("TOKEN")


subprocess.Popen(['java', '-jar', 'src/Lavalink.jar'])
time.sleep(40)


@client.event
async def on_ready():
    print(
        """
====================================
|           Developed by:          |
|            DistinctNoot          |
=====================================
        """)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'loading {filename}')
    

client.run(load)
