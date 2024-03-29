# Works with Python 3.8
# https://discordapp.com/oauth2/authorize?client_id=603975462305136661&scope=bot

import discord
import os
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

#tokens and keys
DISC_TOKEN = ''
tokenFile = open('token','r')
while True:
    line = tokenFile.readline()
    if not line:
        break
    splitLine = line.split(':')
    if splitLine[0] == 'disc':
        DISC_TOKEN = splitLine[1]
        break

#Bot info
BOT_PREFIX = ("$")
client = commands.Bot(command_prefix=BOT_PREFIX)


@client.command()
async def load(ctx, extension):
    print(f'\n---\nLoading\n---\n')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    print(f'\n---\nUnloading\n---\n')
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    print(f'\n---\nReloading\n---\n')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#run the client
client.run(DISC_TOKEN)
