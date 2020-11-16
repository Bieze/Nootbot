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
    async def help(self, ctx):
        prefix = get_prefix(ctx.guild, message=ctx.message)
        em = discord.Embed(title="Our help page!", description=f"Current prefix: {prefix}", color=0x1F46A1)
        em.add_field(name="Music", value=
            """
            **Play** → Plays music
            **Loop** → Loops queue
            **Skip** → Skips a song
            **Queue** → Queues a song
            **Disconnect** → Disconnects the bot
            **Pause** → Pauses the song
            **Resume** → Resumes the song\n\n



            """, inline=False
            )
        em.add_field(
            name="Utility",
            value=
            """
            Current prefix = 
            **Prefix** → Change the guild prefix, Requires `Manage guild permissions`
            **Ban** → Bans a member, Requires `Ban members permissions`
            **Kick** → Kicks a member, Requires `Kick members permissions`
            **Unban** → Unbans a user, Requires `Ban members permissions`
            **Clear** → Clears a certain amount, Requires `Manage messages permissions`\n\n



            """, inline=False
            )
        em.add_field(
            name="Member",
            value=
            """
            **AFK** → Go AFK
            **Server** → Check server stats
            **User** → Check you or another user's stats
            **Ping** → Check your latency
            **Meme** → Get a meme from reddit
            **Pup** → Get pup's picture from reddit
            **Kitten** → Get a kitten's picture from reddit\n\n
            [Support server](https://discord.gg/kTbqgSeDBH)        [Bot invite](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot)
            """, inline=False
            )
        em.add_field(
            name="Owner only",
            value=
            """
            **Change** → Changes the bot status
            **Eval** → Run code in discord
            """
        )
        em.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Helpcog(client))
    return