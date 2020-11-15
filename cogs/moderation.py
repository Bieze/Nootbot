import discord
import datetime
import asyncio
import random
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
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", color=0xff0000)
        await ctx.send(embed=emd)
    else:
        await ctx.message.delete()
        await ctx.guild.ban(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootsuccess:777332367853355009> Banned {member.name}", color=0x32CD32)
        await ctx.send(embed=em)
        
        channel = await member.create_dm()
        await channel.send(f"You have been banned from {ctx.guild.name} for {reason}" .format(reason))

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.User=None, *, reason="Nothing"):
    if member == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", color=0xff0000)
        await ctx.send(embed=emd)
    else:
        await ctx.message.delete()
        await ctx.guild.kick(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootsuccess:777332367853355009> Kicked {member.name}", color=0x32CD32)
        await ctx.send(embed=em)

        channel = await member.create_dm()
        await channel.send(f"You have been kicked from {ctx.guild.name} for {reason}" .format(reason))

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, userid=None):
    if id == None:
        emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a user!", color=0xff0000)
        await ctx.send(embed=emd)
    else:
        username = await self.client.fetch_user(int(userid))
        user = discord.Object(id=userid)
        await ctx.guild.unban(user)
        em = discord.Embed(description=f"<:Nootsuccess:777332367853355009> Unbanned the {username}", color=0x32CD32)
        await ctx.send(embed=em)

  @commands.command(aliases=['whois', 'userinfo'])
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

  @commands.command()
  async def say(self, ctx, *, words=None):
    if words == None:
        em = discord.Embed(description="<:Nooterror:777330881845133352> What do you mean magic man?!", color=0xff0000)
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

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member : discord.Member=None):
        role = get(ctx.guild.roles, name="Muted")
        if member == None:
              emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", color=0xff0000)
              await ctx.send(embed=emd)
        else:
              await member.add_roles(role)
              em = discord.Embed(description="<:Nootsuccess:777332367853355009> Muted " + member.name, color=0x32CD32)
              await ctx.send(embed=em)

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member : discord.Member=None):
        role = get(ctx.guild.roles, name="Muted")
        if member == None:
              emd = discord.Embed(description="<:Nooterror:777330881845133352> Please specify a member!", color=0xff0000)
              await ctx.send(embed=emd)
        else:
              await member.remove_roles(role)
              em = discord.Embed(description="<:Nootsuccess:777332367853355009> Unmuted " + member.name, color=0x32CD32)
              await ctx.send(embed=em)


def setup(client):
    client.add_cog(moderation(client))
    return