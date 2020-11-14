import discord
from discord.ext import commands

class Background(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    em = discord.Embed(title="Uh Oh!", description="[Something went wrong! The problem has been reported](https://discord.gg/BFMueAWxKW.)", color=0x1F46A1)
    await ctx.send(embed=em)

    channel = self.client.get_channel(776583901321101352)
    await channel.send(
f"""
```py
{error}
```
""")

def setup(client):
    client.add_cog(Background(client))
    return