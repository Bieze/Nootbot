import discord
import json
import sys
import os
sys.dont_write_bytecode = True
from discord.ext import commands


class Helpcog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx, category=None):
        if category == None:
            category = await reg(self, ctx)
        elif category == "Member":
            category = await mem(self, ctx)
        elif category == "member":
            category = await mem(self, ctx)
        elif category == "music":
            category = await Music(self, ctx)
        elif category == "Music":
            category = await Music(self, ctx)
        elif category == "Utility":
            category = await Utils(self, ctx)
        elif category == "Utils":
            category = await Utils(self, ctx)
        elif category == "utility":
            category = await Utils(self, ctx)
        elif category == "utils":
            category = await Utils(self, ctx)
        elif category == "mod":
            category = await Utils(self, ctx)
        elif category == "Mod":
            category = await Utils(self, ctx)
        elif category == "moderation":
            category = await Utils(self, ctx)
        elif category == "Moderation":
            category = await Utils(self, ctx)
        else:
            await ctx.send("<:Nooterror:777330881845133352> Help page not found!")

color = 0x7b68ee

async def Music(self, ctx):
    em = discord.Embed(
        title="Music commands",
        description=
        f"""
        Current prefix: **>**
        """, color=color
    )
    em.add_field(name="🎵 Play", value="Play music")
    em.add_field(name="🔄 Loop", value="Loop music")
    em.add_field(name="➡️ Skip", value="Skip music")
    em.add_field(name="⏺️ Queue", value="Queue music")
    em.add_field(name="▶️ Pause", value="Pause music")
    em.add_field(name="⏸ Resume", value="Resume music")
    em.add_field(name="👋 Disconnect", value="Disconnect bot")
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)


async def mem(self, ctx):
    em = discord.Embed(
        title="The best commands",
        value=
        f"""
        Current prefix: **>**
        """, color=color
    )
    em.add_field(name="😂 Meme", value="Reddit memes")
    em.add_field(name="🐶 Pup", value="Puppy pictures")
    em.add_field(name="🐱 Kitten", value="Kitten pictures")
    em.add_field(name="⌨️ AFK", value="Go AFK")
    em.add_field(name="🖥️ Ping", value="Check ping")
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)


async def Utils(self, ctx):
    em = discord.Embed(
        title="The *classified* commands",
        description=
        f"""
        Current prefix: **>**
        """, color=color
    )
    em.add_field(name="👮 Ban", value="Ban a member")
    em.add_field(name="👮 Kick", value="Kick a member")
    em.add_field(name="👮 Unban", value="Unban a user")
    em.add_field(name="♻️ Clear", value="Delete messages")
    em.add_field(name="👋 welcome-config", value="Configure your welcome message")
    em.add_field(name="👋 goodbye-config", value="Configure your goodbye message")
    em.add_field(name="👋 channel-config", value="Configure your greeting channel")
    em.add_field(name="🧹 delguild", value="Delete the guild from the database")
    em.set_footer(icon_url=self.client.user.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=em)



async def reg(self, ctx):
    em = discord.Embed(
        title="Help page",
        description=f"Current prefix: **>**\nTo select a category do help (categoryname)", color=color)
    em.add_field(name="🎵 Music", value="Music commands")
    em.add_field(name="⚒️ Utility", value="Utility commands")
    em.add_field(name="🤹‍♂️ Member", value="Member commands")
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)

def setup(client):
    client.add_cog(Helpcog(client))
    return