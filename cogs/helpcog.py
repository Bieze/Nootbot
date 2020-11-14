import discord
from discord.ext import commands

class Helpcog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title="Our help page!", color=0x1F46A1)
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
        em.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Helpcog(client))
    return