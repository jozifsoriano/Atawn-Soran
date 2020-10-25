import discord
import random
import json
from discord.ext import commands


class Announcements(commands.Cog):

    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(Announcements(client))