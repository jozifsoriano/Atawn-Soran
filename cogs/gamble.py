import json
import random
import discord
from discord.ext import commands

PATH_TO_BANK_JSON = 'content/casino/bank.json'
PATH_TO_BOARD_JSON = 'content/casino/board.json'


class Casino(commands.Cog):
    def __init__(self, client):
        self.client = client

    # function for reading money of user from json
    def read_cash(self, user):
        with open(PATH_TO_BANK_JSON) as json_file:
            bank = json.load(json_file)
            for u in bank['user']:
                if user == u['name']:
                    return int(u['cash'])
                else:
                    self.write_cash(self, user, 3000)
                    return 3000

    # function for reading money of user and then writing [cash] money  to json
    def write_cash(self, user, cash: int):
        flag = False
        bank = {}
        bank['user'] = []
        with open(PATH_TO_BANK_JSON) as json_file:
            bank = json.load(json_file)
            for u in bank['user']:
                if user == u['name']:
                    flag = True  # user exists dont append
                    u['cash'] = cash
        if not flag:  # user does not exist in bank, append
            bank['user'].append({
                'name': user,
                'cash': cash
            })
        with open(PATH_TO_BANK_JSON, 'w') as outfile:
            json.dump(bank, outfile)

    # function for checking if user has enough money to gamble
    def check_balance(self, user, bet: int):
        balance = self.read_cash(user)
        print("chickaccheck" + str(balance))
        if (balance - bet) < 0:
            print("Error: not enough money")
            return -1  # error
        return 0  # can bet the amount

    # function for processing bets
    def process_bet(self, user, bet, payout_mult, winflag):
        final_balance = 0
        print("PROCESSING")
        if winflag == True:  # win
            start = self.read_cash(user)
            profit = bet*payout_mult
            final_balance = start + profit
        else:
            start = self.read_cash(user)
            final_balance = start - bet
        self.write_cash(user, final_balance)
        # return final_balance

    # cash - set cash for user to [cash]
    @commands.command()
    async def abcash(self, ctx, cash: int):
        self.write_cash(str(ctx.author), cash)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title='**BANK OF ANTAWNICA**',
                              description=f'Est. 1994', color=0x4432a8)
        embed.add_field(name=f"{ctx.author}'s New Balance like Kawhi: ",
                        value=f'[{cash}] BIG BALLER BRAND BUCKS.', inline=True)
        await ctx.send(embed=embed)

    # balance - check balance for a user
    @commands.command()
    async def balance(self, ctx):
        balance = self.read_cash(str(ctx.author))
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title='**BANK OF ANTAWNICA**',
                              description=f'Est. 1994', color=0x4432a8)
        embed.add_field(name=f"{ctx.author}'sbalance is ",
                        value=f'[{balance}] BIG BALLER BRAND BUCKS.', inline=True)
        await ctx.send(embed=embed)

    # rps - a friendly game of rock paper scissors
    @commands.command()
    async def rps(self, ctx, choice, bet: int):
        flag = self.check_balance(str(ctx.author), bet)
        winflag = -1
        payout_mult = 1
        if(flag == -1):
            choice = "Boy bye u broke as fuck"
        choices = ["rock", "paper", "scissors"]
        if choice in choices:
            cpu_choice = random.choice(choices)
            embed = discord.Embed(
                title='**JANKENPON**', description=f'CPU CHOSE *{cpu_choice}*', color=0x4432a8)
            if choice == cpu_choice:
                embed.add_field(name="It's a tie!",
                                value=f"No money lost. ", inline=True)
            elif choice == 'rock' and cpu_choice == 'paper':
                embed.add_field(name="Fat L boi.",
                                value=f"You lose {bet}. ", inline=True)
                payout_mult = 1
                winflag = 0
            elif choice == 'rock' and cpu_choice == 'scissors':
                embed.add_field(name="DUBS ONLY.",
                                value=f"You win {2*bet} ", inline=True)
                payout_mult = 1
                winflag = 1
            elif choice == 'paper' and cpu_choice == 'scissors':
                embed.add_field(name="Fat L boi.",
                                value=f"You lose {bet}. ", inline=True)
                payout_mult = 1
                winflag = 0
            elif choice == 'paper' and cpu_choice == 'rock':
                embed.add_field(name="DUBS ONLY.",
                                value=f"You win {2*bet} ", inline=True)
                payout_mult = 1
                winflag = 1
            elif choice == 'scissors' and cpu_choice == 'rock':
                embed.add_field(name="Fat L boi.",
                                value=f"You lose {bet}. ", inline=True)
                payout_mult = 1
                winflag = 0
            elif choice == 'scissors' and cpu_choice == 'paper':
                embed.add_field(name="DUBS ONLY.",
                                value=f"You win {2*bet} ", inline=True)
                payout_mult = 1
                winflag = 1
            final_balance = self.process_bet(
                str(ctx.author), bet, payout_mult, winflag)
            embed.add_field(name=f"{ctx.author}, your final balance is ",
                            value=f"{self.read_cash(str(ctx.author))}.")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='**JANKENPON**',
                                  description=f'ERROR', color=0x4432a8)
            if flag == -1:
                embed.add_field(name=choice, value="Get yo money", inline=True)
            else:
                embed.add_field(name="Not a valid choice.",
                                value=f"Choose {choices}. ", inline=True)
            await ctx.send(embed=embed)

    # table - creates a text channel for roulette
    @commands.command()
    async def table(self, ctx):
        await ctx.channel.purge(limit=1)
        channel = await ctx.message.author.guild.create_text_channel('Roulette Table')
        embed = discord.Embed(title=f"Welcome to the table",
                              description="$roulette [bet_choice] [bet_amount]")
        embed.add_field(name="color(1:1)", value="[red/black]", inline=True)
        embed.add_field(name="parity(1:1)",
                        value="[p1] for odd/[p2] for even", inline=True)
        embed.add_field(name="half(1:1)",
                        value="[h1] for 1-18/[h2] for 19-36", inline=True)
        embed.add_field(
            name="column(2:1)", value="[c1]for 1st column,[c2]for 2nd column,[c3]for 3rd column", inline=True)
        embed.add_field(
            name="dozen(2:1)", value="[d1] for 1st 12,[d2] for 2nd 12,[d3] for 3rd 12]", inline=True)
        embed.add_field(name="number(35:1)", value="[0-36]", inline=True)
        await channel.send(embed=embed)
        await channel.send(file=discord.File("singlezero.jpg"))

    # roulette - play a game of roulette
    @commands.command()
    async def roulette(self, ctx, bet_choice, bet_amount: int):
        # color - 1to1 - "red/black/green"
        colors = ["red", "black"]  # cant bet green
    # parity - 1to1 - p0 [none], p1 [odd], p2 [even]
    # column - 2to1 - c1, c2, c3
    # dozen - 2to1 - d1, d2, d3
    # half - 1to1 - h1, h2
    # number - 35to1 - [0-35]

        embed = discord.Embed(title="**ROULETTE**",
                              description=f"Can I see your ID?", color=0xf538ff)
        flag = self.check_balance(str(ctx.author), bet_amount)
        winflag = False
        payout_mult = 1  # if won, determine winning by calculating against this variable
        bet_type = ''

        # bet_choice->payout_mult&bet_type
        if bet_choice in colors:
            print(f"colors, {bet_choice}")
            payout_mult = 1
            bet_type = 'color'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        elif bet_choice[0] == 'p' and (bet_choice[1] == '1' or bet_choice[1] == '2') and (bet_choice[1] != '0'):
            print(f"parity {bet_choice[0]} {bet_choice[1]}")
            payout_mult = 1
            bet_type = 'parity'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        elif bet_choice[0] == 'c' and (bet_choice[1] == '1' or bet_choice[1] == '2' or bet_choice[1] == '3'):
            print(f"column {bet_choice[0]} {bet_choice[1]}")
            payout_mult = 2
            bet_type = 'column'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        elif bet_choice[0] == 'd' and (bet_choice[1] == '1' or bet_choice[1] == '2' or bet_choice[1] == '3'):
            print(f"dozen {bet_choice[0]} {bet_choice[1]}")
            payout_mult = 2
            bet_type = 'dozen'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        elif bet_choice[0] == 'h' and (bet_choice[1] == '1' or bet_choice[1] == '2'):
            print(f"half {bet_choice[0]} {bet_choice[1]}")
            payout_mult = 1
            bet_type = 'half'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        elif int(bet_choice) in range(0, 37):
            print(f"number {int(bet_choice)}")
            payout_mult = 35
            bet_type = 'number'
            embed.add_field(name=bet_choice,
                            value=f"{payout_mult}:1", inline=False)
        # if invalid bet_choice
        else:
            if flag == -1:
                embed.add_field(
                    name = bet_choice, value="Get yo money", inline=False)
            else:
                embed.add_field(
                    title=f'ERROR, {ctx.author}; Bet choice invalid.', value='Use format [bet_type][bet_choice]')
            await ctx.send(embed=embed)
        if flag != -1:
            roll = random.randint(0, 37)
            print(f'roll: {roll}')
            embed.add_field(name='**WINNING NUMBER:**',
                            value=f"**{roll}**", inline=False)
            with open(PATH_TO_BOARD_JSON) as json_file:
                board = json.load(json_file)
                result = board['board'][roll][bet_type]
                if(bet_type == 'color'):
                    if (result == bet_choice):
                        winflag = True
                elif (bet_type == 'number'):
                    if (result == int(bet_choice)):
                        winflag = True
                else:
                    if (result == bet_choice[1]):
                        winflag = True

            self.process_bet(str(ctx.author), bet_amount, payout_mult, winflag)
            embed.add_field(name=f"{ctx.author}, your final balance is ",
                            value=f"{self.read_cash(str(ctx.author))}.", inline=False)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Casino(client))
