# -- imports
## discord
import discord
from discord.ext import commands
from discord import app_commands

## stuff
from random import randint
from typing import Optional

## other programs
from consts import SONGS
from func import which_function

## os & env
import sys
from os import getenv
from dotenv import load_dotenv

## neural network
from neuralintents import BasicAssistant

# -- config
load_dotenv()

try:
    chatbot = BasicAssistant('./src/json/intents.json')
except FileNotFoundError:
    chatbot = BasicAssistant('../src/json/intents.json')
print("[INFO] Training model...")
chatbot.fit_model()
print("[INFO] Saving model...")
chatbot.save_model()

## const
TOKEN = getenv('TOKEN') # bot token
OWNID = getenv('OWNID') # own id
GUILD = discord.Object(id=int(getenv('GUILD'))) # type: ignore


if not TOKEN:
    sys.exit("Undefined token")
if not OWNID:
    sys.exit("Undefined ID")

PRFX: str = f"<@{OWNID}>"

## discord client setup
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(PRFX, intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name=SONGS[randint(0, len(SONGS)-1)]))

print("[INFO] Bot is starting...")

# -- bot
@client.event
async def on_ready():
    print('[INFO] Successfully loggged in as {0.user}'.format(client))
    print('[DEBUG] ID: {0.user.id}'.format(client))
    sys.stdout.flush()
    await client.tree.sync(guild=GUILD)

@client.event
async def on_message(message):
    # Ignore self
    if message.author == client.user:
        return
    
    if message.content.startswith(PRFX):
        cb_response = chatbot.process_input(message.content[len(PRFX):])
        try:
            await message.channel.send(which_function(cb_response, message.content[4:])) # type: ignore --- no error here
        except ModuleNotFoundError:
            await message.channel.send(cb_response)

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
    try:
        await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore --- no error here either
    except discord.errors.NotFound or discord.app_commands.errors.CommandInvokeError:
        await interaction.response.send_message(f"An error occurred...", ephemeral=True)

client.tree.copy_global_to(guild=GUILD)

client.run(TOKEN)