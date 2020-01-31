import json
import random
import discord
from discord.ext import commands

class Casino(commands.Cog):
    def __init__(self, client):
        self.client = client
        bankfilename = "bank.json"
        boardfilename = "board.json"
        boardimg = "board.png"
        payoutfilename "payout.json"

    #def get_payout_multiplier(self, bet_type):


    #cash - check how much currency a user currently has
    @commands.command()
    async def cash(self, ctx):

    @commands.command()
    async def roulette(self, ctx, bet_choice, bet_amount: int):
    #color - "red/black/green"
    #parity - p0 [none], p1 [odd], p2 [even]
    #column - c1, c2, c3
    #dozen - d1, d2, d3
    #half -h1, h2
        payout_mult = 1

        #betchoice->bet_type
        if bet_choice == 'red' or 'green' or 'black':
            bet_type = 'color'
        elif bet_choice[0] = 'p' and (bet_choice[1] == '1' or bet_choice[1] == '2') and (bet_choice[1] != '0'):
            bet_type = 'parity'
        elif bet_choice[0] = 'c' and (bet_choice[1] == '1' or bet_choice[1] == '2' or bet_choice[1] == '3'):
            bet_type = 'column'
        elif bet_choice[0] = 'd' and (bet_choice[1] == '1' or bet_choice[1] == '2' or bet_choice[1] == '3'):
            bet_type = 'dozen'
        elif bet_choice[0] = 'h' and (bet_choice[1] == '1' or bet_choice[1] == '2'):
            bet_type = 'half'
        #if invalid bet_choice
        else:
            bet_type = 'error'
            await ctx.send(f'ERROR; bet choice invalid\nUse format [bet_type][bet_choice]')

        if bet_type != 'error':


def setup(client):
    client.add_cog(Casino(client))
