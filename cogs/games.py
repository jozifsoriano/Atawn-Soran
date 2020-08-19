import discord
import random
import json
from discord.ext import commands

class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    # read and return json file
    def read_from_json(self, user, game):
        with open('games.json') as json_file:
            return json.load(json_file)

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
    async def fallguy(self, ctx, number:int=None):
        if not number:
            player_list = self.read_from_json(str(ctx.author), 'fallguys')
            embed = discord.Embed(title="**Fall Guys**", description="$fallguys [#] to add your number", color =0xf538ff)
            for player in player_list:
                embed.add_field(name = player['name'],value=player['fallguys'],inline=False)
            await ctx.send(embed = embed)
        else:
            self.write_to_json(str(ctx.author),f'Fall Guy {number}', 'fallguys')
            await ctx.send(f'Welcome, Fall Guy {number}.')
            
        
        

def setup(client):
    client.add_cog(Games(client))