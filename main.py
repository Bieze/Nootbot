import discord
import os
import sys
import subprocess
import time
from keep_alive import keep_alive
sys.dont_write_bytecode = True
from discord.ext import commands

client = commands.Bot(command_prefix=(os.getenv("PREFIX")), help_command=None)

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
	        type=discord.ActivityType.watching,
	        name=f"if you ping me, don't ping me!!"))


keep_alive()
client.run(os.getenv("TOKEN"))
