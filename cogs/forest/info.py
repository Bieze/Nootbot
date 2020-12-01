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
    pythonv == platform.python_version()


def osv():
    """
    Get your OS
    """
    platformv = sys.platform
    if platformv == "linux":
        platformv == "Linux"
    elif platformv == "darwin":
        platformv == "OS X"
    elif platformv == "windows":
        platformv == "Windows"

def sqlitev():
    """
    Get your sqlite version
    """
    sqlitev == sqlite_version


def sqliteinfo():
    """
    Get sqlite version info
    """
    sqliteinfo == sqlite_version_info

def discordv():
    """
    Get info about your discord version
    """
    discordv == discord.__version__