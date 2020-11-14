import discord
from replit import db
import time
from discord.ext import commands

class Other(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['afk'])
  async def AFK(self,ctx, *, reason="`AFK`"):
    var = discord.utils.get(ctx.guild.roles, name = "AFK")
    var2 = discord.utils.get(ctx.guild.roles, name = "Flight Notifications")
    try:
      del db[ctx.author.id]
      nick1 = f"[AFK] {ctx.author.display_name}"
      nick2 = nick1.replace('[AFK]','')
      await ctx.send(f"Welcome back {ctx.author.mention}, i removed your AFK")
      try:
        await ctx.author.remove_roles(var)
        await ctx.author.add_roles(var2)
      except:
        print("cant update role")
      finally:
        try:
          await ctx.author.edit(nick=nick2)
        except:
          print("Cant rename")
    except:      
      db[ctx.author.id] = reason
      await ctx.send(f"I set you AFK: {reason}" .format(reason))
      try:
        await ctx.author.remove_roles(var2)
        await ctx.author.add_roles(var)
      except:
        print("cant change role")
      finally:
        try:
          await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
        except:
          print("Cant rename")

  @commands.command()
  async def ping(self, ctx):
      before = time.monotonic()
      ping = (time.monotonic() - before) * 1000
      await ctx.send(f"Ping Pong! ```{int(ping)}ms```")

def setup(client):
    client.add_cog(Other(client))
    return