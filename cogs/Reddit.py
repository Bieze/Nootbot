import discord
import praw
from discord.ext import commands
import asyncio
import random
from random import randint
import sys
import os
sys.dont_write_bytecode = True
from discord.ext.commands import BucketType, cooldown
from discord.ext.commands import CommandOnCooldown

reddit = praw.Reddit(client_id='c_85u5DZ793OFQ',
                     client_secret='iBBJIhWmv6uB3E6R7UNlgC7t8Go',
                     username = "Electronbot123",
                     password = "Electronbot123",
                     user_agent = "Memes")




class Reddit(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.all_subs = []


    @commands.command(aliases=['meme'])
    @commands.cooldown(1, 10, BucketType.user)
    async def memes(self, ctx):
        subreddit = reddit.subreddit("memes")
        all_subs = []
        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
    
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}')
        await ctx.send(embed=embed)



    @memes.error
    async def memes_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            msg = '<:Nooterror:777330881845133352> You are on meme cooldown try again in: {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error


    @commands.command(aliases=['puppy','dog'])
    @commands.cooldown(1, 10, BucketType.user)
    async def pup(self, ctx):
        subreddit = reddit.subreddit("puppies")
        all_subs = []

        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}')
        await ctx.send(embed=embed)


    
    @pup.error
    async def pup_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            msg = '<:Nooterror:777330881845133352> You are on pup cooldown try again in: {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error


    @commands.command(aliases=['Cat','feline'])
    @commands.cooldown(1, 10, BucketType.user)
    async def kitten(self, ctx):
        subreddit = reddit.subreddit("kittens")
        all_subs = []

        hot = subreddit.hot(limit = 50)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        comments = random_sub.comments
        upvote = random_sub.upvote_ratio
        
        author = random_sub.author
        sub = random_sub.subreddit

        embed = discord.Embed(title = name, colour=randint(0, 0xffffff))

        embed.set_image(url = url)
        embed.set_author(name=f'Posted by {author} from r/{sub}')
        embed.set_image(url=url)
        embed.set_footer(text=f'\t💬 {len(comments)}    ⇅ {upvote}')
        await ctx.send(embed=embed)



    @kitten.error
    async def kitten_error(self, ctx, error):
        if isinstance(error, CommandOnCooldown):
            msg = '<:Nooterror:777330881845133352> You are on kitten cooldown try again in: {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error

def setup(client):
    client.add_cog(Reddit(client))
    return