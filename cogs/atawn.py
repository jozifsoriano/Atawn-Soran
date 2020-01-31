import discord
import random
from discord.ext import commands

class Atawn(commands.Cog):

    def __init__(self, client):
        self.client = client

    #tgif - Thank god it's Friday
    @commands.command()
    async def tgif(self, ctx):
        #msg = 'TGIF, '+ ctx.author.mention +'. LET\'S GET THIS BREAD.'
        msg = f"TGIF, {ctx.author.mention}. LET\'S GET THIS MF BREAD."
        await ctx.send(msg, file=discord.File('TGIF.png'))

    #8ball - ask the magic 8 ball a yes or no question, and it shall answer
    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        embed = discord.Embed(title="Magic 8 Ball", description=question, color=0x000000)
        #embed.add_field(name="Question: ", value=question)
        embed.add_field(name="The Magic 8 Ball says", value = random.choice(responses))
        await ctx.send(embed=embed)

    #setprefix - Change Atawn bot prefix to designated symbol
    #@commands.command()
    #async def setprefix(ctx, x: str):
    #    client = commands.Bot(command_prefix=x)
    #    await ctx.send('Atawn\'s prefix is now ' + x + '.')

def setup(client):
    client.add_cog(Atawn(client))