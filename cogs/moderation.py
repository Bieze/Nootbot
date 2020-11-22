import discord
import datetime
import asyncio
import json
import random
from datetime import date
import time
from random import randint
from discord.utils import get
from discord.ext import commands

class moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.User=None, *, reason="Nothing"):
    if member == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
    elif member == ctx.guild_owner:
        await ctx.send("<:Nooterror:777330881845133352> Cannot ban guild owner!")
    else:
        await ctx.message.delete()
        await ctx.guild.ban(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootsuccess:777332367853355009> Banned {member.name}", inline=False, color=0x32CD32)
        await ctx.send(embed=em)
        
        channel = await member.create_dm()
        await channel.send(f"You have been banned from **{ctx.guild.name}** for: **{reason}**" .format(reason))

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.User=None, *, reason="Nothing"):
    if member == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
    elif member == ctx.guild_owner:
        await ctx.send("<:Nooterror:777330881845133352> Cannot kick guild owner!")
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
    if id == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a user!", inline=False, color=0xff0000)
        await ctx.send(embed=emd)
    else:
        username = await self.client.fetch_user(int(userid))
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)
        em = discord.Embed(description=f"<:Nootsuccess:777332367853355009> Unbanned the {username}", inline=False, color=0x32CD32)
        await ctx.send(embed=em)


  @commands.command()
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

  @commands.command()
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

def setup(client):
    client.add_cog(moderation(client))
    return