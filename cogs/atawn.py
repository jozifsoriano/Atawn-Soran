import discord
import random
from discord.ext import commands

class Atawn(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.counter = 0

    #tgif - Thank god it's Friday
    @commands.command(aliases = ['TGIF','anton'])
    async def atawn(self, ctx):
        await ctx.channel.purge(limit=1)
        msg = f"TGIF, {ctx.author.mention}. LET\'S GET THIS MF BREAD."
        #await ctx.send(msg, file=discord.File('TGIF.png'))
        await ctx.send(msg, file=discord.File('TGIF2.jpg'))

    #luke - Oh no mans got got again
    @commands.command()
    async def luke(self, ctx):
        await ctx.channel.purge(limit=1)
        self.counter += 1
        msg = f"Aw shit, Luke's gotten got {self.counter} time(s)."
        await ctx.send(msg, file=discord.File('luke.png'))

    #john - spits fun facts about the man, the myth, the legend
    @commands.command()
    async def john(self, ctx):
        responses = ["John's full name is actually John Mark Lunes Martes Miercoles Jueves Viernes Sabado Dominguez",
                    "John once won a fishing competition in WoW classic. He reeled in Onyxia!",
                    "John loves to hike. He stated \"I love the beauftiful scenery. It's a great outlet for relieving stress. Every hike, I make sure to come prepared wearing 3 layers of clothes, including a thermal rainjacket and Timberlands. I usually carry a backpack with 3 days supply food and water, a gas-powered grill, 2 gas canisters, a frying pan, bottle opener, charcoal, a tent, a lantern, a headlamp, extra batteries (4xAA, 8xAAA, 2x9v), a sleeping bag, a thermal blanket, a pillow, a hammock, firewood, an axe, a chainsaw, duct tape, rope, a hammer, a leatherman multi-tool, 2000ct matchbook, a lighter, binoculars, portable phone charger, solar panel, desktop PC, keyboard and mouse, and dual monitors. I know this seems like I carry a lot for a 3-hour hike, but honestly, it's still way easier than carrying Anton.\""]
        embed = discord.Embed(title="LUNCHMUNCHIES", description="the goat circa '94", color=0xFFFFFF)
        embed.add_field(name="Did you know?", value = random.choice(responses))
        await ctx.send(embed=embed)

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
