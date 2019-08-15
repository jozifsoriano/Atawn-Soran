# Work with Python 3.6
# https://discordapp.com/oauth2/authorize?client_id=603975462305136661&scope=bot

import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = 'NjAzOTc1NDYyMzA1MTM2NjYx.XTszsA.28FtI99Qh25mbrFjyJCmzx-RXGY'
BOT_PREFIX = ("$")
client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')

#@client.command()
#async def setprefix(ctx, x: str):
#    BOT_PREFIX = x
#    await ctx.send('Atawn\'s prefix is now' + x + '.')

@client.command()
async def tgif(ctx):
    msg = 'TGIF, '+ ctx.author.mention +'. LET\'S GET THIS BREAD.'
    await ctx.send(msg, file=discord.File('TGIF.png'))

client.remove_command('help')

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Atawn bot", description="Atawn, is the name. Commands (put prefix before):", color=0xeee657)
    #embed.add_field(name="setprefix x", value="Set Atawn's prefix to x", inline=True)
    embed.add_field(name="tgif", value="TGIF.", inline=True)
    embed.add_field(name="help", value="Gives this message", inline=True)
    await ctx.send(embed=embed)


client.run(TOKEN)
