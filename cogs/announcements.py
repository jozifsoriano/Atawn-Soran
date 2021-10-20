import discord
from discord.ext import commands


class Announcements(commands.Cog):

    def __init__(self, client):
        self.client = client

    # # tgif - Thank god it's Friday
    # @commands.command(aliases=['TGIF', 'anton'])
    # async def atawn(self, ctx):
    #     await ctx.channel.purge(limit=1)
  


def setup(client):
    client.add_cog(Announcements(client))
