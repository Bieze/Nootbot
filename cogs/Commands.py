import discord
import time
import asyncio
import random
import json
from random import randint
import datetime
import sys
sys.dont_write_bytecode = True
from discord.ext import commands


class Commands(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command(aliases=['afk'])
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


  @commands.command(aliases=['Topic', 'topics', 'Topics', 'topix', 'Topx'])
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


  @commands.command(aliases=['Ping'])
  async def ping(self, ctx):
        before = time.monotonic()
        ping = (time.monotonic() - before) * 1000
        await ctx.send(f"Ping Pong! ```{int(ping)}ms```")


  @commands.command(aliases=['Say'])
  async def say(self, ctx, *, words=None):
        if words == None:
            em = discord.Embed(description="<:Nooterror:777330881845133352> What do you mean magic man?!", inline=False, color=0xff0000)
            await ctx.send(embed=em)
        else:
            await ctx.message.delete()
            await asyncio.sleep(1)
            await ctx.send("{}" .format(words))


  @commands.command(aliases=['Server'])
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


  @commands.command(aliases=['whois', 'userinfo', 'User'])
  async def user(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        if (member.status == discord.Status.online):
            status = "<:Online:769418800718020619> Online"
            pass
        elif (member.status == discord.Status.offline):
            status = "<:Offline:769418801007427594> Offline"
            pass
        elif (member.status == discord.Status.idle):
            status = "<:Idle:769418800940056596> Idle"
            pass
        elif (member.status == discord.Status.dnd):
	        status = "<:DND:769418800843063297> Do Not Disturb"

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
        embed.add_field(name='Status?', value=status)
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