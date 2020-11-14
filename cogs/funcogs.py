import discord
import praw
import random
from discord.ext import commands
client = commands

class redcmds(commands.Cog):
  def __init__(self, client):
    self.client = client

    reddit = praw.Reddit(client_id='c_85u5DZ793OFQ',
                     client_secret='iBBJIhWmv6uB3E6R7UNlgC7t8Go',
                     username = "Electronbot123",
                     password = "Electronbot123",
                     user_agent = "Memes")

    @client.command(aliases=['meme'])
    async def memes(ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []

        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name, colour=0x1F46A1)

        em.set_image(url = url)

        await ctx.send(embed= em)

    @client.command(aliases=['kittens'])
    async def kitten(ctx):
        subreddit = reddit.subreddit("kittens")
        all_subs = []

        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name, colour=0x1F46A1)

        em.set_image(url = url)

        await ctx.send(embed = em)

    @client.command(aliases=['pups'])
    async def pup(ctx):
        subreddit = reddit.subreddit("rarepuppers")
        all_subs = []

        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name, colour=0x1F46A1)

        em.set_image(url = url)

        await ctx.send(embed = em)


def setup(client):
    client.add_cog(redcmds(client))
    return