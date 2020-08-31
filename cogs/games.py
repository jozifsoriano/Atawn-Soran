import discord
import random
import json
from discord.ext import commands

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    #write the user, tag, and the game it's for
    def write_to_json(self, user, tag, game):
        flag = False
        f = {}
        f['user'] = []
        with open('games.json') as json_file:
            f = json.load(json_file)
            for u in f['user']:
                if user == u['name']:
                    flag = True #user exists dont append
                    u[game]=tag
        if not flag: #user does not exist in bank, append
            f['user'].append({
                'name': user,
                game: tag
            })
        with open('games.json', 'w') as outfile:
            json.dump(f, outfile)

    #fallguy - Keeps track of the users fall guy number.
    @commands.command()
    async def fallguys(self, ctx, number:int=None):
        await ctx.channel.purge(limit=1)
        if not number:
            with open('games.json') as json_file:
                player_list = json.load(json_file)
                embed = discord.Embed(title="**Fall Guys**", description="$fallguys [#] to add your number", color =0xf538ff)
                for player in player_list['user']:
                    try:
                        embed.add_field(name = f"@{player['name']}",value=player['fallguys'],inline=False)
                    except:
                        print('NOT FOUND')
                await ctx.send(embed = embed)
        else:
            self.write_to_json(str(ctx.author),f'Fall Guy {number}', 'fallguys')
            await ctx.send(f'Welcome, Fall Guy {number}.')
            

    #slippi - Keeps track of the users fall guy number.
    @commands.command()
    async def slippi(self, ctx, tag=None):
        await ctx.channel.purge(limit=1)
        if not tag:
            with open('games.json') as json_file:
                player_list = json.load(json_file)
                embed = discord.Embed(title="**Rollback Melee**", description="https://slippi.gg/", color =0xf538ff)
                for player in player_list['user']:
                    try:
                        embed.add_field(name = f"{player['name']}",value=player['slippi'],inline=False)
                    except:
                        print('NOT FOUND')
                await ctx.send(embed = embed)
        else:
            self.write_to_json(str(ctx.author),tag, 'slippi')
            await ctx.send(f'{tag} added. ISO can be found at https://drive.google.com/file/d/0B78DlVMCXjSFZWRSaGFxREQtQjg/view?usp=sharing')
        

def setup(client):
    client.add_cog(Games(client))