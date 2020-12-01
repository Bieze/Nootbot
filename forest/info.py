from sqlite3.dbapi2 import sqlite_version, sqlite_version_info
import sys
sys.dont_write_bytecode=True
import discord
import platform

def OWNER_NAME():
    """
    Noot Bot Owner name
    """
    OWNER_NAME == 'DistinctNoot'


def OWNER_DISCRIMINATOR():
    """
    Noot Bot Owner discriminator
    """
    OWNER_DISCRIMINATOR == 6969


def OWNER_ID():
    """
    Noot Bot Owner ID
    """
    OWNER_ID == 541722893747224589


def BOT_VERSION():
    BOT_VERSION == "BOT VERSION: v1.1"


def BOT_NAME():
    """
    Noot Bot name
    """
    BOT_NAME == "Noot Bot"


def BOT_ID():
    """
    Noot Bot ID
    """
    BOT_ID == 731371995979055136


def pythonv():
    """
    Get your python version
    """
    pythonv == f"PYTHON VERSION: {platform.python_version()}"


def osv():
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


def sqlitev():
    """
    Get info about your sqlite version
    """
    print(f"SQLITE VERSION: {sqlite_version}")
    print(f"SQLITE INFO: {sqlite_version_info}")


def discordv():
    """
    Get info about your discord version
    """
    print("DISCORD VERSION: " + discord.__version__)