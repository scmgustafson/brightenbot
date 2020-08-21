import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord successfully.')
    text_channels = discord.utils.get(client.get_all_channels(), guild__name=GUILD, name='general')
    await text_channels.send(content="Hello, World!")

client.run(TOKEN)
