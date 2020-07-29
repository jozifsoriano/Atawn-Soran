import discord
from discord.ext import commands
import requests
import json

API_KEY =  ''
tokenFile = open('token','r')
while True:
    line = tokenFile.readline()
    if not line:
        break
    splitLine = line.split(':')
    if splitLine[0] == 'lol':
        API_KEY = splitLine[1]
        break
        
class LoL(commands.Cog):
    def __init__(self, client):
        self.client = client

    #lol - gives League of Legends information for given [summoner_name]
    @commands.command()
    async def lol(self, ctx, *, name):
        #get info from LoL API (summoner name, info, level, winrate)
        summoner_info = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key=+{API_KEY}')
        s_info = summoner_info.json()
        summoner_name = s_info['name'] #FIX THIS <---
        enc_id = s_info['id']
        league_info = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{enc_id}?api_key={API_KEY}')
        l_info = league_info.json()
        print(f"Enc_id: {enc_id}")
        level = s_info['summonerLevel']
        rank = f"{l_info[0]['tier']} {l_info[0]['rank']} at {str(l_info[0]['leaguePoints'])} LP."
        #rank = l_info[0]['tier']+' '+l_info[0]['rank']+ ' at '+str(l_info[0]['leaguePoints']) + ' LP.'
        wr_f = 100*l_info[0]['wins']/(l_info[0]['wins']+l_info[0]['losses'])
        wr = str("{0:.4f}".format(wr_f)) + '%'

        #create the embedded message to send
        msg = 'Here is the League of Legends info for '+ summoner_name +'.'
        embed = discord.Embed(title='**'+summoner_name+'**', description='*'+msg+'*', color=0x185d9e)
        embed.add_field(name="Level", value=str(level))
        embed.add_field(name="Rank", value=rank)
        embed.add_field(name="Win Rate", value=wr)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(LoL(client))
