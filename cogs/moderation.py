import discord
import datetime
import asyncio
import json
import random
from datetime import date
import time
import sys
import os
import sqlite3
sys.dont_write_bytecode = True
from random import randint
from discord.utils import get
from discord.ext import commands

color = 0x7b68ee




class moderation(commands.Cog):
  def __init__(self, client):
    self.client = client


  #@commands.command()
  #async def warn(self, ctx, member : discord.Member, reason="Non provided"):
    #db = sqlite3.connect("Warnings.sqlite")
    #cursor = db.cursor()
    #cursor.execute(f"SELECT reason FROM main WHERE member_id = {member.id} AND guild_id = {ctx.guild.id}")
    #result = cursor.fetchone()


  @commands.command()
  async def shutdown(self, ctx):
    if ctx.author.id == 731371995979055136:
      await self.client.logout()

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.User=None, *, reason="Nothing"):
      if member == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
        return
      guild = self.client.get_guild(ctx.guild.id)
      await ctx.message.delete()
      if guild.get_member(member.id) is not None:
        c = await member.create_dm()
        await c.send(f"You have been banned from {ctx.guild.name} for: {reason}" .format(reason))
        em = discord.Embed(description=f"<:Nootsuccess:777332367853355009> Banned {member.name}{member.discriminator}", inline=False, color=0x32CD32)
        await ctx.guild.ban(user=member, reason=reason)
        await ctx.send(embed=em)
      elif member.bot is True:
        e = discord.Embed(description="<:Nooterror:777330881845133352> Cannot ban a bot", inline=False, color=0xff0000)
        await ctx.send(embed=e)
      else:
        username = await self.client.fetch_user(int(member.id))
        user = discord.Object(id=member.id)
        await ctx.guild.ban(user=user, reason=reason)
        em = discord.Embed(description=f"<:Nootsuccess:777332367853355009> Banned {username}", inline=False, color=0x32CD32)
        await ctx.send(embed=em)




      #else:
        #try:
          #guild = self.client.get_guild(ctx.guild.id)
          #channel = member.create_dm()
          #await channel.send(f"You have been banned from {ctx.guild.name} for {reason}" .format(reason))
          #await ctx.guild.ban(user=member, reason=reason)
        #except:
          #print("User in guild")
        #finally:
          #try:
        #username = await self.client.fetch_user(int(member))
        #user = discord.Object(id=member)
        #await ctx.guild.ban(user=member)
        #await ctx.message.delete()
        #await ctx.guild.ban(user=user, reason=reason)
        #em=discord.Embed(description=f"<:Nootsuccess:777332367853355009> Banned {username}", inline=False, color=0x32CD32)
        #await ctx.send(embed=em)
      
    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.User=None, *, reason="Nothing"):
    if member == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
    elif member.bot is True:
        e = discord.Embed(description="<:Nooterror:777330881845133352> Cannot kick a bot", inline=False, color=0xff0000)
        await ctx.send(embed=e)
    else:
        await ctx.message.delete()
        await ctx.guild.kick(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootsuccess:777332367853355009> Kicked {member.name}", inline=False, color=0x32CD32)
        await ctx.send(embed=em)

        channel = await member.create_dm()
        await channel.send(f"You have been kicked from **{ctx.guild.name} for: **{reason}**" .format(reason))

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, userid=None):
    if userid == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a user!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
        return
    else:
        username = await self.client.fetch_user(int(userid))
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)
        em = discord.Embed(description=f"<:Nootsuccess:777332367853355009> Unbanned {username}", inline=False, color=0x32CD32)
        await ctx.send(embed=em)
        return


  @commands.command(aliases=['silence'])
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member : discord.Member=None):
        role = get(ctx.guild.roles, name="Muted")
        if member == None:
              emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
              await ctx.send(embed=emd)
        else:
              await member.add_roles(role)
              em = discord.Embed(description="<:Nootsuccess:777332367853355009> Muted " + member.name, inline=False, color=0x32CD32)
              await ctx.send(embed=em)

  @commands.command(aliases=['unsilence'])
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member : discord.Member=None):
        role = get(ctx.guild.roles, name="Muted")
        if member == None:
              emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
              await ctx.send(embed=emd)
        else:
              await member.remove_roles(role)
              em = discord.Embed(description="<:Nootsuccess:777332367853355009> Unmuted " + member.name, inline=False, color=0x32CD32)
              await ctx.send(embed=em)


