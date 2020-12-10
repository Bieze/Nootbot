from platform import python_version
from sqlite3.dbapi2 import sqlite_version, sqlite_version_info
import discord
from datetime import datetime
import time
import asyncio
import random
import json
import os
from random import randint
import datetime
import sys
import sqlite3
from forest.info import pythonv
from forest.info import sqlitev
from forest.info import discordv
sys.dont_write_bytecode = True
from discord.ext import commands

starttime = datetime.datetime.utcnow()

color = 0x7b68ee


class Commands(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def noot(self, ctx):
      await ctx.send("<:Noot:786678144747831306>")
    

  @commands.command(aliases=['stats'])
  async def statistics(self, ctx):
      now = datetime.datetime.utcnow()
      elapsed = now - starttime
      seconds = elapsed.seconds
      minutes, seconds = divmod(seconds, 60)
      hours, minutes = divmod(minutes, 60)
      if sys.platform == "linux":
        plat = "Linux"
      elif sys.platform == "darwin":
        plat = "OS X"
      elif sys.platform == "windows":
        plat = "Windows"
      em = discord.Embed(color=color)
      em.set_author(icon_url=self.client.user.avatar_url, name="Noot bot's stats")
      em.add_field(name="Guilds", value=len(self.client.guilds), inline=True)
      em.add_field(name="Status", value="Online", inline=True)
      em.add_field(name="Display name", value=self.client.user.display_name, inline=True)
      em.add_field(name="Discord version", value=discord.__version__, inline=True)
      em.add_field(name="SQLite version", value=sqlite_version, inline=True)
      em.add_field(name="SQLite info", value=sqlite_version_info, inline=True)
      em.add_field(name="OS", value=plat, inline=True)
      em.add_field(name="Python version", value="Python 3.8.3", inline=True)
      em.add_field(name="Running for", value="{}d {}h {}m {}s".format(elapsed.days, hours, minutes, seconds))
      em.set_footer(text=f'Made by DistinctNoot', icon_url=self.client.user.avatar_url)
      await ctx.send(embed=em)


  @commands.command()
  async def AFK(self, ctx, reason=None):
      nick2 = f"[AFK] {ctx.author.display_name}"
      nick1 = nick2.replace('[AFK]', '')
      afk = discord.utils.get(ctx.guild.roles, name = "AFK")
      if afk in ctx.author.roles:
          await ctx.channel.send(f"Welcome back {ctx.author.mention}!")
          await ctx.author.edit(nick=nick1)
          await ctx.author.remove_roles(afk)
      else:
          await ctx.author.edit(nick=nick2)
          await ctx.author.add_roles(afk)
          await ctx.channel.send("I made you AFK " + ctx.author.mention)


  @commands.command(aliases=['topics','topix', 'Topx'])
  async def topic(self, ctx):
      questions = [
          'What is your favorite game?',
          'What changed your child hood?',
          'What was the most significant change in your life?',
          'What is your favorite food?',
          'Are you vegan?',
          'What is your favorite animal?',
          'What do you like to do?',
          'Favorite school subject?',
          'Have you ever seen snow?',
          'Have you ever tried dragon fruit?',
          'What languages do you speak?',
          'Where are you from?',
          'Do you code? if so, in which languages?',
          'What holidays do you celebrate?',
          'Favorite artist/Favorite song?',
          'Favorite TV show',
          'Where are you from?',
          'What advice do you have for the next generation?',
          'Do you like anime?']

      await ctx.send(f'topic: **{random.choice(questions)}**')


  @commands.command()
  async def ping(self, ctx):
        before = time.monotonic()
        ping = (time.monotonic() - before) * 1000
        await ctx.send(f"Ping Pong! ```{int(ping)}ms```")


  @commands.command()
  async def say(self, ctx, *, words=None):
        if words == None:
            em = discord.Embed(description="<:Nooterror:777330881845133352> What do you mean magic man?!", inline=False, color=0xff0000)
            await ctx.send(embed=em)
        else:
            await ctx.message.delete()
            await asyncio.sleep(1)
            await ctx.send("{}" .format(words))


  @commands.command()
  async def server(self, ctx):
        guild = ctx.guild
        em = discord.Embed(
			title="Information about " + ctx.guild.name,
			color=randint(0, 0xffffff),
			timestamp=datetime.datetime.utcnow())
        em.set_thumbnail(url=ctx.guild.icon_url)
        em.add_field(name="Created at?", value=guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p'), inline=True)
        em.add_field(name="Members?", value=guild.member_count)
        em.add_field(name="Owner?", value=guild.owner)
        em.add_field(name="Verification level?", value=guild.verification_level)
        em.add_field(name="Guild id?", value=guild.id)
        em.set_footer(icon_url=ctx.guild.icon_url, text=f"Requested by {ctx.author.name} at ")
        await ctx.send(embed=em)


  @commands.command(aliases=['whois', 'userinfo'])
  async def user(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        if (member.status == discord.Status.online):
            stat = "<:Online:769418800718020619> Online"
            pass
        elif (member.status == discord.Status.offline):
            stat = "<:Offline:769418801007427594> Offline"
            pass
        elif (member.status == discord.Status.idle):
            stat = "<:Idle:769418800940056596> Idle"
            pass
        elif (member.status == discord.Status.dnd):
	        stat = "<:DND:769418800843063297> Do Not Disturb"

        roles = [role for role in member.roles[:1]]
        embed = discord.Embed(
		    color=randint(0, 0xffffff), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(
		    name="Joined at:",
		    value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(
		    name='Registered at:',
		    value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.add_field(name='Bot?', value=f'{member.bot}')
        embed.add_field(name='Status?', value=stat)
        embed.add_field(name='Top Role?', value=f'{member.top_role}')
        embed.add_field(
		    name=f"Roles ({len(roles)})",
		    value=" ".join([role.mention for role in roles[:1]]))
        embed.set_footer(
		    icon_url=member.avatar_url,
		    text=f'Requested By: {ctx.author.name}')
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Commands(client))
    return