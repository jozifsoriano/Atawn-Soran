import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #event
    #@commands.Cog.listener()
    #async def on_ready(self):
        #print('Logged in')

    #command
    @commands.command()
    async def ping(self,ctx):
        print(f'USERNAME: {str(ctx.message.author)}')
        print(f'GUILD: {str(ctx.message.author.guild)}')
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms.')

def setup(client):
    client.add_cog(Example(client))
