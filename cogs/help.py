import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        #client.remove_command('help')

    #help - gives command list for the bot as a message
    #remove default help to allow for custom help

    @commands.command()
    async def ahelp(self, ctx):
        embed = discord.Embed(title="Atawn bot", description="Atawn, is the name. Commands (put prefix before):", color=0xeee657)
        #embed.add_field(name="", value="", inline=True)
        #embed.add_field(name="setprefix x", value="Set Atawn's prefix to x", inline=True)
        embed.add_field(name="tgif", value="TGIF.", inline=True)
        embed.add_field(name="lol [SummmonerName]", value="Gives LoL information for [SummonerName], such as level, rank, and winrate for soloq.", inline=True)
        embed.add_field(name="8ball [Question]", value="Ask the magic 8ball a [Question] and allow it to predict your fortune!", inline=True)
        embed.add_field(name="clear [x]", value="clears the [x] previous messages from the channel it is called from.", inline=True)
        embed.add_field(name="kick [member] [reason]", value="kicks [member] from the server and informs them with a [reason]", inline=True)
        embed.add_field(name="ban [member] [reason]", value="bans [member] from the server and informs them with a [reason]", inline=True)
        embed.add_field(name="ahelp", value="Shows this message", inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
