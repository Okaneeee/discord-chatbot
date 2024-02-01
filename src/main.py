# -- imports
## discord
import discord
from discord.ext import commands
from discord import app_commands

## stuff
from random import randint
from consts import SONGS
from typing import Optional
# import requests

## os & env
import sys
from os import getenv
from dotenv import load_dotenv

## neural network
from neuralintents import BasicAssistant

# -- config
load_dotenv()

chatbot = BasicAssistant('./src/json/intents.json')
print("[INFO] Training model...")
chatbot.fit_model()
print("[INFO] Saving model...")
chatbot.save_model()

## const
TOKEN = getenv('TOKEN') # bot token
OWNER = getenv('OWNER') # owner id
GUILD = discord.Object(id=int(getenv('GUILD'))) # type: ignore

PRFX: str = "$ai"

if not TOKEN:
    sys.exit("Undefined token")
if not OWNER:
    sys.exit("Undefined owner")

## discord client setup
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(PRFX, intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name=SONGS[randint(0, len(SONGS)-1)]))

print("[INFO] Bot is starting...")

# -- bot
@client.event
async def on_ready():
    print('[INFO] Successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()
    await client.tree.sync(guild=GUILD)

@client.event
async def on_message(message):
    # Ignore self
    if message.author == client.user:
        return
    
    if message.content.startswith(PRFX):
        response = chatbot.process_input(message.content[4:])
        await message.channel.send(response)

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