# Unmute and Mute commands up for improvements!

  @commands.command()
  async def change(self, ctx, *, status):
      if ctx.author.id == 541722893747224589:
        await self.client.change_presence(
	    activity=discord.Activity(
	        type=discord.ActivityType.watching,
	        name="{}" .format(status)))
        await ctx.send("<:Nootsuccess:777332367853355009> Changed status!")
      else:
          em = discord.Embed(description="<:Nooterror:777330881845133352> Sorry, but you don't have permissions to change the bot status!")
          await ctx.send(embed=em)

  @commands.command()
  @commands.has_permissions(manage_guild=True)
  async def prefix(self, ctx, prefix):
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)

    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('ServerPrefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    embed = discord.Embed(
        color=discord.Color.green(),
        title="**Success**",
        description=f"Prefix changed to `{prefix}`"
    )
    embed.set_author(name="Prefix Command.", icon_url=self.client.user.avatar_url)
    embed.set_footer(text=f"Requested by: {ctx.message.author} | Requested at {current_time}")
    message = await ctx.send(embed=embed)
    await message.add_reaction(str('✅'))

  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=1):
      await ctx.channel.purge(limit=amount+1)
      await ctx.send(f"<:Nootsuccess:777332367853355009> Cleared {amount} messages!")
      await asyncio.sleep(5)
      await ctx.channel.purge(limit=1) 


  @commands.group(invoke_without_command=True)
  async def config(self, ctx):
      color = 0x7b68ee
      em = discord.Embed(
          title="Welcome config",
          description="Configure your welcome commands",
          color=color)
      em.add_field(name="delguild", value="Delete the guild from the database")
      em.add_field(name="welcome-config", value="Configure the welcome message")
      em.add_field(name="goodbye-config", value="Configure the goodbye message")
      em.add_field(name="Channel-config", value="Configure the welcome channel")
      em.add_field(name="Setguild", value="Set the guild for welcome message")
      em.add_field(name="config-cheats", value="See the cheat sheet")
      await ctx.send(embed=em)


  @commands.command(aliases=['channel-config', 'c-c', 'cc'])
  @commands.has_permissions(manage_guild=True)
  async def channel_config(self, ctx, channel:discord.TextChannel):
    db = sqlite3.connect("Welcome.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if result is None:
      sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
      val = (ctx.guild.id, channel.id)
      await ctx.send(f"Channel has been set as {channel.mention}")
    elif result is not None:
      sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
      val = (channel.id, ctx.guild.id)
      await ctx.send(f"<:Nootsuccess:777332367853355009> Channel has been set as {channel.mention}")
    cursor.execute(sql, val)
    db.commit()
    cursor.close
    db.close



  @commands.command(aliases=['welcome-config', 'w-c', 'wc'])
  @commands.has_permissions(manage_guild=True)
  async def welcome_config(self, ctx, *, text):
    db = sqlite3.connect("Welcome.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT welcome FROM main WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if result is None:
      sql = ("INSERT INTO main(guild_id, welcome) VALUES(?,?)")
      val = (ctx.guild.id, text)
      await ctx.send(f"Set the welcome message.")
    elif result is not None:
      sql = ("UPDATE main SET welcome = ? WHERE guild_id = ?")
      val = (text, ctx.guild.id)
      await ctx.send(f"<:Nootsuccess:777332367853355009> Set the welcome message.")
    cursor.execute(sql, val)
    db.commit()
    cursor.close
    db.close


  @commands.command(aliases=['goodbye-config', 'g-c', 'gc'])
  @commands.has_permissions(manage_messages=True)
  async def goodbye_config(self, ctx, *, text):
    db = sqlite3.connect("Welcome.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT goodbye FROM main WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if result is None:
      sql = ("INSERT INTO main(guild_id, goodbye) VALUES(?,?)")
      val = (ctx.guild.id, text)
      await ctx.send(f"Set the goodbye message.")
    elif result is not None:
      sql = ("UPDATE main SET goodbye = ? WHERE guild_id = ?")
      val = (text, ctx.guild.id)
      await ctx.send(f"<:Nootsuccess:777332367853355009> Set the goodbye message.")
    cursor.execute(sql, val)
    db.commit()
    cursor.close
    db.close


  @commands.command(aliases=['delguild-config', 'd-c'])
  @commands.has_permissions(manage_messages=True)
  async def delguild(self, ctx):
    db = sqlite3.connect("Welcome.sqlite")
    cursor = db.cursor()
    cursor.execute(f"SELECT goodbye FROM main WHERE guild_id = {ctx.guild.id}")
    result = cursor.fetchone()
    if result is None:
      await ctx.send("This guild is not in the database")
    else:
      sql = (f"DELETE FROM main WHERE guild_id = {ctx.guild.id}")
      await ctx.send("<:Nootsuccess:777332367853355009> Removed guild from database.")
      cursor.execute(sql)
      db.commit()
      cursor.close
      db.close

  @commands.command(aliases=['config-cheats', 'cheats-config'])
  async def cheatsheet(self, ctx):
    em = discord.Embed(color=color)
    em.add_field(name="mention", value="mention a member")
    em.add_field(name="user", value="member name")
    em.add_field(name="members", value="567 member")
    await ctx.send(embed=em)


def setup(client):
    client.add_cog(moderation(client))
    return