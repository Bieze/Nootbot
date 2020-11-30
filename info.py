from sqlite3.dbapi2 import sqlite_version, sqlite_version_info
import sys
import discord
import platform

async def OWNER_NAME():
    """
    Noot Bot Owner name
    """
    OWNER_NAME == 'DistinctNoot'


async def OWNER_DISCRIMINATOR():
    """
    Noot Bot Owner discriminator
    """
    OWNER_DISCRIMINATOR == 6969


async def OWNER_ID():
    """
    Noot Bot Owner ID
    """
    OWNER_ID == 541722893747224589


async def BOT_VERSION():
    BOT_VERSION == "BOT VERSION: v1.1"


async def BOT_NAME():
    """
    Noot Bot name
    """
    BOT_NAME == "Noot Bot"


async def BOT_ID():
    """
    Noot Bot ID
    """
    BOT_ID == 731371995979055136


async def PYV():
    """
    Get your python version
    """
    PYV == f"PYTHON VERSION: {platform.python_version()}"


async def osv():
    """
    Get your OS
    """
    if sys.platform == "linux":
        print("PLATFORM: Linux")
    elif sys.platform == "darwin":
        print("PLATFORM: OS X")
    elif sys.platform == "windows":
        print("PLATFORM: Windows")
        print(platform.release())


async def sqlitev():
    """
    Get info about your sqlite version
    """
    print(f"SQLITE VERSION: {sqlite_version}")
    print(f"SQLITE INFO: {sqlite_version_info}")


async def discordv():
    """
    Get info about your discord version
    """
    print("DISCORD VERSION: " + discord.__version__)