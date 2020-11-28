import discord
import traceback
import os
import asyncio
import json
import math
import sqlite3
import sys
sys.dont_write_bytecode = True
from discord.ext import tasks, commands
from discord.ext.commands import MissingPermissions


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
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            print(error)
            return

        # get the original exception
        error = getattr(error, 'original', error)


        if isinstance(error, commands.CommandNotFound):
            await ctx.send("<:Nooterror:777330881845133352> Command does not exist")

        elif isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '<:Nooterror:777330881845133352> You need the **{}** permission(s) to use this command.'.format(fmt)
            await ctx.send(_message)
            return
        else:
            print(error)
            await ctx.send("<:Nooterror:777330881845133352> I could be missing permissions.")

  @commands.Cog.listener()
  async def on_member_join(self, member):
      db = sqlite3.connect("Welcome.sqlite")
      cursor = db.cursor()
      cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {member.guild.id}")
      result = cursor.fetchone()
      if result is None:
          return
      else:
          mention = member.mention
          members = len(list(member.guild.members))
          user = member.name
          guild = member.guild
          cursor.execute(f"SELECT welcome FROM main WHERE guild_id = {guild.id}")
          result1 = cursor.fetchone()

          channel = self.client.get_channel(int(result[0]))

          await channel.send(str(result1[0]) .format(members=members, mention=mention, user=user, guild=guild))
      #if member.guild.id == 776556035921412136:
        #c = self.client.get_channel(776556035921412139)
        #await c.send(f"Please welcome **{member.mention}**.")
        #await member.add_roles(777284452971708416)


  @commands.Cog.listener()
  async def on_member_remove(self, member):
      db = sqlite3.connect("Welcome.sqlite")
      cursor = db.cursor()
      cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {member.guild.id}")
      result = cursor.fetchone()
      if result is None:
          return
      else:
          mention = member.mention
          members = len(list(member.guild.members))
          user = member.name
          guild = member.guild
          cursor.execute(f"SELECT goodbye FROM main WHERE guild_id = {guild.id}")
          result1 = cursor.fetchone()

          channel = self.client.get_channel(int(result[0]))

          await channel.send(str(result1[0]) .format(members=members, mention=mention, user=user, guild=guild))
          #c = self.client.get_channel(776556035921412139)
          #await c.send(f"**{member.name} left.")


def setup(client):
    client.add_cog(Background(client))
    return