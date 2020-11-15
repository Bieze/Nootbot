import discord
from discord.utils import get
from discord.ext import commands

class Background(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    em = discord.Embed(title="Uh Oh!", description="<:Nooterror:777330881845133352> [Something went wrong! The problem has been reported](https://discord.gg/BFMueAWxKW.)", color=0xff0000)
    await ctx.send(embed=em)
    print(error)

    channel = self.client.get_channel(776583901321101352)
    await channel.send(
f"""
```py
{error}
```
""")

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            perms = discord.Permissions(send_messages=False, read_messages=True)
            await guild.create_role(name="Muted", permissions=perms)
            em = discord.Embed(
                title="Thanks for invting me into your server!", color=0x8A2BE2)
            em.set_thumbnail(url=guild.icon_url)
            em.add_field(
                name="Here is my thank you note",
                value=


                """
                Thanks for inviting me into your server!
                Consider [adding me](https://discord.com/api/oauth2/authorize?client_id=731371995979055136&permissions=8&scope=bot) to other servers to help get me verified
                and so others can have an awesome bot like me!
                Also no dashboard is required so *yaaaaay...*.
                To see my help commands use n!help.
                Yours truly
                        *Noot Bot*
                """
                )
            em.set_footer(icon_url=self.client.user.avatar_url, text=f"Noot Bot & {guild.name}")
            await channel.send(embed=em)
        break
    

def setup(client):
    client.add_cog(Background(client))
    return