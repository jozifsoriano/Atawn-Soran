# Work with Python 3.6
# https://discordapp.com/oauth2/authorize?client_id=603975462305136661&scope=bot

import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

TOKEN = 'NjAzOTc1NDYyMzA1MTM2NjYx.XTnPSg.KVQWzuEbem_HrtkDUg44F23GNJw'
BOT_PREFIX = ("$","|")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!tgif'):
        msg = 'TGIF, {0.author.mention}. LET\'S GET THIS BREAD.'.format(message)
        await message.channel.send(msg, file=discord.File('TGIF.png'))

"""@client.command()
async def tgif():
    msg = 'TGIF, {0.author.mention}. LET\'S GET THIS BREAD.'.format(message)
    await message.channel.send(msg, file=discord.File('TGIF.png'))"""



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
