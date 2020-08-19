import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():   
    print(str(client.user) + ' has connected to Discord successfully.')
    
client.run(TOKEN)