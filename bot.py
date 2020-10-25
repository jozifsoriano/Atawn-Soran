# Works with Python 3.8
# https://discordapp.com/oauth2/authorize?client_id=603975462305136661&scope=bot

import logging
import os
import threading
from flask import Flask, render_template, request, redirect, url_for, session
from discord.ext import commands

# tokens and keys
DISC_TOKEN = ''
tokenFile = open('token', 'r')
while True:
    line = tokenFile.readline()
    if not line:
        break
    splitLine = line.split(':')
    if splitLine[0] == 'discord':
        DISC_TOKEN = splitLine[1]
        break
# Bot info
BOT_PREFIX = "$"
client = commands.Bot(command_prefix=BOT_PREFIX)
app = Flask(__name__)

@client.command()
async def load(ctx, extension):
    print(f'\n---\nLoading\n---\n')
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    print(f'\n---\nUnloading\n---\n')
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    print(f'\n---\nReloading\n---\n')
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


def run_disc():
    logging.info("Running Discord client.")
    # run the client
    client.run(DISC_TOKEN)
    logging.info("Closing Discord client.")


def run_flask():
    logging.info("Running flask.")
    app.run()
    logging.info("Closing flask.")


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == "__main__" :
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=run_disc)
    logging.info("Main    : before creating thread")
    y = threading.Thread(target=run_flask)
    logging.info("Main    : before running threads")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
