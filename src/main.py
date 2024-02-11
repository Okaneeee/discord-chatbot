# -- imports
## discord
import discord
from discord.ext import commands
from discord import app_commands

## stuff
from random import randint
from typing import Optional

## other 
from consts import SONGS
from func import which_function
from logger import Logger

## os & env
import sys
from os import getenv
from dotenv import load_dotenv

## neural network
from neuralintents import BasicAssistant

# -- config
LOGGER = Logger()
load_dotenv()

try:
    chatbot = BasicAssistant('./src/json/intents.json')
except FileNotFoundError:
    chatbot = BasicAssistant('../src/json/intents.json')

LOGGER.makeLog("Training model...", "INFO")
chatbot.fit_model(epochs=400)
LOGGER.makeLog("Saving model...", "INFO")
chatbot.save_model()

## const
TOKEN = getenv('TOKEN') # bot token
OWNID = getenv('OWNID') # own id
GUILD = discord.Object(id=int(getenv('GUILD'))) # type: ignore

if not TOKEN:
    LOGGER.makeLog("Undefined token", "CRITICAL")
    sys.exit("Undefined token")
if not OWNID: # NOTE: Remove if changing prefix
    LOGGER.makeLog("Undefined ID", "CRITICAL")
    sys.exit("Undefined ID")

PRFX: str = f"<@{OWNID}>" # NOTE: Edit if changing prefix

## discord client setup
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(PRFX, intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name=SONGS[randint(0, len(SONGS)-1)]))

LOGGER.makeLog("Bot is starting...", "INFO")

client.activity = discord.Activity(type=discord.ActivityType.listening, name=SONGS[randint(0, len(SONGS)-1)])

# -- bot
@client.event
async def on_ready():
    LOGGER.makeLog(f"Successfully loggged in as {client.user}", "INFO")
    LOGGER.makeLog(f"ID: {client.user.id}", "DEBUG") #type: ignore --- no error here
    sys.stdout.flush()
    await client.tree.sync(guild=GUILD)

@client.event
async def on_message(message):
    # Ignore self
    if message.author == client.user:
        return
    
    if message.content.startswith(PRFX):
        LOGGER.makeLog(f"Mentioned bot", "DEBUG")
        cb_response = chatbot.process_input(message.content[len(PRFX):])
        try:
            await message.channel.send(which_function(cb_response, message.content[len(PRFX):])) # type: ignore --- no error here
        except ModuleNotFoundError:
            await message.channel.send(cb_response)

## commands
@client.tree.command(
    name="ping",
    description="Replies with pong"
)
async def ping(interaction: discord.Interaction):
    """Get bot's latency"""
    try:
        LOGGER.makeLog(f"Invoked ping command ({round(client.latency * 1000)})", "DEBUG")
        await interaction.response.send_message(f"Pong! ||*with {round(client.latency * 1000)}ms*||")
    except discord.errors.NotFound or discord.app_commands.errors.CommandInvokeError:
        LOGGER.makeLog(f"Error occurred when calling *ping* command", "ERROR")
        await interaction.response.send_message(f"An error occurred...", ephemeral=True)

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
        LOGGER.makeLog(f"Invoked joined command for {member}", "DEBUG")
        await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore --- no error here either
    except discord.errors.NotFound or discord.app_commands.errors.CommandInvokeError:
        LOGGER.makeLog(f"Error occurred when calling *joined command", "ERROR")
        await interaction.response.send_message(f"An error occurred...", ephemeral=True)

@client.tree.command(
    name="song",
    description="Replies with a random song and changes the bot's activity to it"
)
async def song(interaction: discord.Interaction):
    """Get a random song"""
    try:
        LOGGER.makeLog(f"Invoked song command", "DEBUG")
        r_song = SONGS[randint(0, len(SONGS)-1)]
        await interaction.response.send_message(f"You should listen to {r_song}!")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=r_song))
    except discord.errors.NotFound or discord.app_commands.errors.CommandInvokeError:
        LOGGER.makeLog(f"Error occurred when calling *song* command", "ERROR")
        await interaction.response.send_message(f"An error occurred...", ephemeral=True)


# -- run
client.tree.copy_global_to(guild=GUILD)
client.run(TOKEN)