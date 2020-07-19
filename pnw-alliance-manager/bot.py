import asyncio
import aiohttp
import discord
from discord.ext import commands
import json
import requests

TOKEN = "" # Hmm ask me or mebbe use ur own?

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name, client.user.id)

#from srv import keep_alive
#keep_alive()
client.run(TOKEN)
