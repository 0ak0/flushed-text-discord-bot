import asyncio
import discord
import os
import time
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='flush=')


@client.event
async def on_ready():
    print(f'{client.user} connected.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="flush=="))


@client.command(name='=')
async def _play(ctx, *, arg):
    print('LOG: ' + str(ctx.author) + ' requested a flush')
    letter = 0
    for char in arg:

        letter += 1



client.run(token)
