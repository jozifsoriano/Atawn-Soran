import discord
from discord.ext import commands
import requests

API_KEY =  ''
tokenFile = open('token','r')
while True:
    line = tokenFile.readline()
    if not line:
        break
    splitLine = line.split(':')
    if splitLine[0] == 'youtube':
        API_KEY = splitLine[1]
        break

class Youtube(commands.Cog):

    def __init__(self, client):
        self.client = client
        #client.remove_command('help')

    #add_playlist_to_mee6 - send messages for adding videos by id using mee6 bot

    @commands.command()
    async def add_playlist_to_mee6(self, ctx, *, playlistId):
        playlistItem_object = requests.get(f'https://content-youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&key={API_KEY}&maxResults=10&playlistId={playlistId}')
        playlistItemJson = playlistItem_object.json()
        for item in (playlistItemJson['items']):
            await ctx.send(f"/add {item['contentDetails']['videoId']}")

def setup(client):
    client.add_cog(Youtube(client))
# https://discord.com/blog/welcome-to-the-new-era-of-discord-apps/?ref=message_content_notification