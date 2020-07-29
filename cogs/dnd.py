import json
import random
import discord
from discord.ext import commands
#https://github.com/Miserlou/dnd-tldr

class DnD(commands.Cog):

    def __init__(self, client):
        self.client = client

    def new_char():
        print("hi")
    
    #map - Gets the map for the current campaign
    @commands.command()
    async def map(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send("", file=discord.File('DNDMAP.jpg'))

    #roll - roll a dice ([x]d[y])
    @commands.command()
    async def roll(self, ctx, input: str):
        await ctx.channel.purge(limit=1)
        if(input[1] != 'd'):
            embed = discord.Embed(title="**ERROR**", description=f"Hmmmm......", color =0xf538ff)
            embed.add_field(name = '**Failed to roll: **',value="*roll in format [x]d[y], where x is how many die and y is max roll*",inline=False)
        else:
            x = int(input[0])
            y = int(input[2:])
            embed = discord.Embed(title="**ROOOOOoooooolllll**", description=f"{ctx.author.mention} || *Max: {y}*", color =0xf538ff)
            for i in range (x):
                embed.add_field(name = f'**Dice {i+1}:**',value=f"**{random.randint(1,y)}**",inline=False)
        await ctx.send(embed = embed)
    
    #charhelp - links the players handbook
    @commands.command()
    async def charhelp(self, ctx):
        embed = discord.Embed(title="Player's Handbook 5e", description="How to play this game.")
        embed.add_field(name='Link:',value="https://online.anyflip.com/ofsj/cxmj/mobile/index.html#p=287")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(DnD(client))