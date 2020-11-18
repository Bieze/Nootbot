import discord
import json
from discord.ext import commands


def get_prefix(client, message):
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


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

async def Music(self, ctx):
    prefix = get_prefix(ctx.guild, message=ctx.message)
    em = discord.Embed(
        title="Music commands",
        description=
        f"""
        Current prefix: {prefix}
        **Play** → Plays music
        **Loop** → Loops queue
        **Skip** → Skips a song
        **Queue** → Queues a song
        **Disconnect** → Disconnects the bot
        **Pause** → Pauses the song
        **Resume** → Resumes the song\n\n

        [Support server](https://discord.gg/kTbqgSeDBH)        [Bot invite](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot)
        """, color=0x7b68ee
        )
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)


async def Utils(self, ctx):
    prefix = get_prefix(ctx.guild, message=ctx.message)
    em = discord.Embed(title="Utility commands",
        description=
        f"""
        Current prefix: {prefix}
        [Support server](https://discord.gg/kTbqgSeDBH)        [Bot invite](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot)
        """, color=0x7b68ee)
    await ctx.send(embed=em)


async def mem(self, ctx):
    prefix = get_prefix(ctx.guild, message=ctx.message)
    em = discord.Embed(
        title="Regular commands",
        description=
        f"""
        Current prefix: {prefix}
        **Server** → Check server stats **User** → Check you or another user's stats
        **Ping** → Check your latency   **Meme** → Get a meme from reddit
        **Pup** → Get pup's picture from reddit **Kitten** → Get a kitten's picture from reddit

        [Support server](https://discord.gg/kTbqgSeDBH)        [Bot invite](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot)
        """, color=0x7b68ee
        )
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)


async def reg(self, ctx):
    prefix = get_prefix(ctx.guild, message=ctx.message)
    em = discord.Embed(
        title="Help page",
        description=f"Current prefix: **{prefix}**\nTo select a category do help (categoryname)", color=0x7b68ee)
    em.add_field(name="🎵 Music", value="Music commands")
    em.add_field(name="⚒️ Utility", value="Utility commands")
    em.add_field(name="🤹‍♂️ Member", value="Member commands")
    em.set_footer(icon_url=self.client.user.avatar_url, text="Requested by " + ctx.author.name)
    await ctx.send(embed=em)

def setup(client):
    client.add_cog(Helpcog(client))
    return