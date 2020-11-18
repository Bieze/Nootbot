import discord
import time
import asyncio
from discord.ext import commands

class Other(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def afk(self, ctx, mins):
    current_nick = ctx.display.name
    embed = discord.Embed(color = 0x212c47, title = "AFK")
    embed.add_field(name = "----------------------" ,value= f"{ctx.author.mention} has gone afk for {mins} minutes.")
    await ctx.send(embed = embed)
    await ctx.author.edit(nick=f"[AFK] {ctx.display.name}")
    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            await ctx.author.edit(nick=current_nick)
            await ctx.send(f"{ctx.author.mention} is no longer AFK")
            break

  @commands.command()
  async def ping(self, ctx):
      before = time.monotonic()
      ping = (time.monotonic() - before) * 1000
      await ctx.send(f"Ping Pong! ```{int(ping)}ms```")

def setup(client):
    client.add_cog(Other(client))
    return