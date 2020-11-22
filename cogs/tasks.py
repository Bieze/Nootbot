import discord
import traceback
import sys
import asyncio
import json
import math
from discord.ext import tasks, commands


class Background(commands.Cog):
  def __init__(self, client):
    self.client = client  

  @commands.Cog.listener()
  async def on_error(self, ctx, error):
      print(error) 


  @commands.Cog.listener()
  async def on_guild_remove(self, guild):
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('ServerPrefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        

  @commands.Cog.listener()      
  async def on_guild_join(self, guild): 
    with open('ServerPrefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = 'n!'

    with open('ServerPrefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)   
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            perms = discord.Permissions(send_messages=False, read_messages=True)
            await guild.create_role(name="Muted", permissions=perms)
            perms1 = discord.Permissions(send_messages=True, read_messages=True)
            await guild.create_role(name="AFK", permissions=perms1)
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

  @commands.Cog.listener()  
  async def on_command_error(self, ctx, error):
        c = self.client.get_channel(776583901321101352)
        await c.send(error)
        # if command has local error handler, return
        if hasattr(ctx.command, 'on_error'):
            return

        # get the original exception
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send("<:Nooterror:777330881845133352> Command does not exist!")
            print(error)

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '<:Nooterror:777330881845133352> I need the **{}** permission(s) to run this command.'.format(fmt)
            await ctx.send(_message)
            print(error)
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled.')
            print(error)
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("<:Nooterror:777330881845133352> This command is on cooldown, please retry in {}s.".format(math.ceil(error.retry_after)))
            print(error)
            return

        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '<:Nooterror:777330881845133352> You need the **{}** permission(s) to use this command.'.format(fmt)
            await ctx.send(_message)
            print(error)
            return

        if isinstance(error, commands.UserInputError):
            await ctx.send("Invalid input.")
            print(error)
            return

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send('<:Nooterror:777330881845133352> This command cannot be used in direct messages.')
            except discord.Forbidden:
                pass
            print(error)
            return

        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:Nooterror:777330881845133352> You do not have permission to use this command.")
            print(error)
            return

        # ignore all other exception types, but print them to stderr
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)

        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(client):
    client.add_cog(Background(client))
    return