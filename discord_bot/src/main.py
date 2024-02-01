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

## commands
@client.tree.command(
    name="ping",
    description="Replies with pong"
)
async def ping(interaction: discord.Interaction):
    """Get bot's latency"""
    await interaction.response.send_message(f"Pong! ||*with {round(client.latency * 1000)}ms*||")

@client.tree.command(
        name="joined",
        description="Says when a member joined",
)
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user # type: ignore --- no error here

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore --- no error here either

client.tree.copy_global_to(guild=GUILD)

client.run(TOKEN)