import discord
from discord.ext import commands
import asyncio
from tokin import tokin
from genrate import generate

intents = discord.Intents.all()
intents.message_content = True  # Needed for on_message to read content

client = discord.Client(intents=intents)
activity = discord.Activity(type=discord.ActivityType.playing, name="MineCraft")

@client.event
async def on_ready():
    print(f'Bot is ready as {client.user}')
    await client.change_presence(activity=activity, status=discord.Status.idle)


@client.event
async def on_message(message : discord.Message):
    content = message.content
    if message.author == client.user:
        return  # avoid responding to itself
    response = generate(content.lower())
    await message.reply(response)


# Replace with your bot token
client.run(tokin)
