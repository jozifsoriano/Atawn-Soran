import discord
from discord.ext import commands


class Announcements(commands.Cog):

    def __init__(self, client):
        self.client = client

    # minecraft - Details about the minecraft server
    @commands.command()
    async def minecraft(self, ctx):
        embed = discord.Embed(title="Minecraft Server", description="", color=0xFFFFFF)
        embed.add_field(name="MC Eternal 1.12.2 modpack", value = "")
        embed.add_field(name="IP Address", value = "69.12.95.216:25565")
        embed.add_field(name="Venmo", value = "@MSAnthony")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Announcements(client))
