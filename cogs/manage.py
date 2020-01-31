import discord
from discord.ext import commands

class Manage(commands.Cog):

    def __init__(self, client):
        self.client = client
    #EVENTS
    #event - Succesful bot Login
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(self.client.user.name)
        print(self.client.user.id)
        print('----------')
        #await ctx.send("What's good mother fuckers.")

    #event - a member has joined
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server.')

    #event - a member has joined
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    #COMMANDS
    #clear - clears the previous [amount] of messages, default just the command
    @commands.command()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    #kick - kicks [member] from the server for the following [reason]
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)

    #ban - bans [member] from the server for the following [reason]
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)

    #unban - unbans [member] from the server
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")

def setup(client):
    client.add_cog(Manage(client))
