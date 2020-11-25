import discord
import praw
from discord.ext import commands
import asyncio
import random
from random import randint
import sys
sys.dont_write_bytecode = True
from discord.ext.commands import BucketType, cooldown

reddit = praw.Reddit(client_id='c_85u5DZ793OFQ',
                     client_secret='iBBJIhWmv6uB3E6R7UNlgC7t8Go',
                     username = "Electronbot123",
                     password = "Electronbot123",
                     user_agent = "Memes")

class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.all_subs = []


    @commands.command(aliases=['meme', 'Memes', 'Meme'])
    @commands.cooldown(1, 10, BucketType.user)
    async def memes(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []

        hot = subreddit.hot(limit = 50000)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        up = random_sub.score
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
        await ctx.send(embed=embed)


    @commands.command(aliases=['Pup', 'Puppy', 'puppy', 'Dog', 'dog'])
    @commands.cooldown(1, 10, BucketType.user)
    async def pup(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []

        hot = subreddit.hot(limit = 50000)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        up = random_sub.score
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
        await ctx.send(embed=embed)


    @commands.command(aliases=['Kitten', 'Cat', 'cat', 'feline', 'Feline'])
    @commands.cooldown(1, 10, BucketType.user)
    async def kitten(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []

        hot = subreddit.hot(limit = 50000)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        up = random_sub.score
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}    ↑ {up}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reddit(client))
    return