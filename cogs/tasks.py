import discord
import traceback
import os
import asyncio
import json
import math
import sys
sys.dont_write_bytecode = True
from discord.ext import tasks, commands


class Background(commands.Cog):
  def __init__(self, client):
    self.client = client  
          

  @commands.Cog.listener()
  async def on_error(self, ctx, error):
      print(error) 


  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('ServerPrefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        

  @commands.Cog.listener()      
  async def on_guild_join(self, guild): 
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'n!'

    with open('ServerPrefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)   
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            perms = discord.Permissions(send_messages=False, read_messages=True)
            await guild.create_role(name="Muted", permissions=perms)
            perms1 = discord.Permissions(send_messages=True, read_messages=True)
            await guild.create_role(name="AFK", permissions=perms1)
            em = discord.Embed(
                title="Thanks for invting me into your server!", color=0x8A2BE2)
            em.set_thumbnail(url=guild.icon_url)
            em.add_field(
                name="Here is my thank you note",
                value=


                """
                Thanks for inviting me into your server!
                Consider [adding me](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot) to other servers to help get me verified
                and so others can have an awesome bot like me!
                Also no dashboard is required so *yaaaaay...*.
                To see my help commands use n!help.
                Yours truly
                        *Noot Bot*
                """
                )
            em.set_footer(icon_url=self.client.user.avatar_url, text=f"Noot Bot & {guild.name}")
            await channel.send(embed=em)
        break

  @commands.Cog.listener()  
  async def on_command_error(self, ctx, error):
        c = self.client.get_channel(776583901321101352)
        await ctx.send("<:Nooterror:777330881845133352> Oh no! It looks like I might be missing permissions or you are missing permissions.")
        await c.send(
            f"""
            ```py
            {error}
            ```
            """
        )

def setup(client):
    client.add_cog(Background(client))
    return