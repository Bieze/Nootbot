import discord
import os
import sys
import subprocess
import time
import json
from keep_alive import keep_alive
sys.dont_write_bytecode = True
from discord.ext import commands


def get_prefix(client, message):
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix, help_command=None)

intents = discord.Intents.all()

subprocess.Popen(['java', '-jar', 'Lavalink.jar'])
time.sleep(40)


@client.event
async def on_ready():
    print("Running...")
    for filename in os.listdir('./cogs'):
	    if filename.endswith('.py'):
		    client.load_extension(f'cogs.{filename[:-3]}')
		    print(f'loading {filename}')
    await client.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.playing,
	        name=f"Start up.."))
    time.sleep(10)


keep_alive()
client.run(os.getenv("TOKEN"))
