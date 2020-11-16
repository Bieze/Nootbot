import discord
import time
from discord.ext import commands

class Other(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self, ctx):
      before = time.monotonic()
      ping = (time.monotonic() - before) * 1000
      await ctx.send(f"Ping Pong! ```{int(ping)}ms```")

def setup(client):
    client.add_cog(Other(client))
    return