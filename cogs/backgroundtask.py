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

  @commands.Cog.listener()
  async def on_message(message):
      word_list = ['<@731371995979055136>']

      for word in word_list():
          if message.content.count(word) > 0:
              await message.channel.send("Why did you ping me scrub? You know I'm busy barking at my owner noob, my prefix is n!")

def setup(client):
    client.add_cog(Background(client))
    return