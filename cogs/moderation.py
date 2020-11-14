import discord
import datetime
import asyncio
from discord.ext import commands

class moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.User, reason="Nothing"):
        await ctx.message.delete()
        await ctx.guild.ban(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootcheck:776557486210940948> Banned {member.name}", color=0x1F46A1)
        await ctx.send(embed=em)
        
        channel = member.create_dm()
        await channel.send(f"You have been banned from {ctx.guild_name} for {reason}")

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.User, reason="Nothing"):
        await ctx.message.delete()
        await ctx.guild.kick(user=member, reason=reason)
        em=discord.Embed(description=f"<:Nootcheck:776557486210940948> Kicked {member.name}", color=0x1F46A1)
        await ctx.send(embed=em)

        channel = member.create_dm()
        await channel.send(f"You have been kicked from {ctx.guild_name} for {reason}")

    
  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, id):
        member = await self.client.fetch_user(id)
        await ctx.guild.unban(user=member)
        em = discord.Embed(description="<:Nootcheck:776557486210940948> Unbanned the user", color=0x1F46A1)
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
		    color=0x1F46A1, timestamp=datetime.datetime.utcnow())
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
  async def say(self, ctx, *, words):
        await ctx.message.delete()
        await asyncio.sleep(1)
        await ctx.send("{}" .format(words))


  @commands.command()
  async def server(self, ctx):
        guild = ctx.guild
        em = discord.Embed(
			title="Information about " + ctx.guild.name,
			color=0x1F46A1,
			timestamp=datetime.datetime.utcnow())
        em.set_thumbnail(url=ctx.guild.icon_url)
        em.add_field(name="Created at?", value=guild.created_at.strftime('%a, %#d %B %Y, %I:%M %p'), inline=True)
        em.add_field(name="Members?", value=guild.member_count)
        em.add_field(name="Owner?", value=guild.owner)
        em.add_field(name="Verification level?", value=guild.verification_level)
        em.add_field(name="Guild id?", value=guild.id)
        em.set_footer(icon_url=ctx.guild.icon_url, text=f"Requested by {ctx.author.name} at ")
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(moderation(client))
    return