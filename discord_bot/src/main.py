# -- imports
## discord
import discord
from discord.ext import commands
from discord import app_commands

## stuff
# from random import randint
# import requests

## os & env
import sys
from os import getenv
from dotenv import load_dotenv

# -- config
load_dotenv()

## const
TOKEN = getenv('TOKEN')
GUILD = discord.Object(id=int(getenv('GUILD'))) # type: ignore

PRFX: str = ""

if not TOKEN :
    sys.exit("Undefined token")

## discord setup
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(PRFX, intents=intents)

print("Bot is starting...")

# -- bot
@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()
    await client.tree.sync(guild=GUILD)

@client.event
async def on_message(message):
    # Ignore self
    if message.author == client.user:
        return

@client.tree.command(
    name="ping",
    description="Replies with pong"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! ||with *{round(client.latency * 1000)}ms*||")

client.tree.copy_global_to(guild=GUILD)

client.run(TOKEN)